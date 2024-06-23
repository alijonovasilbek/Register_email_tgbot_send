from django.db import models


class RegionUser(models.Model):
    region_name=models.CharField(max_length=99)

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name='Region'
        db_table='Region_table'


class ClassUser(models.Model):
    class_name=models.CharField(max_length=44)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name='Class'
        db_table='Class_table'


class UserInformation(models.Model):
    first_name = models.CharField(max_length=255)
    phone_your = models.CharField(max_length=13)
    region=models.ForeignKey(RegionUser,on_delete=models.CASCADE)
    class_user=models.ForeignKey(ClassUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name='User_information'
        db_table='user_table'

