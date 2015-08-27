from django.db import models


class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField()
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'About me'


class Project(models.Model):
    title = models.CharField(max_length=100)
    is_owner = models.BooleanField()
    participate_from = models.DateField()
    participate_to = models.DateField()
    url = models.URLField()
    thumb_url = models.FilePathField()


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField()


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=8)


class Community(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        verbose_name_plural = 'Communities'
