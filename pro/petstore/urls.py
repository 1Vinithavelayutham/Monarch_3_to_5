from django import views
from django.contrib import admin
from django.urls import path
from petstore import views
from petstore.views import SimpleView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("name/",views.names),
    path("contact/",views.contact),
    path("edit/<rid>",views.edit),
    path("delete/<rid>",views.delete),
    path('simple',SimpleView.as_view()),
    path('home/',views.home),
    path('dtl/',views.hello),

]