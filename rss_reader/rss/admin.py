from django.contrib import admin

# Register your models here.

from .models import RssChanel, Article, Tags, Profile

admin.site.register(RssChanel)
admin.site.register(Article)
admin.site.register(Tags)
admin.site.register(Profile)
