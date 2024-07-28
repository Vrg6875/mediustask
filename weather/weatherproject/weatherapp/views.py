from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
import logging

def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'indore'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=cf4a1b5c4f94e1c2fd468b9505a4cefb'
    PARAMS = {'units':'metric'}

    API_KEY = 'AIzaSyBAunsRxfEu50lwLhl2RSJ5AOC1yJRRpYw'

    SEARCH_ENGINE_ID = '418f5f1e0894f49c0'
                       
 
     
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    search_items = data.get("items")

    if search_items:

     image_url = search_items[0]['link'] 
    else:
    
     image_url = None 


    try:
          
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
      
          day = datetime.date.today()

          return render(request,"weatherapp/index.html" ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )
               
    


def homepage(request):
    return render(request,"homepage.html")  