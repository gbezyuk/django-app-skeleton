from django.utils.translation import ugettext_lazy as _
from django.contrib.syndication.views import Feed
from news.models import NewsItem
import datetime

class NewsFeed(Feed):
	title = _('site news')
	link = "/news/"
	description = _('site news')

	def items(self):
		#from datetime.datetime import now
		#now=datetime.datetime.now()
		return NewsItem.published_list()

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.body.content