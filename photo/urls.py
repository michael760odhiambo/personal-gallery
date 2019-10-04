from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home, name='home'),
    url('^today/$',views.photo_of_day, name='photoToday'),
    url('^archives/(\d{4}-\d{2}-\d{2})',views.past_days_photos, name='pastPhotos')

]