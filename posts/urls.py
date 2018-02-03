from django.conf.urls import url

from . import views

urlpatterns=[
                                                                    # urls work from top to bottom and left to right
    url(r'^create/$',views.posts_create,name='bob'),                # so if we have two same urls the first one will
    url(r'^$',views.posts_list,name='huston'),                      # will be rendered
    url(r'^(?P<id>\d+)/$',views.posts_detail,name='detail'),
    url(r'^update/$',views.posts_update,name='george'),
    url(r'^delete/$',views.posts_delete,name='hamilton'),


]