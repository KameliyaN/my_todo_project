from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    picture = models.URLField()
    email = models.EmailField()
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=20)


class Todo(models.Model):
    prof = Profile.objects.first().id if Profile.objects.first() else 1
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE, default=prof)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)

