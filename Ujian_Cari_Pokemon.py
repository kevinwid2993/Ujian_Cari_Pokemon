from flask import Flask, render_template, redirect, request, url_for, jsonify
import json, requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil', methods=['POST', 'GET'])
def post():
    name=request.form['nama']
    url='https://pokeapi.co/api/v2/pokemon/'+name
    poke=requests.get(url)

    filenama=poke.json()['forms']

    nama=filenama[0]['name']

    filegambar=poke.json()['sprites']

    gambar=filegambar['front_default']

    idPoke=poke.json()['id']

    berat=poke.json()['weight']

    tinggi=poke.json()['height']

    files=[nama,gambar,idPoke,berat,tinggi]

    return render_template('hasil.html',x=files)

@app.route('/NotFound')
def NotFound():
    return render_template('error.html')

if __name__=='__main__':
    app.run(debug=True)