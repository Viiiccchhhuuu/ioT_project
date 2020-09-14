from flask import Flask
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

#creating the app.

app= Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:database.db'
db=SQLAlchemy(app)
class sensorDatabase(db.Model):
    device_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String, nullable=False)
    sensor_level = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    def __repr__(self):
        return("The device ID is:=%r" % self.device_id)

db.create_all()         #database created, remove this line after executing once.


sensor_put_args= reqparse.RequestParser()
sensor_put_args.add_argument("device_id", type=int, help="error!", required=True)
sensor_put_args.add_argument("location", type=str, help="error!",required=True)
sensor_put_args.add_argument("owner", type=str, help="error!",required=True)
sensor_put_args.add_argument("sensor_level", type=str, help="error!",required=True)
sensor_put_args.add_argument("status", type=str, help="error!",required=True)


resource_fields = {
    'device_id': fields.String,
    'location': fields.String,
    'owner': fields.String,                         #ALL THE DATA TYPES , EXCEPT THE DEVICE_ID,  ARE OF TYPE STRING IN THE DATABASE.
    'sensor_level': fields.String,
    'status': fields.String
}




class sensor(Resource):
    @marshal_with(resource_fields)
    def get(self,device_id,sensor_level,location,owner,status):         #THE GET API FOR THE DATA READING CONTINUOUSLY
        result = sensorDatabase.query.filter_by(id=device_id).first()
        return result

    @marshal_with(resource_fields)
    def get(self, device_id, sensor_level, location, owner, status):
        result = sensorDatabase.query.filter_by(id=device_id).first()                   #GET API FOR THE OUTPUT STATE
        return result

    @marshal_with(resource_fields)
    def get(self, device_id,status , location):
        result = sensorDatabase.query.filter_by(id=device_id).first()           # THE GET API FOR THE INITIAL CONFIGURATION (CALLED ONLY ONCE)
        return result





# shoving into db

api.add_resource(sensor,"/sensor/<int:device_id>")
if __name__ == "__main__":
    app.run(debug=True)