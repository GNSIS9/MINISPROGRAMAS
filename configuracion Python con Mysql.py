import pymysql #1. pip3 install --upgrade pip 2. pip3 install pymysql

import pandas as pd
import numpy as np
import collections
import itertools
from datetime import date, datetime, timedelta


################ MySQL ###################
database = 'mibd'
username = 'root'
password = '1234'
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password, database=database)


def consulta():
    consulta = " SELECT * from empleado "
    print("consulta:", consulta)
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)
    print("df.info()=",df.info())
    print("df.describe()=",df.describe())
    print("df.head(10)=",df.head(10))
    print("df.tail(10)=",df.tail(10))
    print("df.sample(20)=",df.sample(20))
    
consulta() 