import db_handler as handler
from flask import Flask, request, jsonify

'''
This is the API router. When using this it will run on localhost:5000 which means that
it is being hosted by the computer running it. The computer running the server will connect to the database and
serve the data from there.

APIs have things called endpoints and there are 4 main methods for data interaction
GET: retrieving information
POST: sending information
PATCH: updating information
DELETE: deleing information

endpoints look similar to website addresses (theyre kinda similar one serves html data API typically do json)
ex endpoint:
localhost:8080/users
-A GET request to this endpoint would give you all the users in the database
-A POST request to this endpoint might allow a user to send a body of data (formatted a certain way in JSON) which would
be parsed by the API logic to send it to the database
'''


#app is a flask object
app = Flask(__name__)

'''
by running the python code and going to ur browser localhost:5000/users it will 
send a GET request to this endpoint which will trigger it to send the data from the table users
the other endpoints arent tested but they have a similar premise except the body and header
of the request will have to be different
'''
@app.route('/users', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def users():
    if request.method == 'GET':
        # Retrieve all users
        return handler.data_GET("USERS")

    elif request.method == 'POST':
        # Example of how to get data from the request body
        data = request.get_json()
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        handler.data_INSERT("users", columns, values)
        return jsonify({'message': 'User added successfully'})

    elif request.method == 'PATCH':
        # Example of how to update data
        data = request.get_json()
        handler.data_UPDATE("users", data['column_new'], data['data_new'], data['column_old'], data['data_old'])
        return jsonify({'message': 'User updated successfully'})

    elif request.method == 'DELETE':
        # Example of how to delete data
        data = request.get_json()
        handler.data_DELETE("users", data['column'], data['value'])
        return jsonify({'message': 'User deleted successfully'})

@app.route('/goals', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def goals():
    if request.method == 'GET':
        # Retrieve all users
        return handler.data_GET("GOALS")

if __name__ == '__main__':
    app.run(debug=True)