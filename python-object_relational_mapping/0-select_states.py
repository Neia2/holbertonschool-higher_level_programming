import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123passwd",
    database="hbtn_0e_0_usa"  # Specify the database
)

# Create a cursor to execute SQL queries
cursor = mydb.cursor()

# SQL query to create the table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
"""
cursor.execute(create_table_query)

list_states_query = "SELECT * FROM states;"
cursor.execute(list_states_query)

states = cursor.fetchall()
for state in states:
    print(state)

cursor.close()
mydb.close()
