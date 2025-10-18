from django.urls import path
from .views import SerieList, SerieCreate, SerieUpdate, SerieDelete

urlpatterns = [
    path('', SerieList.as_view(), name='series'),
    path('create/', SerieCreate.as_view(), name='serie_create'),
    path('update/<int:pk>/', SerieUpdate.as_view(), name='serie_update'),
    path('delete/<int:pk>/', SerieDelete.as_view(), name='serie_delete'),

]