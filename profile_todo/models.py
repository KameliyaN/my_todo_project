from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    pic = models.URLField(null=True, blank=True)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    passw = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Todo(models.Model):
    prof = Profile.objects.first().id if Profile.objects.first() else 1
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE, default=prof)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    is_done = models.BooleanField(blank=False)

    def __str__(self):
        return self.title
