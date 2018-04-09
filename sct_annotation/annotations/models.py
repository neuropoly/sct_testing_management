from pathlib import Path

import logging
import nibabel as nib

from django.conf import settings
from django.db import models


logger = logging.getLogger(__name__)


class FileNameMixin(models.Model):

    OK_FILE = ('OK', 'File is available')
    NO_FILE = ('NA', 'File not available')
    ERR_FILE = ('ERR', 'File error')
    FILESTATE = (OK_FILE, NO_FILE, ERR_FILE)

    filename = models.CharField(
        'File path',
        max_length=512,
        unique=True,
        help_text=f'path prefix: {settings.SCT_DATASET_ROOT}'
    )
    filestate = models.CharField(
        'The state of the file',
        max_length=3,
        default='NA',
        choices=FILESTATE
    )

    def validate_filename(self):

        path = str(Path(settings.SCT_DATASET_ROOT) / self.filename)

        try:
            obj = nib.load(path)
            self.filestate = self.OK_FILE[0]
            logger.info(f'Path {path} exists')
            return obj
        except FileNotFoundError as err:
            self.filestate = self.NO_FILE[0]
            self.error_msg = str(err)
            logger.warning(err)
            return False
        except Exception as err:
            self.filestate = self.ERR_FILE[0]
            self.error_msg = str(err)
            logger.warning(err)
            return False

    def save(self, *args, **kwargs):
        self.validate_filename()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Acquisition(models.Model):

    date_of_scan = models.DateField(null=True, blank=True)
    center = models.CharField(max_length=32)
    scanner = models.CharField(max_length=32, null=True, blank=True)
    study = models.CharField(max_length=64)
    session = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.center} {self.study} {self.session}'

    class Meta:
        unique_together = (('center', 'study', 'session'))


class Demographic(models.Model):
    GENDER = (('M', 'Male'), ('F', 'Female'))
    acquisition = models.OneToOneField(
        Acquisition, on_delete=models.CASCADE, related_name='demographic'
    )
    surname = models.CharField(max_length=64, default='unknown')
    family_name = models.CharField(max_length=64, default='unknown')
    gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    pathology = models.CharField(max_length=128, null=True, blank=True)
    researcher = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'{self.surname} {self.family_name} {self.gender} {self.pathology}'


class Image(FileNameMixin):
    acquisition = models.ForeignKey(
        Acquisition, on_delete=models.CASCADE, related_name='images'
    )
    contrast = models.CharField(max_length=32)
    start_coverage = models.CharField(max_length=16, null=True, blank=True)
    end_coverage = models.CharField(max_length=16, null=True, blank=True)
    orientation = models.CharField(max_length=16, null=True, blank=True)
    resolution = models.CharField(max_length=16, null=True, blank=True,
                                  help_text='The resolution of the nifti file')
    # study
    pam50 = models.BooleanField(default=False,
                                help_text='Is image used in the generation of PAM50')
    ms_mapping = models.BooleanField(default=False,
                                     help_text='Is image used in mapping MS')
    gm_model = models.BooleanField(default=False,
                                   help_text='Is image used to model gray matter')

    def __str__(self):
        return f'{self.contrast} -- {self.acquisition}'

    def save(self, *args, **kwargs):
        img = self.validate_filename()
        if img:
            resolution = img.header.get_zooms()
            self.resolution = 'x'.join(['{0:.2f}'.format(i) for i in resolution])

        super().save(*args, **kwargs)


class LabeledImage(FileNameMixin):
    CORD = ('seg_manual', 'Binary mask of spinal cord')
    GM = ('gmseg_manual', 'Binary mask of gray matter')
    LESION = ('lesion_manual', 'Binary mask of lesions')
    DISC = (
        'labels_disc', 'Single voxel at the posterior tip of each inter-vertebral disc'
    )
    LABELS = (CORD, GM, LESION, DISC)
    contrast = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='labeled_images'
    )
    label = models.CharField(max_length=16,
                             choices=LABELS,
                             help_text='What type of labeled image')
    author = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f'{self.label} -- {self.contrast}'
