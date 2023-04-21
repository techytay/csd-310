# Taylor Niemann 4/21/23 Movies: Table Queries

# Python imports needed
import mysql.connector
from mysql.connector import errorcode

# Database config object
config = {
    "user": "root",
    "password": "Jmp^AndRun815",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# Connection test code
try:
    db = mysql.connector.connect(**config)

    # Query from tables in movies database
    cursor = db.cursor()

    # Query all fields from studio table
    cursor.execute("SELECT studio_id, studio_name FROM studio;") # selecting fields from studio table
    print("-- DISPLAYING Studio RECORDS --")
    studios = cursor.fetchall()
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    # Query all fields from genre table
    cursor.execute("SELECT genre_id, genre_name FROM genre;")
    print("-- DISPLAYING Genre RECORDS --")
    genres = cursor.fetchall()
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    # Query movie names for movies that have runtime less than 2 hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
    print("-- DISPLAYING Short Film RECORDS --")
    short_films = cursor.fetchall()
    for short_film in short_films:
        print("Film Name: {}\nRuntime: {}\n".format(short_film[0], short_film[1]))

    # Query film names and directors ordered by director
    cursor.execute("SELECT film_name, film_director From film ORDER BY film_director;")
    print("-- DISPLAYING Director RECORDS in Order--")
    directors = cursor.fetchall()
    for director in directors:
        print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()