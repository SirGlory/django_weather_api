from django.conf.urls import url
from . import views

# url that accepts city as first parameter and accepts query string from /?days=<number_of_days>
urlpatterns = [
    url(r'^api/locations/(?P<city>[a-zA-Z][a-zA-Z ]+[a-zA-Z])/$', views.Temperatures.as_view(), name='home'),
]
