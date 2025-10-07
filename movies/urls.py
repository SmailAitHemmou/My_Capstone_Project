from django.urls import path
from .views import MovieList, MovieDetail, MovieCreate, MovieUpdate, MovieDelete

urlpatterns = [
    path('', MovieList.as_view(), name='movies'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('create/', MovieCreate.as_view(), name='movie_create'),
    path('update/<int:pk>/', MovieUpdate.as_view(), name='movie_update'),
    path('delete/<int:pk>/', MovieDelete.as_view(), name='movie_delete'),

]