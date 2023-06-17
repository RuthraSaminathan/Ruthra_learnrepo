from flask import Flask,jsonify
from src.jsoner import show_the_write


app=Flask(_name_)

@app.route('/api/printHello')
def hello():
    data={'value':'Hello World'}
    return jsonify(data)


@app.route('/api/modifyRecepie')
def modrec():
    data=show_the_write()
    return jsonify(data)


if _name=='main_':
    app.run(debug=True,port=80)
