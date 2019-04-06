import os
import psycopg2


passwd = os.environ.get('DB_passwd')
try:
    connection = psycopg2.connect(
        database="postgres",
        user="team9",
        password= passwd,
        host="product-analytics-db-instance.cupv3jj2ht0z.us-west-2.rds.amazonaws.com",
        port='5432'
    )
    SQLCursor=connection.cursor()
    SQLCursor.execute(open('create_user_table.sql','r').read())
    
except (Exception, psycopg2.Error) as error : print ("Error while executing script", error)

finally:
#closing database connection.
    if(connection):
        SQLCursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

