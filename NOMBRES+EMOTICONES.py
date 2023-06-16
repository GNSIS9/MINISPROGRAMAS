import pymysql
import pandas as pd
import numpy as np
import collections
import itertools
import random
from datetime import date, datetime, timedelta

################ MySQL ###################
database = "mibd";
username = "root";
password = "1234";
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password,
database=database)
cursor = db.cursor()# prepare a cursor object using cursor() method
lista=["😡","🤬","🤡","🥳","🧐","🧓","👿","🤔","😆","💩","😤","😛","😲","🤯","🤭","🤔","🥰","😘","🤪","😜","😟","😳","😴"]

def consulta():
    consulta = "SELECT nombre, puesto from empleado"
   
    print("consulta:", consulta)
   
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)

    df.nombre = df.nombre.map(lambda x: x+"lista"+random.choice(lista))
    print("df.head(21)=",df.head(21))

    df.to_excel("df.xlsx")
consulta()