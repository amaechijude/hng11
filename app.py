import requests, random, json
from flask import Flask,request,jsonify, redirect, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/api/hello')


@app.route(r"/api/hello", methods=['GET'])
def help():
    response = requests.get('https://api64.ipify.org?format=json').json()

    visitor_name = request.args.get('visitor_name', default='Mark')
    ip_address = response["ip"]
    location = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    city = location.get("city")
    temp = " 33 "

    response = {
            "client_ip": ip_address,
            "location": city,
            "s_greeting": f'Hello {visitor_name}, the temperature is {temp} degrees celcius in {city}',

            }
    return jsonify(response)




#if __name__ == '__main__':
#   app.run(debug=False)


