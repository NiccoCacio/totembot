import sqlite3
from sqlite3 import Error
import os,pathlib
import deepfashion.demo.test_cate_attr_predictor


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def checkatt(attlist):
    for i in range(len(attlist)):
        if attlist[i] == "floral":
            attlist[i] = "floreale"
        elif attlist[i] == "graphic":
            attlist[i] = "stampato"
        elif attlist[i] == "striped":
            attlist[i] = "a righe"
        elif attlist[i] == "embroidered":
            attlist[i] = "ricamato"
        elif attlist[i] == "pleated":
            attlist[i] = "pieghetto"
        elif attlist[i] == "solid":
            attlist[i] = "tinta unita"
        elif attlist[i] == "long_sleeve":
            attlist[i] = "maniche lunghe"
        elif attlist[i] == "short_sleeve":
            attlist[i] = "maniche corte"
        elif attlist[i] == "sleeveless":
            attlist[i] = "smanicato"
        elif attlist[i] == "maxi_length":
            attlist[i] = "lungo"
        elif attlist[i] == "mini_length":
            attlist[i] = "corto"
        elif attlist[i] == "no_dress":
            attlist[i] = "non abito"
        elif attlist[i] == "crew_neckline":
            attlist[i] = "girocollo"
        elif attlist[i] == "v_neckline":
            attlist[i] = "collo a v"
        elif attlist[i] == "square_neckline":
            attlist[i] = "collo squadrato"
        elif attlist[i] == "no_neckline":
            attlist[i] = "scollato"
        elif attlist[i] == "chiffon":
            attlist[i] = "stoffa"
        elif attlist[i] == "cotton":
            attlist[i] = "cotone"
        elif attlist[i] == "leather":
            attlist[i] = "pelle"
        elif attlist[i] == "knit":
            attlist[i] = "a maglia"
        elif attlist[i] == "tight":
            attlist[i] = "attillato"
        elif attlist[i] == "loose":
            attlist[i] = "largo"
        elif attlist[i] == "conventional":
            attlist[i] = "convenzionale"


def checkcat(catlist):
    for i in range(len(catlist)):
        if catlist[i] == "Anorak":
            catlist[i] = "giacca a vento"
        elif catlist[i] == "Blouse":
            catlist[i] = "camicetta"
        elif catlist[i] == "Flannel":
            catlist[i] = "flanella"
        elif catlist[i] == "Halter":
            catlist[i] = "cavezza"
        elif catlist[i] == "Hoodie":
            catlist[i] = "felpa"
        elif catlist[i] == "Tank":
            catlist[i] = "canottiera"
        elif catlist[i] == "Chinos":
            catlist[i] = "pantaloni chinos"
        elif catlist[i] == "Skirt":
            catlist[i] = "gonna"
        elif catlist[i] == "Sweatpants":
            catlist[i] = "tuta"
        elif catlist[i] == "Dress":
            catlist[i] = "abito"
        elif catlist[i] == "Sweater":
            catlist[i] = "maglione"
        elif catlist[i] == "coat":
            catlist[i] = "cappotto"
        elif catlist[i] == "Jacket":
            catlist[i] = "giacchetto"
        elif catlist[i] == "Henley":
            catlist[i] = "serafino"
        elif catlist[i] == "Robe":
            catlist[i] = "vestito"
        elif catlist[i] == "Shirtdress":
            catlist[i] = "chemisier"
        elif catlist[i] == "Tee":
            catlist[i] = "maglietta"
        elif catlist[i] == "Culottes":
            catlist[i] = "culotte"
        elif catlist[i] == "Jersey":
            catlist[i] = "maglia"
        elif catlist[i] == "Peacot":
            catlist[i] = "caban"
        elif catlist[i] == "Turtleneck":
            catlist[i] = "dolcevita"
        elif catlist[i] == "Trunks":
            catlist[i] = "mutande"
        elif catlist[i] == "Sweatshorts":
            catlist[i] = "shorts da palestra"
        elif catlist[i] == "Jumpsuit":
            catlist[i] = "tuta intera"
        elif catlist[i] == "Cutoffs":
            catlist[i] = "shorts tagliati"
        elif catlist[i] == "Kaftan":
            catlist[i] = "caffettano"
        elif catlist[i] == "Nightdress":
            catlist[i] = "vestito da sera"



def main():
    database = r"/home/nikkaz/PycharmProjects/Tesi/database/mall.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS store (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        attributes TEXT NOT NULL,
                                        category TEXT NOT NULL,
                                        img TEXT NOT NULL,
                                        negozio TEXT NOT NULL
                                    ); """


    # aggiunta colonna negozio per simulare aiuto nella ricerca
    # create a database connection
    conn = create_connection(database)
    cursor = conn.cursor()
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")
    #a,b=deepfashion.demo.test_cate_attr_predictor.main()
    #image=convertToBinaryData("/home/nikkaz/PycharmProjects/Provafinale/Agente/database/imgs/rossarighe.jpg")
    
    #checkatt(a)
    #checkcat(b)

    # cursor.execute("""
    # DELETE FROM store
    # WHERE id='3'
    # """)
    
    cursor.execute("""SELECT * FROM store
    WHERE category="Jeans" """)
    
    # cursor.execute("""
    # INSERT INTO store (name,attributes,category,img,negozio) VALUES (?,?,?,?,?)
    # """, ("maglietta stampa naruto",a[1]+", "+ a[2]+", " +a[4]+", " + a[6],b[0], image ,"Negozio A"))

#    att_value = list
#    att_value.append("attillato")
#    att_name = "attributes"
#    cursor.execute(f"""
#    SELECT id, attributes, category, negozio, img FROM store
#    WHERE {att_name} LIKE "%{att_value[0]}%" """,)


    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()