from django.db import models

# Create your models here.
class USER(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    usarName = models.CharField(max_length=100)
    PassWord = models.CharField(max_length=100)
    def __str__(self):
        return self.usarName

    class Meta:
        db_table="users"


class ARTICLE(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    atricle = models.CharField(max_length=1000)
    img = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.atricle

    class Meta:
        db_table="atricles"