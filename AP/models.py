from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class ArtWork(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Art Author')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, verbose_name='Art Category')
    art = models.FileField(upload_to='./media', null=False, verbose_name='Art Image')
    name = models.CharField(max_length=50, null=False, verbose_name='Art Name')
    desc = models.TextField(null=True, verbose_name='Art Description')
    published = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published = timezone.now()
        self.save()


class Category(models.Model):
    name = models.CharField(null=False, max_length=50, verbose_name='Category Name')
    desc = models.TextField(null=True, verbose_name='Category Description')

    class Meta:
        verbose_name_plural = 'Categories'
