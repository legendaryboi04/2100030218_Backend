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
        l.location_id,
        l.street_address,
        l.city,
        l.state_province,
        c.country_name
    FROM locations l
    JOIN countries c
    ON l.country_id = c.country_id
    WHERE l.country_id = 'CA'
"""

mycursor.execute(query)

results = mycursor.fetchall()


for row in results:
    print(row)

mydb.close()
