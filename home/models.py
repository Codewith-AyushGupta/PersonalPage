from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from tinymce import models  as tinymce_models
from import_export.admin import ImportExportModelAdmin
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class project(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    short_about = tinymce_models.HTMLField()
    short_aboutshort_about = models.CharField(default="",max_length=500)
    decription=tinymce_models.HTMLField()
    image=models.ImageField()
    status = models.IntegerField(choices=STATUS, default=1)
    date_time=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title