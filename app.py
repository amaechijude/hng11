import requests, time
from flask import Flask,request,jsonify,redirect
from decouple import config

app = Flask(__name__)

@app.route("/")
def index():
    time.sleep(1)
    return redirect('/api/hello')


@app.route(r"/api/hello", methods=['GET'])
def help():
    response = requests.get('https://api64.ipify.org?format=json').json()

    visitor_name = request.args.get('visitor_name', default='Mark')
    ip_address = response["ip"]
    location = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    city = location.get("city")

    try:
        api_key = config('api_key')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
        time.sleep(1)
        resp = requests.get(url).json()
        temperature = resp.get('main', {}).get('temp')
        temperature_celsius = round(temperature - 273.15, 2)
    except:
        temperature_celsius = "Unknown"


    output = {
            "client_ip": ip_address,
            "location": city,
            "greeting": f'Hello {visitor_name}, the temperature is {temperature_celsius} degrees celcius in {city}',

            }
    return jsonify(output)




if __name__ == '__main__':
    app.run()


