from crypt import methods
from flask import Flask, jsonify,request

app  = Flask(__name__)
data = [
    {
        "ID": 1,
        "Contact": u"Raju",
        "Name": u"9987644456",
        "Done":False
    },
    {
        "ID": 2,
        "Contact": u"Rahul",
        "Name": u"9876543222",
        "Done":False
    }
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "Message":"Please provide the data"
        },400)

    contact = {
        "ID": data[-1]["ID"]+1,
        "Title": request.json["Title"],
        "Description": request.json.get("Description",""),
        "Done":False
    }

    data.append(contact)
    return jsonify({
        "status":"Sucess",
        "Message":"Contact added sucessfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })

if (__name__ == "__main__"):
    app.run(debug = True)