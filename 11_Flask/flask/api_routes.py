### Put and Delete-HTTP verb
### Working with api--json

from flask import Flask,jsonify,request

app=Flask(__name__)

# Intial data to do list:

items =[
    
    {"id":1,"name":"Item1","discription":"This is item 1"},
    {"id":2,"name":"Item2","discription":"This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to the sample to do list App"

# Get :Retreve the all item
@app.route('/item',methods=['GET'])
def get_items():
    return jsonify(items)

# get : Retreve a specifick item by Id
@app.route('/item/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None) # here is call retreive the item
    if item is None:
        return jsonify({"error":"item are not fount"})
    return jsonify(item)

# Post : Creat  a new task - API
@app.route('/item',methods=['POST'])
def creat_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item are not fount"})
    new_item={
        "id":items[-1]["id"] +1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']
    }

    items.append(new_item)
    return jsonify(new_item)

# Put : update exiting item 
@app.route('/item/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item are not fount"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

# Delete: Delete an Item
@app.route('/item/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items= [item for item in items if item["id"]!=item_id ]
    return jsonify({"result":"Item Deleted"})



# Entry point
if __name__ == "__main__":
    app.run(debug=True)