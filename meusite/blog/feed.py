__author__ = 'will'


from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import Post

class LatestEntriesFeed(Feed):
    title = "GalvanicLoop.com Posts"
    link = "/post/"
    description = ""

    def items(self):
        return Post.objects.order_by('-date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.subtitle

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('Post', args=[item.id, ""])