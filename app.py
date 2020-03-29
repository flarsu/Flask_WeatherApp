import requests
from flask import Flask, render_template, request,redirect,flash,url_for


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/form', methods=['GET','POST'])


def city():
        city ='Shimla'
        if request .method == 'POST':
                city = request.form['city']
        if city == None or city == '':
                city = 'Shimla'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=dc5649c5d57673d96b686f4141f94b6f'

        r = requests.get(url.format(city)).json()
        print(r)

        description = r['weather'][0]['description']
        temprature = r['main']['temp']
        icon = r['weather'][0]['icon']
        
        # def ftoc():
        #        c = (5/9)*(temprature-32)
        #        return round(c,1)
        return render_template('weather1.html', title='WEATHER APP', city = city, description = description, temprature = temprature, icon = icon)
        





if __name__ =="__main__":
        app.run(debug =True , port = 5500)