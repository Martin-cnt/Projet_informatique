from flask import Flask, render_template, redirect, g, request
import pymysql.cursors
from datetime import datetime
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'une cle(token) : grain de sel(any random string)'

                                    ## à ajouter
from flask import session, g
import pymysql.cursors

def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="localhost",                 # à modifier
            user="martin",                     # à modifier
            password="Chavanne02!",                # à modifier
            database="mcuinet5",        # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()
@app.route('/', methods=['GET'])
def show_layout():
    return render_template('layout.html')

@app.route('/type-animal/show', methods=['GET'])
def show_type_animal():
    mycursor = get_db().cursor()
    sql = """ SELECT * FROM type_animal"""
    mycursor.execute(sql)
    type_animals = mycursor.fetchall()
    return render_template('type-animal/show_type_animal.html', type_animals = type_animals )

@app.route('/type-animal/add', methods=['GET'])
def add_type_animal():
    mycursor = get_db().cursor()

    sql = "SELECT * FROM type_animal ORDER BY nom_type"
    mycursor.execute(sql)
    type_animals = mycursor.fetchall()
    return render_template('type-animal/add_type_animal.html', type_animals=type_animals)

@app.route('/type-animal/add', methods=['POST'])
def valid_add_type_animal():
    mycursor = get_db().cursor()
    nom_type = request.form.get('nom_type', '')

    sql = """ INSERT INTO type_animal (nom_type) VALUES (%s)"""
    mycursor.execute(sql, (nom_type,))
    get_db().commit()
    return redirect('/type-animal/show')

@app.route('/type-animal/edit', methods=['GET'])
def edit_type_animal():

    mycursor = get_db().cursor()

    id_type_animal = request.args.get('id_type_animal', None)

    sql = """ SELECT * FROM type_animal WHERE id_type_animal = %s"""
    mycursor.execute(sql, (id_type_animal,))
    type_animals = mycursor.fetchone()
    return render_template('type-animal/edit_type_animal.html', type_animals = type_animals )

@app.route('/type-animal/edit', methods=['POST'])
def valid_edit_type_animal():
    mycursor = get_db().cursor()
    id_type_animal = request.form.get('id_type_animal')
    nom_type = request.form.get('nom_type', '')

    sql = """ UPDATE type_animal SET nom_type = %s WHERE id_type_animal = %s"""
    mycursor.execute(sql, (nom_type, id_type_animal))
    get_db().commit()
    return redirect('/type-animal/show')

@app.route('/type-animal/delete', methods=['POST'])
def delete_type_animal():
    id = request.form.get('id', '')
    mycursor = get_db().cursor()
    sql = """DELETE FROM type_animal WHERE id_type_animal = %s"""
    mycursor.execute(sql, (id,))
    get_db().commit()
    return redirect('/type-animal/show')



@app.route('/animal/show', methods=['GET'])
def show_animal():
    mycursor = get_db().cursor()
    sql = """ SELECT * FROM animaux"""
    mycursor.execute(sql)
    animals = mycursor.fetchall()

    sql_type_animal = """SELECT * FROM type_animal"""
    mycursor.execute(sql_type_animal)
    type_animals = mycursor.fetchall()

    return render_template('animal/show_animaux.html', animals=animals, type_animals=type_animals )



@app.route('/animal/add', methods=['GET'])
def add_animal():
    mycursor = get_db().cursor()

    sql="""SELECT * FROM animaux"""
    mycursor.execute(sql)
    animals = mycursor.fetchall()

    sql="""SELECT id_type_animal FROM type_animal"""
    mycursor.execute(sql)
    type_animals = mycursor.fetchall()

    return render_template('animal/add_animal.html', animals=animals, type_animals=type_animals)

@app.route('/animal/add', methods=['POST'])
def valid_add_animal():
    mycursor = get_db().cursor()

    type_animal_id = request.form.get('type_animal_id', '')
    nom_animal = request.form.get('nom_animal', '')
    prix_achat = request.form.get('prix_achat', '')
    date_naissance = request.form.get('date_naissance', '')
    couleur = request.form.get('couleur', '')
    poids = request.form.get('poids', '')
    taille = request.form.get('taille', '')
    photo = request.form.get('photo', '')

    tuple_insert = (type_animal_id, nom_animal, prix_achat, date_naissance, couleur, poids, taille, photo)
    sql = """ INSERT INTO animaux (type_animal_id, nom_animal, prix_achat, date_naissance, couleur, poids, taille, photo) 
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    mycursor.execute(sql, tuple_insert)
    get_db().commit()
    return redirect('/animal/show')

@app.route('/animal/edit', methods=['GET'])
def edit_animal():
    mycursor = get_db().cursor()
    id_animal = request.args.get('id_animal', None)
    sql="""SELECT id_animal, type_animal_id, nom_animal, prix_achat, date_naissance, couleur, poids, taille, photo 
    FROM animaux
    WHERE id_animal = %s"""
    mycursor.execute(sql, (id_animal,))
    animals = mycursor.fetchone()

    sql_type_animal = """SELECT id_type_animal FROM type_animal"""
    mycursor.execute(sql_type_animal)
    type_animals = mycursor.fetchall()
    return render_template('animal/edit_animal.html', animals=animals, type_animals=type_animals)

@app.route('/animal/edit', methods=['POST'])
def valid_edit_animal():
    id_animal = request.form.get('id_animal')
    mycursor = get_db().cursor()
    type_animal_id = request.form.get('type_animal_id')
    nom_animal = request.form.get('nom_animal')
    prix_achat = request.form.get('prix_achat')
    date_naissance = request.form.get('date_naissance')
    couleur = request.form.get('couleur')  # Correction ici
    poids = request.form.get('poids')
    taille = request.form.get('taille')
    photo = request.form.get('photo')

    tuple_update = (type_animal_id, nom_animal, prix_achat, date_naissance, couleur, poids, taille, photo, id_animal)

    sql = '''UPDATE animaux 
             SET type_animal_id = %s, nom_animal = %s, prix_achat = %s, date_naissance = %s, couleur = %s, poids = %s, taille = %s, photo = %s 
             WHERE id_animal = %s'''
    mycursor.execute(sql, tuple_update)
    get_db().commit()
    return redirect('/animal/show')

@app.route('/animal/delete', methods=['POST'])
def delete_animal():
    id = request.form.get('id', '')
    mycursor = get_db().cursor()
    sql = """DELETE FROM animaux WHERE id_animal = %s"""
    mycursor.execute(sql, (id,))
    get_db().commit()
    return redirect('/animal/show')

@app.route('/animal/filtre', methods=['GET'])
def filtre_animal():
    mycursor = get_db().cursor()

    mycursor.execute("SELECT * FROM type_animal")
    type_animals = mycursor.fetchall()

    mycursor.execute("SELECT * FROM animaux")
    animals = mycursor.fetchall()

    filter_word = session.get('filter_word', '')
    filter_types = session.get('filter_types', [])
    filter_price = session.get('filter_price', '')

    return render_template('animal/front_animal_filtre_show.html', type_animals=type_animals, animals=animals,
                           filter_word=filter_word, filter_types=filter_types, filter_price=filter_price)

@app.route('/animal/filtre', methods=['POST'])
def valid_filtre_animal():
    filter_word = request.form.get('filter_word', '').strip()
    filter_types = request.form.getlist('filter_types')
    filter_price = request.form.get('filter_price', '').strip()
    mycursor = get_db().cursor()

    session['filter_word'] = filter_word
    session['filter_types'] = filter_types
    session['filter_price'] = filter_price

    sql = "SELECT * FROM animaux"
    conditions = []
    params = []

    if filter_word:
        conditions.append("nom_animal LIKE %s")
        params.append(f"%{filter_word}%")

    if filter_types:
        placeholders = ', '.join(['%s'] * len(filter_types))
        conditions.append(f"type_animal_id IN ({placeholders})")
        params.extend(filter_types)

    if filter_price:
        conditions.append("prix_achat = %s")  # Prix exact
        params.append(filter_price)

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    mycursor.execute(sql, tuple(params))
    animals = mycursor.fetchall()

    mycursor.execute("SELECT * FROM type_animal")
    type_animals = mycursor.fetchall()

    return render_template('animal/front_animal_filtre_show.html', animals=animals, type_animals=type_animals)

@app.route('/animal/filtre/suppr', methods=['POST', 'GET'])
def suppr_etat():
    session.pop('filter_word', None)
    session.pop('filter_types', None)
    session.pop('filter_price', None)

    return redirect('/animal/filtre')

@app.route('/animal/etat', methods=['GET'])
def etat_animal():
    mycursor = get_db().cursor()


    sql_global = """
        SELECT 
            COUNT(*) AS total_animals,
            AVG(poids) AS average_weight,
            AVG(prix_achat) AS average_price
        FROM animaux
    """
    mycursor.execute(sql_global)
    global_stats = mycursor.fetchone()


    sql_grouped = """
        SELECT 
            nom_type AS animal_type,
            COUNT(a.id_animal) AS total_animals,
            AVG(a.poids) AS average_weight,
            AVG(a.prix_achat) AS average_price
        FROM animaux a
        JOIN type_animal t ON a.type_animal_id = t.id_type_animal
        GROUP BY t.nom_type
        ORDER BY t.nom_type
    """
    mycursor.execute(sql_grouped)
    grouped_stats = mycursor.fetchall()

    return render_template('animal/etat_animal.html', global_stats=global_stats, grouped_stats=grouped_stats)





@app.route('/type-animal/layout')
def show_layout_maraicher():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
