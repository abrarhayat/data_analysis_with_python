from dbmodule import connect

#create a connection object
connection = connect('databasename', 'user_name', 'password')

#create a cursor object
cursor = connection.cursor()

#run queries
cursor.execute('select * from mytable')

#get all results from execution
results = cursor.fetchall()

#free up resources
cursor.close()
connection.close()