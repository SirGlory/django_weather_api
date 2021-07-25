from django.conf.urls import url
from . import views

# url that accepts city as first parameter and accepts query string from /?days=<number_of_days>
# regex expression to account for majority of city names, allows space between the characters.
# Does not allow numbers or special characters. It will also not allow the space at the start and end.
urlpatterns = [
    url(r'^api/locations/(?P<city>[a-zA-Z][a-zA-Z ]+[a-zA-Z])/$', views.Temperatures.as_view(), name='home'),
]
