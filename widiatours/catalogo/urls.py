from django.urls import path
from . import views

urlpatterns = [
    #LOGIN 
    path('iniciosesion',views.iniciosesion,name='iniciosesion.html'),
    path('creacionusuario',views.creacionusuario,name='creacionusuario.html'),
    #PAGINAS
    path('',views.index,name='index.html'),
    path('compra/<str:pk>',views.CompraDetailView.as_view(), name='compra-detail'),
    path('compra/', views.CompraListView.as_view(), name='compra'),
    path('users/<str:pk>',views.UsuarioDetailView.as_view(), name='user-detail'),
    path('users/', views.UsuarioListView.as_view(), name='usuario'),
    path('acercadeee',views.acercadeee,name='acercadeee.html'),
    path('tienda',views.tienda,name='tienda.html'),
    path('quehacer',views.quehacer,name='quehacer.html'),
    #---------TIENDA---------
    #ACCESORIOS 
    path('camping',views.camping,name='camping.html'),
    path('playa',views.playa,name='playa.html'),
    path('nieve',views.nieve,name='nieve.html'),
    path('kayak',views.kayak,name='kayak.html'),
    path('trekking',views.trekking,name='trekking.html'),
    path('ciclismo',views.ciclismo,name='ciclismo.html'),
    #VESTIMENTA
    path('chaqueta',views.chaqueta,name='chaqueta.html'),
    path('poleron',views.poleron,name='poleron.html'),
    path('polera',views.polera,name='polera.html'),
    path('pantalon',views.pantalon,name='pantalon.html'),
    path('short',views.short,name='short.html'),
    path('calzado',views.calzado,name='calzado.html'),

]

urlpatterns += [
    #compra
    path('compra/create/', views.CompraCreate.as_view(), name='compra_create'),
    path('compra/<str:pk>/update/', views.CompraUpdate.as_view(), name='compra_update'),
    path('compra/<str:pk>/delete/', views.CompraDelete.as_view(), name='compra_delete'),
    #usuario
    path('usuario/create/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('users/<str:pk>/update/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('users/<str:pk>/delete/', views.UsuarioDelete.as_view(), name='usuario_delete'),
]