from django.contrib import admin
from models import Post, Poster
from forms import PostForm



class PostAdmin(admin.ModelAdmin):
    form = PostForm

    class Media:
        css = {'all': ('/media/codemirror/theme/solarized.css',
                       '/media/codemirror/lib/codemirror.css',)
        }

        js = ("/media/codemirror/lib/codemirror.js",
              "/media/codemirror/mode/markdown/markdown.js",
              "/media/js/Markdown.Converter.js",
              "/media/js/Markdown.Editor.js",
              "/media/js/Markdown.Sanitizer.js",
              "/media/js/jquery-1.11.2.min.js",
              "/media/js/jquery.cookie.js",
              "/media/js/shortcut.js",)


admin.site.register(Post, PostAdmin)

admin.site.register(Poster)

