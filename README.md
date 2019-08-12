# PythonAPITest
Simple project using python to provide Api endpoint for http post and save data to mangodb afterward.

# Getting Started
The script has been tested in Ubuntu 18.04.1. To test the script, simply put the file helloApi.py under a folder and access it with console.

## Prerequisites
The script require pymongo and flask-restful to provide mongo db connection and REST api support. To install the modules:
```
$pip install flask-restful
$pip install pymongo==2.7.2
```

## installing
on the helloApi.py file, below line need to be replaced the ip address and port number with real mongodb setting. 
```
connection = Connection('localhost', 27017)
```
on the console, run below command to start up the API
```
$pythone helloApi.py
```
The API endpoint should be open at port 5002 localhost.

## Run the tests
Use postman to send a http post to http://localhost:5002/hello
if need to run postman on another computer. below line in helloApi.py file need to replace localhost to the ip address of your api endpoint.
```
app.run(debug=True, port='5002',host='localhost')
```
postman should return respond > hello Stranger!
Use postman to send another http post to http://localhost:5002/hello, this time with *name=James* on the body 
postman should return respond > hello James

## verify the data in mongo db
a record of {'Visit_name': 'James'} should be able to find with command in mongo shell
```
use hellodb
db.Visitors.find()
```

