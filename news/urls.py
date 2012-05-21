from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to, direct_to_template
from news.models import NewsItem
import datetime
from news.views import *
from news.feed import NewsFeed

#now=datetime.datetime.now()
#queryset = NewsItem.objects.filter(is_published=True).filter(published_at__lt=now).order_by('-published_at')[:3]

urlpatterns = patterns('',
	url(r'^$', redirect_to, { 'url': '/news/list' }, name='index'),
	url(r'list$',news_list,name='list'),
	url(r'(?P<item_id>\d+)/$',news_detail,name='detail'),
	url(r'archive$',archive,name='archive'),
	url(r'^feed/$', NewsFeed(), name='feed'),
)