from flask import Flask
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:database.db'
db=SQLAlchemy(app)
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return("The name is:=%r" % self.name)





db.create_all()

video_put_args= reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="error!", required=True)
video_put_args.add_argument("views", type=int, help="error!",required=True)
video_put_args.add_argument("likes", type=int, help="error!",required=True)
videos={}

#def abortion_function(video_id):
   # if video_id not in videos:
    #    abort(404,messaage="Video ve ila da venna....")                 # I SAT WITH THE ERROR THAT ABORT WAS UNDEFINED FOR A FEW MINUTES , BUT THEN SAME LIKE IN SPRING BOOT , I HIT COMMAND SPACE FOR SUGGESTIONS ,
                                                                    # AND GOT THE RESTFUL API SUGGGESTION , SLEECTED ABORT IN THAT.
        # NOW IT WORKs
                        # note if you're using abort you have to put the status cide first then only the message="message here"
#def abort_if_video_exists(video_id):
 #   if video_id in videos:
  #      abort(404, message="Video already exists with the same video ID....")
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result= VideoModel.query.filter_by(id=video_id).first()
        return result
        #abortion_function(video_id)  # CALLING THE IMPLEMENTED PROGRAM TO PREVENT PROGRAM CRASH.
        #return videos[video_id]\
    @marshal_with(resource_fields)
    def put(self, video_id):
       # abort_if_video_exists(video_id)

        args = video_put_args.parse_args()   # this pafrt puts the parser into function
        video = VideoModel(id=video_id , name= args['name'] , views=args['views'] , likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

        #return videos[video_id] ,201       # to show http status for created
    #def delete(self,video_id):
        #abortion_function(video_id)
       #del videos[video_id]
        #return ''  # 404 returned automatically

        #return "", 204



print(videos)

api.add_resource(Video,"/video/<int:video_id>")
if __name__ == "__main__":
    app.run(debug=True)
