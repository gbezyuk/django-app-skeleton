# Create your views here.
from django.views.generic.simple import redirect_to, direct_to_template
from news.models import NewsItem
from django.http import HttpResponse
import datetime

#now=datetime.datetime.now()
#queryset = NewsItem.objects.filter(is_published=True).filter(published_at__lt=now).order_by('-published_at')[:3]



def news_list(request):
	return direct_to_template(request,'news/news_item_list.haml',{'queryset': NewsItem.published_list()[:3],})
	
def news_detail(request,item_id):
	return direct_to_template(request,'news/news_item_detail.haml',{'object': NewsItem.objects.all().get(id=item_id)})
	
def archive(request):
	return direct_to_template(request,'news/news_archive.haml',{'queryset': NewsItem.published_list(),})