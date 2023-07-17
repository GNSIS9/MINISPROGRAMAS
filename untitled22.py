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
abjetivos=["Bulliciosa", "Juvenil", "Pueril", "Vigil", "Varonil", "Mujeril", "Jabril", "Estudiantil", 
           "Zacandil", "Textil", "Brujeril", "Pajuos", "Sabrositos"]

def consulta():
    consulta = "SELECT ciudad from centrodetrabajo"
   
    print("consulta:", consulta)
   
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)

    df.ciudad = df.ciudad.map(lambda x: x + " " + random.choice(abjetivos))
    print("df.head(21)=",df.head(21))

    df.to_excel("df.xlsx")
consulta()