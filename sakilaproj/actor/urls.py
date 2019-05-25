from django.urls import path

from .views import ActorList, ListCreateSongsView

urlpatterns = [
    path('actor/', ActorList.as_view(), name="songs-all"),
    path('addActor/', ListCreateSongsView.as_view(), name="songs-list-create"),
]
