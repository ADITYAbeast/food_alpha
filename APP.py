import firebase_admin
from firebase_admin import credentials,firestore
import flask
from flask import abort,jsonify,request,redirect
import json
import requests

app = flask.Flask(__name__)

cred = credentials.Certificate("food-alpha-9c051-firebase-adminsdk-dj3lz-d793fb53fb.json")
firebase_app = firebase_admin.initialize_app(cred)
store = firestore.client()




@app.route('/addResturant' ,methods=['POST'])
def addRESTURANT():
    data = request.get_json(force=True)
    dit={}
    dit["name"]=data.get("name")
    dit["mobile_no"]= data.get("mobile")
    dit["address"]=data.get("address")
    dit["image"] = data.get("imageUrl")
    dit["location"]={
                        "latitude":data.get("lat") ,
                        "longitude":data.get("lang")
                        
                        }
    dit["type"]=data.get("typ")
    dit["ID"]=data.get("rest_id")
    dit["AddedOnDate"]=firestore.SERVER_TIMESTAMP 
    store.collection("RESTURANT").add(dit)

    return jsonify({"response":200 })


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=False)