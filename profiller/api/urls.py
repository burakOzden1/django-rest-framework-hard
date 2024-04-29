from django.urls import path, include
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiller', ProfilViewSet)
router.register(r'durum', ProfilDurumViewSet)

urlpatterns = [
    path('', include(router.urls))
]

## HER DEFASINDA BUNLARI YAZMAK ZORUNDA DEGILIZ!!!!!!!
# from profiller.api.views import ProfilViewSet

# profil_list = ProfilViewSet.as_view({'get': 'list'})
# profil_detay = ProfilViewSet.as_view({'get': 'retrieve'})

# urlpatterns = [
#     path('kullanici-profilleri/', profil_list, name='profiller'),
#     path('kullanici-profilleri/<int:pk>', profil_detay, name='profil-detay'),
# ]
