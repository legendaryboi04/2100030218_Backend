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
SELECT l.location_id,
       l.street_address,
       l.city,
       l.state_province,
       (CASE WHEN l.country_id = 'CA' THEN (SELECT country_name FROM countries WHERE country_id = 'CA') ELSE NULL END) AS country_name
FROM locations l;

"""

mycursor.execute(query)

results = mycursor.fetchall()


for row in results:
    print(row)

mydb.close()
