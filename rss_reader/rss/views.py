from django.shortcuts import render, redirect

from django.contrib.auth import get_user

# Create your views here.

from .models import RssChanel, Article, Tags, Profile, User
from django.http import HttpResponse,JsonResponse, HttpResponseNotFound

import feedparser

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import json

@login_required #Проверка на вход пользователя
def index(request):

    if request.GET.get("tag"):
        tag = request.GET["tag"]
        articles = Article.objects.filter(tags__name = tag)
    else:
        articles = Article.objects.all().order_by('date')

    #tags = Tags.objects.all()
    all_articles = []
  
    for article in articles:
      tags = []
      for tag in article.tags.all():
        tags.append(tag)

      json_articless = {"title":article.title, "link": article.link, "date":article.date, "tags": tags, "summary":article.summary, "id":article.id}
      all_articles.append(json_articless)
      
      
    return render(
        request,
        "index.html",
        context={'articles':all_articles},
    )


def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('index')
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form,})

def tags(request):
    tag = request.GET["tags"]
    if len(tag) < 2:
      return HttpResponseNotFound("400")
    tags = Tags.objects.filter(name__contains=tag)
    all_tags = {}
    for tag in tags:
      all_tags[tag.name] = None
    print(all_tags)
    return JsonResponse(all_tags,safe=False) 

@login_required
def save(request):
    try:
      id = request.GET["id"]
      arcticle = Article.objects.get(id=id)
      prof = Profile.objects.create(user_id=request.user.id)
      
      prof.save_article.add(arcticle)
      prof.save()
      return HttpResponse(request)
    except:
      return HttpResponseNotFound(request)

@login_required   
def saved(request):
  articles = Profile.objects.filter(user_id = request.user.id)
  all_articles=[]
  for art in articles:
    for article in art.save_article.all():
      tags = []
      for tag in article.tags.all():
        tags.append(tag)
        json_articless = {"title":article.title, "link": article.link, "date":article.date, "tags": tags, "summary":article.summary, "id":article.id}
      all_articles.append(json_articless)
      
  print(all_articles)
  return render(
      request,
      "save_articles.html",
      context={'articles':all_articles},
  )

def delete(request):
  print("______---------______--------______------")
  #try:
  id = request.GET["id"]
  print(id)
  arcticle = Article.objects.get(id=id)
  print(arcticle)
  profs = Profile.objects.filter(user_id=request.user.id, save_article=arcticle)
  
  for prof in profs:
    print(prof)
    prof.delete()
  prof.save()

  return HttpResponse(request)
  #except:
    #return HttpResponseNotFound(request)