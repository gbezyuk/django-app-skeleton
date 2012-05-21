
from django.db.utils import IntegrityError
from django.test import TestCase
from .factories import Item_Factory
from ..models import NewsItem
import datetime

class NewsTestCase(TestCase):
	'''
	test for NewsItem models
	'''
	def setUp(self):
		#raise ValueError('Hi! I am a bug!')
		"""
		Initialization with a factory-provided set of models
		"""
		self.first_item=Item_Factory()
		self.second_item=Item_Factory(title='Notorios is alive!',is_published=False)
		self.third_item=Item_Factory(title='eminem is truly black')
		#print NewsItem.published_list()
		
	def test_published_queryset(self):
		#raise ValueError(LOGIN_URL)
		'''
			testing queryset of published news. like context_processors. news_list
			
		'''
		for item in NewsItem.published_list() :
			self.assertEqual(item.is_published,True)
