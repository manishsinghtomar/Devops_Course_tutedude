import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password='mysecretpassword',
                        port="5432")

cur = conn.connect()

# Create table

 cur.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name varchar(255), email varchar(255), password varchar(255))")
 print("Table created successfully")

# Insert data

cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", ("John242345123", "john@snow.com", "johnpassword"))

 conn.commit()

# Get data

cur.execute("SELECT FROM users")

rows cur.fetchall()

for row in rows:

  print(row)

# Close connection

conn.close()