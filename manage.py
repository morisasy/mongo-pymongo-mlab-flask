# APP
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
#mongo = PyMongo(app)


# data configurations
app.config['MONGO_DBNAME'] = 'XXXXX'
app.config['MONGO_URI'] = 'mongodb://user:password@ds123946.mlab.com:23946/fXXX'
# initialize db connections
mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({"name": "Rajabu", "language": "Swahili", "gender": "His"})
    user.insert({"name": "Susi", "language": "Finnish" , "gender": " Her"})
    user.insert({"name": "Mahombi", "language": "Lingala" , "gender": "His"})
    user.insert({"name": "Yasama", "language": "Shiraz" , "gender": "Her"})
    return "Added Users !"

@app.route('/find')
def find():
    user = mongo.db.users
    find_name = user.find_one({"name": "Yasama"})
    return ("You found " + find_name["name"] + "." + find_name["gender"] + " favorites language is "+ find_name["language"] + " !")

@app.route('/update')
def update():
    user = mongo.db.users
    updated_name = find_name = user.find_one({"name": "Susi"})
    updated_name["language" ] = "Suomi"
    user.save(updated_name)
    return("updated " + updated_name["language"] + " !")

@app.route('/delete')
def delete():
    user = mongo.db.users
    delete_name = user.find_one_and_delete({"name": "Susi"})
    #delete_name.delete_one()
    return(" deleted !")

if __name__ == '__main__':
    app.run(debug = True)
