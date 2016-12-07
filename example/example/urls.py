from django.conf.urls import include, url
from django.contrib import admin

from .testapp import views

urlpatterns = [
    url(r'^$', views.TestFormView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
