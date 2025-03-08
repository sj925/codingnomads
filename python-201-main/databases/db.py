import sqlalchemy
import pymysql #noqa
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:Kajukenbo!994@127.0.0.1/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()  
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)  
  
query = sqlalchemy.select(actor)  
result_proxy = connection.execute(query)  
  
result_set = result_proxy.fetchall()  
pprint(result_set)
print(type(result_set))