from django.conf.urls import url
from adventures.views import MyAdventuresView, AdventuresList


urlpatterns = [
    url(r'^adventures/', AdventuresList.as_view()),
    url(r'^myadventures/', MyAdventuresView.as_view()),
]
