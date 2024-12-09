from django.urls import path

from . import views

app_name = 'historias'


""""Urls para a primeira e segunda parte com views funcionais sem classes genericas"""
""""
urlpatterns = [
    path('', views.list_historias, name='index'),
    path('<int:historia_id>/', views.detail_historia, name='detail'),
    path('search/', views.search_historias, name='search'),
    path('create/', views.create_historia, name='create'),
    path('update/<int:historia_id>/', views.update_historia, name='update'),
    path('delete/<int:historia_id>/', views.delete_historia, name='delete'),

    path('', views.HistoriaListView.as_view(), name='index'),
] """


""""Mudanças das urls para a implantação das classes genéricas"""
urlpatterns = [
    path('', views.HistoriaListView.as_view(), name='index'),
    path('<int:pk>/', views.HistoriaDetailView.as_view(), name='detail'),
    path('search/', views.search_historias, name='search'),
    path('create/', views.HistoriaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.HistoriaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.HistoriaDeleteView.as_view(), name='delete'),
    path('<int:historia_id>/comment/', views.create_comment, name='comment'),
    path('categorias/', views.CategoriaListView.as_view(), name='categorias'),
    path('categorias/create', views.CategoriaCreateView.as_view(), name='createcategoria'),
    path('categorias/<int:pk>', views.historiascatego, name='indexcatego'),
]