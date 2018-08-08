from django.db import models

# Create your models here.

#关联班级表
class Grades(models.Model):

    gname     = models.CharField(max_length=20)
    gdate     = models.DateTimeField()
    ggirlnum  = models.IntegerField()
    gboynum   = models.IntegerField()
    isDelete  = models.BooleanField(default=False)

    def __str__(self):
        return self.gname

#关联学生表
class Students(models.Model):

    sname    = models.CharField(max_length=20)
    sgender  = models.BooleanField(default=True)
    sage     = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #设置外键
    sgrade   = models.ForeignKey("Grades")

    def __str__(self):
        return self.sname