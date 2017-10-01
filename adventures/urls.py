from django.conf.urls import url
#from Adventure.views import MyAdventureView, AdventureList

from django.contrib import admin

from .views import (
    AdventureCreateAPIView,
    AdventureDeleteAPIView,
    AdventureDetailAPIView,
    AdventureListAPIView,
    AdventureUpdateAPIView,
    )

from .views import (
    MyAdventureCreateAPIView,
    MyAdventureDeleteAPIView,
    MyAdventureDetailAPIView,
    MyAdventureListAPIView,
    MyAdventureUpdateAPIView,
    )


urlpatterns = [
    #url(r'^Adventure/', AdventureList.as_view()),
    #url(r'^myAdventure/', MyAdventureView.as_view()),
    #from coding youtyube
    url(r'^adventure/$', AdventureListAPIView.as_view(), name='list'),
    url(r'^adventure/create/$', AdventureCreateAPIView.as_view(), name='create'),
    url(r'^adventure/(?P<pk>[\d-]+)/$', AdventureDetailAPIView.as_view(), name='detail'),
    url(r'^adventure/(?P<pk>[\d-]+)/edit/$', AdventureUpdateAPIView.as_view(), name='update'),
    url(r'^adventure/(?P<pk>[\d-]+)/delete/$', AdventureDeleteAPIView.as_view(), name='delete'),

    url(r'^myadventure/$', MyAdventureListAPIView.as_view(), name='list'),
    url(r'^myadventure/create/$', MyAdventureCreateAPIView.as_view(), name='create'),
    url(r'^myadventure/(?P<pk>[\d-]+)/$', MyAdventureDetailAPIView.as_view(), name='detail'),
    url(r'^myadventure/(?P<pk>[\d-]+)/edit/$', MyAdventureUpdateAPIView.as_view(), name='update'),
    url(r'^myadventure/(?P<pk>[\d-]+)/delete/$', MyAdventureDeleteAPIView.as_view(), name='delete'),
]