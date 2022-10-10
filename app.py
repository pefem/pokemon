from flask import Flask, request
from flask import render_template
import db
from scraper import Scraper


app = Flask(__name__)
scraper = Scraper()

@app.route('/pokemon', methods=["GET"])
def get_pokemon():
    conn = db.db_connection()

    if request.method == "GET":
        def run_query(conn):
            cursor = conn.execute("SELECT * FROM tb_pokemon")
            pokemon_data = [
                dict(name=row[0], ability=row[1], experience=row[2], height=row[3])
                for row in cursor.fetchall()
            ]
            return pokemon_data

        pokemons = run_query(conn)

        if pokemons:
            return render_template("index.html", pokemons=pokemons)
        else:
            response = scraper.get_response()
            data = scraper.get_data(response)
            pokemon_list = scraper.extract_data(data)
            db.add_to_db(pokemon_list, conn)
            pokemons = run_query(conn)

            return render_template("index.html", pokemons=pokemons)


if __name__ == "__main__":
    app.run(debug=True)

