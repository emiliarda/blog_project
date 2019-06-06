from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^cat_food/$', views.post_cat_food, name='post_cat_food'),
    url(r'^behavioral_problems/$', views.post_behavioral_problems, name='post_behavioral_problems'),
    url(r'^new_kitten/$', views.post_new_kitten, name='post_new_kitten'),
    url(r'^sick_cat/$', views.post_sick_cat, name='post_sick_cat'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^register/', views.register, name='register'),
]
