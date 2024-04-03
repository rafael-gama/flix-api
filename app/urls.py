from django.contrib import admin
from django.urls import path

from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'), 
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
    
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    

]
