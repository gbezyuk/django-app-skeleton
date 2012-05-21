"""
    Model factories for testing news application
"""

import factory
from news.models import NewsItem


class Item_Factory(factory.Factory):
    """
    Item model factory
    """
    FACTORY_FOR = NewsItem
    title = '2pac is alive!'
    body = '<p>some text</p> <!-- split --> <p>more text</p>'
    is_published=True
    published_at='2006-10-25 14:30:59'