from django.contrib import admin
from django.urls import path, include

from search.views import home_view, course_detail_view, category_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("search.urls")),
    path("course/<int:pk>/", course_detail_view, name="course-detail"),
    path("category/<str:category>/", category_view, name="category-view"),
    path("", home_view, name="home"),
]
