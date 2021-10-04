from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router=DefaultRouter()
router.register('user', views.UserViewSet)
router.register('country', views.CountryViewSet)
router.register('city', views.CityViewSet)
router.register('game', views.GameViewSet)
router.register('category', views.CategoryViewSet)
router.register('characteristic_user', views.characteristic_userViewSet)
router.register('gender', views.GenderViewSet)
router.register('detail_user', views.Detail_UserViewSet)
router.register('detail_category', views.Detail_CategoryViewSet)
router.register('detail_game', views.Detail_GameViewSet)


urlpatterns = [
      path('', include(router.urls)),
      path('login/', views.UserLoginApiView.as_view()),

      #path('detail-user-list/', views.Detail_UserViewSet.detail_userList, name="detail_userList"),
      #path('detail-user-create/', views.Detail_UserViewSet.detail_userCreate, name="detail_userCreate"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)