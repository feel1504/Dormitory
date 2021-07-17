from django.db import models

# Create your models here.
class Myuser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
#学生表
class Student(models.Model):
    sno = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    ssex = models.BooleanField(default=0)
    sage = models.IntegerField()
    sdept = models.CharField(max_length=20)
    smajor = models.CharField(max_length=20)
    sgrade = models.CharField(max_length=20)
    stype = models.CharField(max_length=20)
    sintime = models.CharField(max_length=20)
    souttime = models.CharField(max_length=20)

#宿舍
class Dormitory(models.Model):
    sushe_num = models.CharField(max_length=30)
    louhao = models.CharField(max_length=20)
    quhao = models.CharField(max_length=10)
    cenghao = models.CharField(max_length=20)
    sushehao = models.CharField(max_length=20)
    max_occupancy = models.IntegerField()
    occupancy = models.IntegerField()
    telephone = models.CharField(max_length=15)

#管理员
class Admin(models.Model):
    emp_num = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=20)
    emp_sex = models.BooleanField(default=0)
    emp_age = models.IntegerField()

#缴费
class Pay(models.Model):
    pay_amount = models.FloatField()
    yongshuiliang = models.IntegerField()
    yongdianliang = models.IntegerField()

#报修
class Repair(models.Model):
    sushe = models.CharField(max_length=20,default='')
    people = models.CharField(max_length=20)
    data = models.CharField(max_length=20)
    reason = models.TextField(max_length=100)

class Waijian(models.Model):
    dormitory = models.ForeignKey("Dormitory", on_delete=models.CASCADE, default='')
    repair = models.ForeignKey("Repair", on_delete=models.CASCADE)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    admin = models.ForeignKey("Admin",on_delete=models.CASCADE)
    pay = models.ForeignKey("Pay",on_delete=models.CASCADE)


