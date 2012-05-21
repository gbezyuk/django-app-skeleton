from django.db import models
from model_utils.fields import SplitField
import datetime
# Create your models here.

class NewsItem(models.Model):
	title=models.CharField(max_length=100,default='', blank=False, null=False, verbose_name=(u'title'))
	body=SplitField()
	is_published = models.BooleanField(default=False, verbose_name=(u'is published'))
	published_at = models.DateTimeField(verbose_name=(u'published at'))
	
	def __unicode__(self):
		return self.title
	@classmethod
	def published_list(self):
		now=datetime.datetime.now()
		queryset = NewsItem.objects.filter(is_published=True).filter(published_at__lt=now).order_by('-published_at')
		return queryset
	@models.permalink
	def get_absolute_url(self):
		return ('news:detail', (), { 'item_id': self.id })

