from django.db import models

# Create your models here.
class team(models.Model):
    teamName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    point = models.BigIntegerField()

    st1 = models.CharField(max_length=50)    #队长名字
    stnum1 = models.CharField(max_length=50) #学号
    #qq1 = models.CharField(max_length=50)
    num1 = models.CharField(max_length=50)

    st2 = models.CharField(max_length=50)     #队员1名字
    stnum2 = models.CharField(max_length=50)  #学号
    #qq2 = models.CharField(max_length=50)
    num2 = models.CharField(max_length=50)

    st3 = models.CharField(max_length=50)     #队员2名字
    stnum3 = models.CharField(max_length=50)  #学号
    #qq3 = models.CharField(max_length=50)
    num3 = models.CharField(max_length=50)

class notice(models.Model):
    #title = models.CharField(max_length=50)
    info = models.CharField(max_length=500)

#class challenge(models.Model):
#   name        = models.CharField(max_length=50)
#    category    = models.CharField(max_length=50)
#    description = models.CharField(max_length=200)
#    value       = models.CharField(max_length=50)
#    flag        = models.CharField(max_length=100)

class challenge(models.Model):
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=500)
    flag = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    point = models.BigIntegerField(default=100)


class log(models.Model):
    challengeid = models.BigIntegerField()
    name = models.CharField(max_length=50)
    flag = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(default='2017-11-02 10:30:00')
    check = models.BooleanField()




