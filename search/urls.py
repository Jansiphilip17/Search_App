from django.urls import path

from .views import SearchAPIView, ContentListAPIView

urlpatterns = [
    path("search/", SearchAPIView.as_view(), name="search-api"),
    path("content/", ContentListAPIView.as_view(), name="content-list-api"),
]
