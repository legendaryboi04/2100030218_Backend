import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tarun@143",
    database="sql_store"
)

mycursor = mydb.cursor()


query = """
SELECT 
    location_id,
    street_address,
    city,
    state_province,
    (SELECT country_name FROM countries WHERE country_id = 'CA') AS country_name
FROM 
    locations
WHERE 
    country_id = 'CA';


"""

mycursor.execute(query)

results = mycursor.fetchall()


for row in results:
    print(row)

mydb.close()
