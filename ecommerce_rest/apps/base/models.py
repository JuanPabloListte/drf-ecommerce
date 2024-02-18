from django.db import models

# Create your models here.
class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    created_date = models.DateField('Created Date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Modified Date', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Deleted Date', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = "Base Model"
        verbose_name_plural = "Base Models"


