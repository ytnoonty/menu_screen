
import pymysql
import dbconfig
connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS myflaskapp"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.users (
                id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                venue_name VARCHAR(100),
                name VARCHAR(100),
                username VARCHAR(30),
                password VARCHAR(100),
                email VARCHAR(100),
                register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.users (
            venue_name,
            name,
            username,
            password,
            email)
            VALUES
            ("admin",
            "admin",
            "admin",
            "",
            "admin@email.com")"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.user_settings (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,venue_db_id INT(255),
            font_color_one VARCHAR(100),
            font_color_two VARCHAR(100),
            font_color_three VARCHAR(100),
            font_color_direction VARCHAR(100),
            shadow_font_color_one VARCHAR(100),
            shadow_font_color_two VARCHAR(100),
            shadow_font_color_three VARCHAR(100),
            shadow_font_color_direction VARCHAR(100),
            background_color_one VARCHAR(100),
            background_color_two VARCHAR(100),
            background_color_three VARCHAR(100),
            background_color_direction VARCHAR(100),
            name_font_color VARCHAR(100),
            abv_font_color VARCHAR(100),
            ibu_font_color VARCHAR(100),
            brewery_font_color VARCHAR(100),
            name_font_size INT(10),
            abv_font_size INT(10),
            ibu_font_size INT(10),
            brewery_font_size INT(10),
            screen_template INT(10))"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.user_settings (venue_db_id,
            font_color_one,
            font_color_two,
            font_color_three,
            font_color_direction,
            shadow_font_color_one,
            shadow_font_color_two,
            shadow_font_color_three,
            shadow_font_color_direction,
            background_color_one,
            background_color_two,
            background_color_three,
            background_color_direction,
            name_font_color,
            abv_font_color,
            ibu_font_color,
            brewery_font_color,
            name_font_size,
            abv_font_size,
            ibu_font_size,
            brewery_font_size,
            screen_template)
            VALUES
            ("1",
            "#000000",
            "#000000",
            "#000000",
            "to bottom",
            "#000000",
            "#000000",
            "#000000",
            "to bottom",
            "#000000",
            "#000000",
            "#000000",
            "to bottom",
            "#000000",
            "#000000",
            "#000000",
            "#000000",
            "1",
            "1",
            "1",
            "1",
            "1")"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.list_history (
                id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                venue_db_id INT(255),
                name VARCHAR(100),
                style VARCHAR(100),
                abv VARCHAR(10),
                ibu VARCHAR(10),
                brewery VARCHAR(100),
                location VARCHAR(255),
                website VARCHAR(255),
                description TEXT,
                draft_bottle_selection VARCHAR(50),
                create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (venue_db_id, name, style, abv, ibu, brewery, location, website, description, draft_bottle_selection) VALUES ("1", "name", "style", "0.0", "0", "brewery", "location", "website", "description", "draft/bottle")"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.list_current (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                venue_db_id INT(255),
                id_history INT(100),
                id_on_next INT(100),
                id_dropdown INT(100)
                )"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.font_size_options (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                venue_db_id INT(255),
                font_sizes VARCHAR(100)
                )"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.font_size_options (venue_db_id, font_sizes) VALUES ("1", "1.0em")"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS myflaskapp.templates (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                templates VARCHAR(100),
                venue_db_id INT(255),
                active_template VARCHAR(100)
                )"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.templates (venue_db_id, templates, active_template) VALUES ("1", "1 Column", "disabled")"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.templates (venue_db_id, templates, active_template) VALUES ("1", "2 Columns, Names", "disabled")"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.templates (venue_db_id, templates, active_template) VALUES ("1", "2 Columns, Artist Time", "disabled")"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.templates (venue_db_id, templates, active_template) VALUES ("1", "2 Columns, Names, ABV", "disabled")"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.templates (venue_db_id, templates, active_template) VALUES ("1", "2 Columns, Names, ABV, IBU", "disabled")"""
        cursor.execute(sql)


        for i in range(1, 2):
            sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", %s)"""
            cursor.execute(sql, (i))
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "2")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "3")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "4")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "5")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "6")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "7")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "8")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "9")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "10")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "11")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "12")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "13")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "14")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "15")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "16")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "17")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "18")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "19")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "20")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "21")"""
        # cursor.execute(sql)
        # sql = """INSERT INTO myflaskapp.list_current (venue_db_id, id_history, id_on_next, id_dropdown) VALUES ("1", "1", "1", "22")"""
        # cursor.execute(sql)
        connection.commit()

finally:
        connection.close()
