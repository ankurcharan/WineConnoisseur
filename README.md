# Wine Connoisseur

----
## Database
Create sql database using the the data dump given.
Create a table with all the fields in the data, remove the headers in data and load the data in sql using the 'LOAD DATA INFILE' command.

Create a user 'django' on localhost identified by 'password'

## Django Server

Run 
    
    $ python manage.py inspectdb

and paste the output in earth/models.py

Run the server using command

    $ python manage.py runserver

and visit [https://localhost:8000](http://localhost:8000)

## Assignment

On the homepage it shows the data of all wines.
You can filter on it by country, province, region as given in the search bar at the top.
Choose any one you like and write the search text.

Choose wines from the navigation bar to choose from all the distinct wines.
You can filter on them based on different types of grapes used.

Choose any wine to check its details.
It shows all the places and details where that wine is used.
You can sort here according to the price (ascending/descending) of the wine used. 
