from django.urls import path, include
from reviews.admin import admin

import reviews.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", reviews.views.index),
    path("book-search/", reviews.views.book_search, name="book_search"),
    path("", include("reviews.urls")),

]
