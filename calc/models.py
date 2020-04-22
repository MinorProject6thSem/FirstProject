from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
class Teachers(models.Model):
    teacherId = models.IntegerField()
    teacherName = models.CharField(max_length=100)
    teacherPhone = models.CharField(max_length=10)
    teacherEmailId = models.EmailField(max_length=254)
    '''def __unicode__(self):
        return (self.teacherId, self.teacherName,self.teacherPhone,self.teacherEmailId)'''

class classroom(models.Model):
    room1 = models.IntegerField()
    room2 = models.IntegerField()
    room3 = models.IntegerField()
    room4 = models.IntegerField()
    '''priority=models.IntegerField()'''


class addcourse(models.Model):
    coursename=models.CharField(max_length=100)
    subject1=models.CharField(max_length=100,default="")
    subject2=models.CharField(max_length=100,default="")
    subject3=models.CharField(max_length=100,default="")
    subject4=models.CharField(max_length=100,default="")
    teacher1=models.CharField(max_length=100,default="")
    teacher2=models.CharField(max_length=100,default="")
    teacher3=models.CharField(max_length=100,default="")
    teacher4=models.CharField(max_length=100,default="")
    '''priority=models.IntegerField()'''

class timetable(models.Model):
    section1=models.CharField(max_length=100)
    section2=models.CharField(max_length=100)
    section3=models.CharField(max_length=100)
    section4=models.CharField(max_length=100)