# Taylor Niemann 4/21/23 Movies Update & Delete

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    # Inner join query
    cursor.execute("""SELECT film_name AS Name, film_director AS Director, 
        genre_name as Genre, studio_name AS "Studio Name" FROM film
        INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN 
        studio ON  film.studio_id=studio.studio_id""")

    # Get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # Iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Python imports needed
import mysql.connector
from mysql.connector import errorcode

# Database config object
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# Connection test code
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor() # Initiate cursor

    # Call the function to display films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert new film
    cursor.execute("""INSERT INTO film (film_name, film_director, film_releaseDate, film_runtime, studio_id, genre_id)
        VALUES('Star Wars', 'George Lucas', 1977, 121, 1, 2);""")
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien film to being horror genre
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_id = 2;")
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete the movie Gladiator
    cursor.execute("DELETE FROM film WHERE film_id = 1;")
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()