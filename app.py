from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# define a list of stores
# each list entry in stores is a dictionary
# each dictionary has a 'name' and a list of items
# each item is a dictionary containing a name and a price
stores = [
	{
		'name': 'My Wonderful Store',
		'items': [
			{
			'name': 'My Item',
			'price': 15.99
			}
		]
	}
]


# from the POV of a server
# POST - used to recieve data
# GET - used to send data back

@app.route('/')
def home():
	return render_template('index.html')


# POST /store data: {name:}
# creats a new store for a given name
@app.route('/store', methods=['POST']) # create an endpoint as a POST
def create_store():
	request_data = request.get_json() 
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)


# GET /store/<string:name>
# gets a store for a given name and return info about it
@app.route('/store/<string:name>')
def get_store(name):
	# Iterate over stores
	for store in stores:
	# If the store name mathces, return it
		if store['name'] == name:
			return jsonify(store)
	# If none match, return an error message
		else:
			return jsonify({'message': 'Store not found'})


# GET /store
# returns a list of all the stores
@app.route('/store') # create an endpoint as a GET (endpoints are GET by default)
def get_stores():
	return jsonify({'stores': stores}) # Converts stores variable into JSON ({'sotres': stores}) because JSON is a dictionary



# POST /store/<string:name>/item {name: price:}
# create an item inside a store for a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)
		else:
			return jsonify({'message': 'Store not found'})




# GET /store/<string:name>/item
# get all the items in a specific store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items': store['items']})
		else:
			return jsonify({'message': 'Store not found'})



app.run(port=5000)