import mysql.connector

try:
  mydb = mysql.connector.connect(
    host='prclab1.pr.erau.edu',
    user='prescott',
    password='embryriddle',
    database='vanhilsm_db',
    unix_socket='/var/lib/mysql/mysql.sock'
  )

except mysql.connector.Error as error:
  print(error)


