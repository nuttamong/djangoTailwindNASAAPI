from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

api_key = os.environ.get('API_KEY')

class Apod:
    def __init__(self):
        url_apod = "https://api.nasa.gov/planetary/apod?api_key={}".format(api_key)
        apod_res = requests.get(url_apod)
        self.apod_loaded_data = json.loads(apod_res.text)
        self.daily_image = self.apod_loaded_data['url']
        self.url_image = self.apod_loaded_data['url']
        self.title = self.apod_loaded_data['title']
        self.explanation = self.apod_loaded_data['explanation']
        self.date = self.apod_loaded_data['date']
        try:
            self.owner = self.apod_loaded_data['copyright']
        except:
            self.owner = None

class MarRover:
    def __init__(self, date = '2024-2-19', rover_name = 'curiosity'):
        url_mar = "https://api.nasa.gov/mars-photos/api/v1/rovers/{}/photos?earth_date={}&api_key={}".format(rover_name, date, api_key)
        mar_res = requests.get(url_mar)
        self.date = date
        self.mar_loaded_data = json.loads(mar_res.text)

    def camera_info(self):
        img_data = []
        for i in self.mar_loaded_data['photos']:
            info_dict = {
                "camera_name": i['camera']['name'],
                "camera_full_name": i['camera']['full_name'],
                "camera_img": i['img_src'],
            }
            img_data.append(info_dict)
        return img_data

init_apod_data = Apod()
init_mar_data = MarRover()

# Create your views here.
def home(req):
    return render(req, 'home.html')

def apod(req):
    apod_data = init_apod_data

    daily_image = apod_data.daily_image
    url_image = apod_data.url_image
    title = apod_data.title
    explanation = apod_data.explanation
    date = apod_data.date
    owner = apod_data.owner

    context = {
        'daily_image': daily_image,
        'title':title,
        'explanation':explanation,
        'date':date,
        'url': url_image,
    }

    if owner:
        context['owner'] = owner

    return render(req, 'apod.html', context)

def startMarPage(req):
    data = init_mar_data.camera_info()
    
    context = {
        'mar_img': data,
        'date': init_mar_data.date,
    }
    return render(req, 'mar_photo.html', context)

def reMarPage(req):
    date = req.POST['datepicker']
    list_date = date.split("-")
    year = list_date[0]
    month = list_date[1]
    day = list_date[2]

    if month[0] == '0':
        month = month[1]

    if day[0] == '0':
        day = day[1]

    re_date = "{}-{}-{}".format(year, month, day)
    
    mar_data = MarRover(re_date)

    data = mar_data.camera_info()

    context = {
        'mar_img': data,
        'date': mar_data.date,
    }
    return render(req, 'mar_photo.html', context)
