from flask import Flask, render_template, request
from weather import *
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not bool(city.strip()):
        city = 'Lagos'
    weather_data = get_weather_condition(city)

    if not weather_data['cod'] == 200:
        return render_template('city_not_found.html')

    return render_template("weather.html",
        title=weather_data['name'],
        description=weather_data['weather'][0]['description'].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port="8000")