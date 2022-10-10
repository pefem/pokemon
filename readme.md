## installation
* all libraries required to run this file are contained in the "requirements.txt" file

## folder structure
"app.py" file
* contains the logic for the route rquired to make the api call

"requirements.txt" file
* all libraries installed, mainly from installing flask

"db.pokemon" file
* database file containing persisted pokemon data. Can use "db browser" to open.

"scraper.py" file
* contains logic for extracting data from "PokeAPI"

"templates/index.html" file
* contains markup for displaying data from database.

"test_scraper.py" file
* contains logic for unit tests


## How to run program
to run program simply run start the server by running "flask run" in the terminal and enter the url "http://127.0.0.1:5000/pokemon" in a web browser.


## Brief Explainer
# Design and implementation
Design and implementation for this crawler api was primarly centered around being simple for the purposes of this test.

A Scraper class was defined in "scraper.py", to estabilish a connection with the defined PokeAPI endpoints and extract the data needed. Once this was accomplished, a "db.py" module was set up to handle database connection logic as well as logic to persist data retrieved from PokeAPI endpoints to a database.

The above processes are further called within the "app.py" file which is set up to handle the route required to access the data from the database. If data exists in the database the scraper is not called.

# Scaling and testing
in terms of allowing for scaling not much was done given the scope. However, areas which i would consider improving the scale would be in having a more flexible approcah when getting back data from the "PokeAPI". Currently, the amount of pokemon data that can be recieved from the PokeAPI is set at 10. Although this can be easily adjusted within the the code, an approach i would consider going forward would be to have this value passed in as an argument. Furthermore, another area i would consider scaling is in updating the records if changes are made, althougth this would be most essential if all the data was required consistently.

With regards to testing, focus was around the response gotten from the "PokeAPI" as well as the number of values returned, hence two test functions were written.

