from typing_extensions import Self
from unicodedata import name
from flask import Flask,jsonify,request
from flask_cors import CORS

class Contact:
    def __init__(self, id, req) -> None:
        self.id = id
        self.name = req.get("Name")
        self.contact = req.get("Contact")
    def returnDict(self):
        return {'ID':self.id, 'Name':self.name, "Contact":self.contact}

contacts = []

app = Flask(__name__)
CORS(app)

@app.route("/")
def sayHello():
    return "<b>Contact List</b>"

@app.route("/adddata", methods=["POST"])
def addtask():
    if not request.args:        
        return jsonify({"Status":"error","Error":"Please provide the data!"}, 400)
    else:
        contact = Contact(len(contacts), request.args)
        contacts.append(contact)
        print([str(i.returnDict()) for i in contacts])
        return jsonify({"Status":"Success","message":"Task added"})


#Execute Main function

if __name__ == "__main__": 
    app.run()