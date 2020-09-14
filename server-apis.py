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
    'device_id': fields.Integer,
    'location': fields.String,
    'owner': fields.String,                         #ALL THE DATA TYPES , EXCEPT THE DEVICE_ID,  ARE OF TYPE STRING IN THE DATABASE.
    'sensor_level': fields.String,
    'status': fields.String
}

data1=  {
    'device_id': 1 ,
    'location': "Chennai",
    'owner': "Vichu",                         #ALL THE DATA TYPES , EXCEPT THE DEVICE_ID,  ARE OF TYPE STRING IN THE DATABASE.
    'sensor_level': "Full",
    'status': "Running"
}
#db.session.add(data1)
#db.session.commit()


class sensor(Resource):
    @marshal_with(resource_fields)
    @app.route('/getdata', methods=['GET'])
    def getdata(self,device_id):         #THE GET API FOR THE DATA READING CONTINUOUSLY
        result = sensorDatabase.query.filter_by(id=device_id).first()
        return result

    @marshal_with(resource_fields)
    @app.route('/getOutputState', methods=['GET'])
    def outputstate(self, device_id):
        result = sensorDatabase.query.filter_by(id=device_id).first()    #GET API FOR THE OUTPUT STATE
        return result.status



    @marshal_with(resource_fields)
    @app.route('/getConfig', methods=['GET'])
    def config(self, device_id):
        result = sensorDatabase.query.filter_by(id=device_id).first()           # THE GET API FOR THE INITIAL CONFIGURATION (CALLED ONLY ONCE)
        return {result.location, result.owner, result.status}





# shoving into db

api.add_resource(sensor,"/sensor/<int:device_id>")
if __name__ == "__main__":
    app.run(debug=True)
