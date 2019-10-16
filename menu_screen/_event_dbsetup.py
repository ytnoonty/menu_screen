
import pymysql
import dbconfig
connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS myflaskapp"
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.events (
                id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                venue_db_id INT(255),
                name VARCHAR(100),
                artist VARCHAR(100),
                date_of_event DATE,
                time_of_event TIME,
                endtime_of_event TIME,
                location VARCHAR(255)
                )"""
        cursor.execute(sql)

        connection.commit()

finally:
        connection.close()

## NEED TO ADD TO DB
## ALTER TABLE events ADD COLUMN endtime_of_event TIME;
