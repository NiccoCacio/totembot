from typing import Text, Any, List, Dict

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.types import DomainDict
import sqlite3, random
from sqlite3 import Error
database = r"/home/nikkaz/PycharmProjects/Tesi/database/mall.db"

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = DbQueryingMethods.create_connection(db_file=database)
        attr_value = tracker.get_slot("attributes")
       # print(attr_value[0])
        cat_value = tracker.get_slot("category")
       # print(cat_value)
        att_name = "attributes"
        cat_name = "category"
        query1 = DbQueryingMethods.select_capo(conn=conn, att_name=att_name, att_value=attr_value,
                                               cat_name=cat_name, cat_value=cat_value)
        #print(query1, "query pre remove")
        prima = query1[random.randint(0, len(query1)-1)]
        lista1 = list(prima)
        idq1 = DbQueryingMethods.get(rows=lista1, i=0)
        #print(idq1, "questo è l'id")
        query1.remove(prima)
        #print(query1, "post remove")
        #print(type(query1))
        seconda = query1[random.randint(0, len(query1)-1)]
        lista2 = list(seconda)
        idq2 = DbQueryingMethods.get(rows=lista2, i=0)
        query1.remove(seconda)
        terza = query1[random.randint(0, len(query1)-1)]
        lista3 = list(terza)
        idq3 = DbQueryingMethods.get(rows=lista3, i=0)
        # print(idq)
        cat1 = DbQueryingMethods.get(rows=lista1, i=2)
        cat2 = DbQueryingMethods.get(rows=lista2, i=2)
        # print(cat)
        att1 = DbQueryingMethods.get(rows=lista1, i=1)
        att2 = DbQueryingMethods.get(rows=lista2, i=1)
        # print(att)
        img1 = DbQueryingMethods.get(rows=lista1, i=3) + ".png"
        img2 = DbQueryingMethods.get(rows=lista2, i=3) + ".png"
        img3 = DbQueryingMethods.get(rows=lista3, i=3) + ".png"
        # print(img1, img2)

        dispatcher.utter_message(text="Che ne pensi?")

        dispatcher.utter_message(
            #text="Categorie: " + cat1 + "\n Attributi: " + att1,
            image=str(img1)
        )

        dispatcher.utter_message(
            #text="Categorie: " + cat2 + "\n Attributi: " + att2,
            image=str(img2)
        )

        dispatcher.utter_message(
            # text="Categorie: " + cat3 + "\n Attributi: " + att3,
            image=str(img3)
        )


        return [SlotSet("query1", idq1), SlotSet("query2", idq2), SlotSet("query3", idq3)]


class ActionModify(Action):

    def name(self) -> Text:
        return "action_modify"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = DbQueryingMethods.create_connection(db_file=database)
        q1 = tracker.get_slot("query1")
        q2 = tracker.get_slot("query2")
        q3 = tracker.get_slot("query3")
        qmod = tracker.get_slot("querymod")
        spot = tracker.get_slot("spot")
        attr_value = tracker.get_slot("attributes")
        cat_value = tracker.get_slot("category")
        att_name = "attributes"
        cat_name = "category"
        if spot is None:
            query_mod = DbQueryingMethods.select_mod(conn=conn, att_name=att_name, att_value=attr_value,
                                                     cat_name=cat_name, cat_value=cat_value, id1=q1, id2=q2, id3=q3)
        elif spot == "primo" and qmod is None:
            attributo = list(DbQueryingMethods.retrieve(conn=conn, idm=q1)[0])
            attr_value = attributo[0]
            query_mod = DbQueryingMethods.select_mod(conn=conn, att_name=att_name, att_value=attr_value,
                                                     cat_name=cat_name,
                                                     cat_value=cat_value, id1=q1, id2=q2, id3=q3)
        elif spot == "primo" and qmod is not None:
            attributo = list(DbQueryingMethods.retrieve(conn=conn, idm=qmod[-3])[0])
            attr_value = attributo[0]
            query_mod = DbQueryingMethods.select_mod(conn=conn, att_name=att_name, att_value=attr_value,
                                                         cat_name=cat_name,
                                                         cat_value=cat_value, id1=q1, id2=q2, id3=q3)
        elif spot == "secondo" and qmod is None:
            attributo = list(DbQueryingMethods.retrieve(conn=conn, idm=q2)[0])
            attr_value = attributo[0]
            query_mod = DbQueryingMethods.select_mod(conn=conn, att_name=att_name, att_value=attr_value,
                                 cat_name=cat_name,
                                 cat_value=cat_value, id1=q1, id2=q2, id3=q3)

        elif spot == "secondo" and qmod is not None:
            attributo = list(DbQueryingMethods.retrieve(conn=conn, idm=qmod[-2])[0])
            attr_value = attributo[0]
            query_mod = DbQueryingMethods.select_mod(conn=conn, att_name=att_name, att_value=attr_value,
                                                     cat_name=cat_name,
                                                     cat_value=cat_value, id1=q1, id2=q2, id3=q3)

        elif spot == "secondo" and qmod is None:
            attributo = list(DbQueryingMethods.retrieve(conn=conn, idm=q3)[0])
            attr_value = attributo[0]
            query_mod = DbQueryingMethods.select_mod(conn=conn, att_name=att_name, att_value=attr_value,
                                                     cat_name=cat_name,
                                                     cat_value=cat_value, id1=q1, id2=q2, id3=q3)

        elif spot == "terzo" and qmod is not None:
            attributo = list(DbQueryingMethods.retrieve(conn=conn, idm=qmod[-1])[0])
            attr_value = attributo[0]
            query_mod = DbQueryingMethods.select_mod(conn=conn, att_name=att_name, att_value=attr_value,
                                                     cat_name=cat_name,
                                                     cat_value=cat_value, id1=q1, id2=q2, id3=q3)

        mod1 = query_mod[random.randint(0, len(query_mod) - 1)]
        listamod1 = list(mod1)
        idq1 = DbQueryingMethods.get(rows=listamod1, i=0)
        query_mod.remove(mod1)
        mod2 = query_mod[random.randint(0, len(query_mod) - 1)]
        listamod2 = list(mod2)
        idq2 = DbQueryingMethods.get(rows=listamod2, i=0)
        query_mod.remove(mod2)
        mod3 = query_mod[random.randint(0, len(query_mod) - 1)]
        listamod3 = list(mod3)
        idq3 = DbQueryingMethods.get(rows=listamod3, i=0)

        if qmod is None:
            qmod = [None]*3
            qmod[0] = idq1
            qmod[1] = idq2
            qmod[2] = idq3
        else:
            qmod.append(idq1)
            qmod.append(idq2)
            qmod.append(idq3)

        cat = DbQueryingMethods.get(rows=listamod1, i=2)
        att = DbQueryingMethods.get(rows=listamod1, i=1)
        img1 = DbQueryingMethods.get(rows=listamod1, i=3) + ".png"
        img2 = DbQueryingMethods.get(rows=listamod2, i=3) + ".png"
        img3 = DbQueryingMethods.get(rows=listamod3, i=3) + ".png"

        dispatcher.utter_message(text="Riproviamo")

        dispatcher.utter_message(
            image=img1
        )
        #dispatcher.utter_message(text="Categorie: " + cat + "\n Attributi: " + att)

        dispatcher.utter_message(
            image=img2
        )
        # dispatcher.utter_message(text="Categorie: " + cat + "\n Attributi: " + att)

        dispatcher.utter_message(
            image=img3
        )

        return [SlotSet("querymod", qmod), SlotSet("mod", True)]




class ActionAccetta(Action):
    def name(self) -> Text:
        return "action_accetta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = DbQueryingMethods.create_connection(db_file=database)
        mod = tracker.get_slot("mod")
        query1 = tracker.get_slot("query1")
        query2 = tracker.get_slot("query2")
        query3 = tracker.get_slot("query3")
        querymod = tracker.get_slot("querymod")
        spot = tracker.get_slot("spot")

        if mod is False:
            if spot == "primo":
                queryresult = query1
                ida = DbQueryingMethods.select_acpt(conn=conn, ida=queryresult)
                acpt = list(ida[0])
                negozio = DbQueryingMethods.get(rows=acpt, i=0)
                img = DbQueryingMethods.get(rows=acpt, i=1) + ".png"
                dispatcher.utter_message(
                    text="Hai scelto il primo capo, puoi trovarlo al " + negozio,
                    image=img
                )
            elif spot == "secondo":
                queryresult = query2
                ida = DbQueryingMethods.select_acpt(conn=conn, ida=queryresult)
                acpt = list(ida[0])
                negozio = DbQueryingMethods.get(rows=acpt, i=0)
                img = DbQueryingMethods.get(rows=acpt, i=1) + ".png"
                dispatcher.utter_message(
                    text="Hai scelto il secondo capo, puoi trovarlo al " + negozio,
                    image=img
                )
            elif spot == "terzo":
                queryresult = query3
                ida = DbQueryingMethods.select_acpt(conn=conn, ida=queryresult)
                acpt = list(ida[0])
                negozio = DbQueryingMethods.get(rows=acpt, i=0)
                img = DbQueryingMethods.get(rows=acpt, i=1) + ".png"
                dispatcher.utter_message(
                    text="Hai scelto il terzo capo, puoi trovarlo al " + negozio,
                    image=img
                )
        elif mod is True:
            if spot == "primo":
                print(mod)
                queryresult = querymod[-3]
                ida = DbQueryingMethods.select_acpt(conn=conn, ida=queryresult)
                acpt = list(ida[0])
                negozio = DbQueryingMethods.get(rows=acpt, i=0)
                img = DbQueryingMethods.get(rows=acpt, i=1) + ".png"
                dispatcher.utter_message(
                    text="Perfetto, puoi trovare il primo capo al " + negozio,
                    image=img
                )
            elif spot == "secondo":
                queryresult = querymod[-2]
                ida = DbQueryingMethods.select_acpt(conn=conn, ida=queryresult)
                acpt = list(ida[0])
                negozio = DbQueryingMethods.get(rows=acpt, i=0)
                img = DbQueryingMethods.get(rows=acpt, i=1) + ".png"
                dispatcher.utter_message(
                    text="Perfetto, puoi trovare il secondo capo al " + negozio,
                    image=img
                )
            elif spot == "terzo":
                queryresult = querymod[-1]
                ida = DbQueryingMethods.select_acpt(conn=conn, ida=queryresult)
                acpt = list(ida[0])
                negozio = DbQueryingMethods.get(rows=acpt, i=0)
                img = DbQueryingMethods.get(rows=acpt, i=1) + ".png"
                dispatcher.utter_message(
                    text="Perfetto, puoi trovare il terzo capo al " + negozio,
                    image=img
                )
        #print(queryresult)

        return [AllSlotsReset()]

class ActionRifiuta(Action):
    def name(self) -> Text:
        return "action_rifiuta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Mi dispiace non averti aiutato")
        return [AllSlotsReset()]

class DbQueryingMethods:

    def create_connection(db_file):
        """
        create a database connection to the SQLite database
        specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def select_capo(conn, att_name, att_value, cat_name, cat_value):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()


        if att_value is not None and cat_value is not None:
            cur.execute(f'''SELECT id, attributes, category, img FROM store
                    WHERE {cat_name} LIKE "%{cat_value}%" 
                    AND {att_name} LIKE "%{att_value[0]}%" ''')
        elif att_value is not None and cat_value is None:
            cur.execute(f'''SELECT id, attributes, category, img FROM store
                    WHERE {att_name} LIKE "%{att_value[0]}%" ''')
        elif att_value is None and cat_value is not None:
            cur.execute(f'''SELECT id, attributes, category, img FROM store
                    WHERE {cat_name} LIKE "%{cat_value}%" ''')

        # return an array
        rows = cur.fetchall()
        #print(rows)

        return rows

    def select_mod(conn, att_name, att_value, cat_name, cat_value, id1, id2, id3):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        #print("modifica",cat_value,att_value,id1,id2,)

        if att_value is not None and cat_value is not None:
            cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {cat_name} LIKE "%{cat_value}%" 
                        AND {att_name} LIKE "%{att_value[0]}%"
                        AND id NOT IN ({id1},{id2},{id3})  ''')

        elif att_value is not None and cat_value is None:
            cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {att_name} LIKE "%{att_value[0]}%"
                        AND id NOT IN ({id1},{id2},{id3}) ''')

        elif att_value is None and cat_value is not None:
            cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {cat_name} LIKE "%{cat_value}%"
                        AND id NOT IN ({id1},{id2},{id3}) ''')
        # return an array
        rows = cur.fetchall()

        return rows

    def select_mod_spot(conn, att_name, att_value, cat_name, cat_value, id1, id2, id3, idmod):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        #print("modifica",cat_value,att_value,id1,id2,)
        if idmod is not None:
            if att_value is not None and cat_value is not None:
                cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {cat_name} LIKE "%{cat_value}%" 
                        AND {att_name} LIKE "%{att_value[0]}%"
                        AND id NOT IN ({id1},{id2},{id3},{idmod})  ''')

            elif att_value is not None and cat_value is None:
                cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {att_name} LIKE "%{att_value[0]}%"
                        AND id NOT IN ({id1},{id2},{id3},{idmod}) ''')

            elif att_value is None and cat_value is not None:
                cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {cat_name} LIKE "%{cat_value}%"
                        AND id NOT IN ({id1},{id2},{id3},{idmod}) ''')
        else:
            if att_value is not None and cat_value is not None:
                cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {cat_name} LIKE "%{cat_value}%" 
                        AND {att_name} LIKE "%{att_value[0]}%"
                        AND id NOT IN ({id1},{id2},{id3})  ''')

            elif att_value is not None and cat_value is None:
                cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {att_name} LIKE "%{att_value[0]}%"
                        AND id NOT IN ({id1},{id2},{id3}) ''')

            elif att_value is None and cat_value is not None:
                cur.execute(f'''SELECT id, attributes, category, img FROM store
                        WHERE {cat_name} LIKE "%{cat_value}%"
                        AND id NOT IN ({id1},{id2},{id3}) ''')
            # return an array
            rows = cur.fetchall()

        return rows

    def select_acpt(conn, ida):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()

        cur.execute(f'''SELECT negozio, img FROM store
              WHERE id = "{ida}" ''')

        rows = cur.fetchall()
        return rows


    def retrieve(conn, idm):
        cur = conn.cursor()
        cur.execute(f'''SELECT attributes, category FROM store
                    WHERE id ="{idm}" ''')

    def get(rows, i):
        if len(list(rows)) < 1:
            return "Non ci sono risorse per la tua richiesta"
        else:
            return rows[i]
