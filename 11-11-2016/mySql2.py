import pymysql.cursors
import time

def mysql_func(rID= "", volts= "", current= "", watts= "", status= ""):
    #print "Starting mysql module "
    #print "mysql function radio ID is  " + rID


    #print "Connecting to db"
    #print ""
    connection = pymysql.connect(host='localhost',
    user='root',
    password='root',
    db='ICBP',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    time.sleep(100/1000)

    print "Storing into table = " + rID
    print ""

    
    with connection.cursor() as cursor:
        sql = "INSERT INTO " +rID+ "(ID, Volts, Current, Watts, Status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (rID, volts, current, watts, status))
        connection.commit()
        cursor.close()

        time.sleep(1/2)


    
