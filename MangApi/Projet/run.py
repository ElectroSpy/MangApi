import os
from sys import stderr

from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

mangadb = mongo.db.mangadb

@app.route('/', methods=['GET', 'POST'])
def index():
    categorie = mangadb.find().distinct('categorie')
    if request.method == "POST":
        selected_categorie = request.form.getlist("categorie")
        recherche = request.form.get("recherche")
        if recherche:
            recherche = str.capitalize(recherche)
            mangadbs = mangadb.find({"titre": {"$regex": recherche}})
        elif not selected_categorie and not recherche:
            mangadbs = mangadb.find().sort("titre", 1)
        else:
            mangadbs = mangadb.find(
                    {"categorie": {"$in": selected_categorie}}
            ).sort("titre", 1)
        countmanga = mangadbs.count()
        return render_template('index.html', mangadbs=mangadbs, categorie=categorie, countmanga=countmanga)
    else:
        mangadbs = mangadb.find().sort("titre", 1)
        countmanga = mangadbs.count()
        return render_template('index.html', mangadbs=mangadbs, categorie=categorie, countmanga=countmanga)


@app.route('/detail/<id>', methods=['GET'])
def detail(id):
    solo_mangadb = mangadb.find_one({'_id': ObjectId(id)})
    return render_template('detail.html', solo_mangadb=solo_mangadb)


@app.route('/add_manga', methods=['GET'])
def page_add_manga():
    return render_template('add_manga.html')

@app.route('/add', methods=['POST'])
def add_manga():
    titre = request.form.get('titre')
    auteur = request.form.get('auteur')
    categorie = request.form.get('categorie')
    statut = request.form.get('statut')
    sortie = request.form.get('sortie')
    nombre = request.form.get('nombre')
    description = request.form.get('description')
    image_card = request.form.get('image_card')
    image_back = request.form.get('image_back')
    mangadb.insert_one({'titre': titre, 'auteur': auteur, 'categorie': categorie, 'description': description, 'image_card': image_card, 'image_back': image_back})
    return redirect(url_for('index'))


@app.route('/mangadb_delete/<id>', methods=['POST'])
def delete_manga(id):
    mangadb.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))


@app.route('/mangadb_update/<id>', methods=['POST'])
def update_manga(id):
    titre = request.form.get('titre')
    auteur = request.form.get('auteur')
    categorie = request.form.get('categorie')
    statut = request.form.get('statut')
    sortie = request.form.get('sortie')
    nombre = request.form.get('nombre')
    description = request.form.get('description')
    image_card = request.form.get('image_card')
    image_back = request.form.get('image_back')

    updated_mangadb = mangadb.find_one({'_id': ObjectId(id)})

    updated_mangadb["titre"] = titre
    updated_mangadb["auteur"] = auteur
    updated_mangadb["categorie"] = categorie
    updated_mangadb["statut"] = statut
    updated_mangadb["sortie"] = sortie
    updated_mangadb["nombre"] = nombre
    updated_mangadb["description"] = description
    updated_mangadb["image_card"] = image_card
    updated_mangadb["image_back"] = image_back

    mangadb.replace_one({'_id': ObjectId(id)}, updated_mangadb)
    return redirect(url_for('detail', id=id))

@app.route('/mangadb/<id>', methods=['GET'])
def detail_manga_test(id):
    solo_mangadb = mangadb.find_one({'_id': ObjectId(id)})
    return render_template('detail_test.html', solo_mangadb=solo_mangadb)

@app.route('/categorie/<categorie>', methods=['GET'])
def categorie_manga(categorie):
    categorieFiltre = mangadb.find().distinct('categorie')
    mangadbs = mangadb.find({'categorie': categorie}).sort("titre", 1)
    countmanga = mangadbs.count()
    return render_template("index.html", mangadbs=mangadbs, categorie=categorieFiltre, countmanga=countmanga)

@app.route('/categorie/<categorie>/desc', methods=['GET'])
def categorie_manga_desc(categorie):
    categorieFiltre = mangadb.find().distinct('categorie')
    mangadbs = mangadb.find({'categorie': categorie}).sort("titre", -1)
    countmanga = mangadbs.count()
    return render_template("index.html", mangadbs=mangadbs, categorie=categorieFiltre, countmanga=countmanga)

@app.route('/desc/', methods=['GET', 'POST'])
def index_desc():
    categorie = mangadb.find().distinct('categorie')
    mangadbs = mangadb.find().sort("titre", -1)
    countmanga = mangadbs.count()
    return render_template('index.html', mangadbs=mangadbs, categorie=categorie, countmanga=countmanga)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
