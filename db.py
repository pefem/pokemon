import sqlite3


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("db.pokemon")
    except sqlite3.error as e:
        print(e)
    
    return conn

def add_to_db(pokemon_list, conn):

    command = "INSERT INTO tb_pokemon VALUES(?, ?, ?, ?)"

    for pokemon in pokemon_list:
        conn.execute(command, tuple(pokemon.values()))
        print("data added to database")
        
        conn.commit()



