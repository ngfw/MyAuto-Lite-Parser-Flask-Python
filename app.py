# Делаем импорт
from flask import Flask, render_template,request
import requests
from bs4 import BeautifulSoup





app = Flask(__name__)

# mainpage = 'http://www.myauto.ge/'
pageurl = 'http://www.myauto.ge/?action=search&page='





@app.route('/')
@app.route('/index')

def index():
    
    r = requests.get(pageurl)
    soup = BeautifulSoup(r.content, 'html.parser')
            
    data = []
    for cars in soup.find_all('div', {'class': 'current-item'}):
        car_info = {} # Start with an empty dictionary for each car.

        car_info['name'] = cars.find("div", {"class": "car-name-wrapper"}).find('a').get_text()
        car_info['year'] = cars.find("p", {"class": "car-levy car-year"}).get_text()
        car_info['engine'] = cars.find("div", {"class": "car-detail-in cr-engine"}).get_text()
        car_info['mileage'] = cars.find("div", {"class": "car-detail-in cr-road"}).get_text()
        car_info['image'] = cars.find("figure", {"class": "search-list-figure"}).find('img').get('src')
        car_info['link'] = cars.find('a').get('href')
        car_info['wheel'] = cars.find("div", {"class": "car-detail-in cr-wheel"}).get_text()
        car_info['transmision'] = cars.find("div", {"class": "car-detail-in cr-wheel"}).get_text()
        car_info['status'] = cars.find("p", {"class": "car-levy"}).get_text()
        car_info['price'] = cars.find("h4", {"class": "h4-price"}).get_text()
            # car_info['desc'] = cars.find("p", {"class": "cr-det-info"}).get_text()



        data.append(car_info)


    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
