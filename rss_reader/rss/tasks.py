# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta 
import feedparser

from .models import RssChanel, Article, Tags
import json
import time

@periodic_task(run_every=(timedelta(minutes=1)), name="my_first_task")
def my_first_task():
    print("run")
    Article.objects.all().delete() 
    Tags.objects.all().delete() 
    rss_url = RssChanel.objects.all()
    for url in rss_url:
        feed = feedparser.parse(str(url))
        for entry in feed.entries:
            json_entry = json.dumps(entry)
            try:
                print(entry.published[:-7])
                publish_struct =time.strptime(entry.published[:-7],'%a, %d %b %Y %H:%M')
                publish_time= time.strftime('%Y-%m-%d %H:%M',publish_struct)
                my_article = Article(title = entry.title, link = entry.link, summary = entry.summary, date = publish_time)
                my_article.save()

            except Exception as e: print(e)

            
            if 'tags' in entry:
                for tag in entry.tags:
                    try:
                        #print("-------")
                        my_tags = Tags(name = tag.term)
                        my_tags.save()
                        
                        art_b = Article.objects.get(link = entry.link)
                        tag_b = Tags.objects.get(name = tag.term)
                        art_b.tags.add(tag_b)
                        art_b.save()
                    except:
                        pass

                    #art_b = Article.objects.get(link = entry.link)
                    #tag_b = Tags.objects.get(name = tag.term)
                    #art_b.tags.add(tag_b)
                    #art_b.save()
                    


            else:
                pass

            


