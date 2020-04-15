try:  
  mydb = mysql.connector.connect(host='localhost',
                                 user='prescott',
                                 password='embryriddle',
                                 database='klainl_db',
                                 unix_socket='/var/lib/mysql/mysql.sock')  

except mysql.connector.Error as error: 
	print(error)