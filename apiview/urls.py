from django.urls import path

from .views import CategoryAPI,ProductSignsAPI,ProductSignsAPIDelete,ProductDetailSignsAPI,ProductUpdate
urlpatterns = [
    path('category/', CategoryAPI.as_view()),
    path('musicklip/', ProductSignsAPI.as_view()),
    path('musicklip_detail/<int:pk>', ProductDetailSignsAPI.as_view()),
    path('musicklipdelete/<int:pk>', ProductSignsAPIDelete.as_view()),
    path('musicklipupdate/<int:pk>', ProductUpdate.as_view()),


]