from flask import Flask,jsonify
from flask_cors import CORS
#flask-CORS->helps in cross origin request(It Enables the 'origin')
 
app=Flask(__name__) # To create app instance
cors=CORS(app,origins="*") # To enable CORS


@app.route('/api/users',methods=['GET'])
def get_users():
    return jsonify(
        {
            "users":[
             'Anand',
             'Suresh',
             'Ramesh',
             'Vinod'
            ]
        }
    )
   

if __name__=='__main__':
    app.run(debug=True,port=8080)

