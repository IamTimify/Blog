from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import *
from django.contrib.sitemaps.views import sitemap
from posts.sitemaps import PostSitemap


sitemaps = {
    "posts": PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('contact/', contact,name = 'contact' ),
    path('search/', search, name = 'search'),
    path('tos/', tos, name = 'tos'),
    path('add_post/', add_post, name = 'add_post'),
    path('faq/', faq, name = 'faq'),
    path('postlist/<slug>/', postlist, name = 'postlist'), 
    path('posts/', allposts, name = 'allposts'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
