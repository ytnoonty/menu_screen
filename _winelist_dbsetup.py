import pymysql
import dbconfig
connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS myflaskapp"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.wines (
                id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                venue_db_id INT(255),
                name VARCHAR(100),
                location VARCHAR(100),
                description TEXT,
                glass VARCHAR(10),
                bottle VARCHAR(10),
                varietal VARCHAR(100),
                foodPairings TEXT
                )"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.winelist_current (
                id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                venue_db_id INT(255),
                id_wine INT(100),
                id_dropdown INT(100)
                )"""
        cursor.execute(sql)

        for i in range(1, 2):
            sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", %s, %s)"""
            cursor.execute(sql, (i, i))
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "2", "2")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "3", "3")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "4", "4")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "5", "5")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "6", "6")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "7", "7")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "8", "8")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "9", "9")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "10", "10")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "11", "11")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "12", "12")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "13", "13")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "14", "14")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "15", "15")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "16", "16")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "17", "17")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "18", "18")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "19", "19")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "20", "20")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "21", "21")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "22", "22")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "23", "23")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "24", "24")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "25", "25")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "26", "26")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "27", "27")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.winelist_current (venue_db_id, id_wine, id_dropdown) VALUES ("1", "28", "28")"""
        # cursor.execute(sql)


        connection.commit()

finally:
        connection.close()
