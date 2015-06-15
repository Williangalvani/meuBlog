__author__ = 'will'


from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import Post

class LatestEntriesFeed(Feed):
    title = "GalvanicLoop.com Posts"
    link = "http://galvanicloop.com/blog/post/"
    description = ""

    def items(self):
        return Post.objects.filter(published=True).order_by('-date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.subtitle

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return "http://galvanicloop.com/blog/post/{0}/".format(item.id)#reverse('Post', args=[item.id, ""])