from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

def home(request):
    return render(request,"all_photos/home.html")

def photo_of_day(request):
    date = dt.date.today()
   # day = convert_dates(date)

 
    return render(request,'all_photos/today-photos.html',{'date':date})



def past_days_photos(request,past_date):
    try:

        # Converts data from the string Url
         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http400()
        assert False
    if date == dt.date.today():

         return redirect(photo_of_day)

    return render(request,'all_photos/past-day-photo.html', {'date':date})             
    day = convert_dates(date)

   
