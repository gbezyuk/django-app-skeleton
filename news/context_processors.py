from django.conf import settings
from news.models import NewsItem
import datetime

def news_list(request):
	now=datetime.datetime.now()
	return {
		'published_list': NewsItem.published_list(),
		'request': request
	}