from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    tz = models.CharField(max_length=30) 

    def __str__(self):
        return self.name


class Activity_peroid(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)