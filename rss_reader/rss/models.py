from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class RssChanel(models.Model):

    site_name = models.CharField(max_length=200)

    rss_url = models.URLField(max_length=200, unique = True)

    def __str__(self):
        return self.rss_url

class Tags(models.Model):

    name = models.CharField(max_length=200, unique = True)

    def __str__(self):
        return self.name
    

class Article(models.Model):

    #article_id = models.AutoField(primary_key=True)
    #article = models.TextField(unique = True)
    title = models.TextField(default="default")
    link = models.URLField(unique = True)
    date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tags)
    summary = models.TextField(default="default")




class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    save_article = models.ManyToManyField(Article)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()