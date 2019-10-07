from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home, name='home'),
    url('^today/$',views.photo_of_day, name='photoToday'),
    url('^celeb/$',views.celeb, name='photoCeleb'),
    url('^city/$',views.city, name='photoCity'),
    url('^land/$',views.land, name='photoLand'),
    url('^morning/$',views.morning, name='photoMorning'),
    url('^ocean/$',views.ocean, name='photoOcean'),
    url('^sun/$',views.sun, name='photoSun'),
    url('^tree/$',views.tree, name='photoTree'),
    url('^archives/(\d{4}-\d{2}-\d{2})',views.past_days_photos, name='pastPhotos'),
    url(r'^search/', views.search_results, name='search_results')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    