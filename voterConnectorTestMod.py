import mysql.connector

try:  
  mydb = mysql.connector.connect(host='localhost',
                                 user='prescott',
                                 password='embryriddle',
                                 database='klainl_db',
                                 unix_socket='/var/lib/mysql/mysql.sock')  

except mysql.connector.Error as error: 
	print(error)

cursor = mydb.cursor()
    
cursor.execute('SELECT candidate_name FROM candidates')  
for candidate_name in cursor:  
  print("{}".format(candidate_name))

    
cursor.execute('SELECT voter_id FROM voter')  
for voter_id in cursor:  
  print("{}".format(voter_id))

if mydb.is_connected():    
  cursor.close()   
  mydb.close()