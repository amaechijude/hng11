import requests, random, json
from flask import Flask,request,jsonify, redirect, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/api/hello')


@app.route(r"/api/hello", methods=['GET'])
def help():
    visitor_name = request.args.get('visitor_name', default='Mark')
    ip_address = " 192 "
    city = " anambra "
    temp = " 33 "

    response = {
            "client_ip": ip_address,
            "location": city,
            "s_greeting": f'Hello {visitor_name}, the temperature is {temp} degrees celcius in {city}',

            }
    return jsonify(response)




if __name__ == '__main__':
    app.run(debug=True)


