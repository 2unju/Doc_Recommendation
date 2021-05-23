import psycopg2.extras
from Doc_Recommendation.DocRec.DocList.recommend import Top10_Docs
import pandas as pd

sign_info = "host='localhost' dbname ='docdb' user='postgres' password='tlqejr1010'"
sign = psycopg2.connect(sign_info, cursor_factory=psycopg2.extras.DictCursor)
cursor = sign.cursor()

sql = "SELECT * FROM doclist"
cursor.execute(sql)
doc = cursor.fetchall()
cursor.close()
sign.close()

df = pd.DataFrame(doc)

Top10 = Top10_Docs(df, 2)
print(Top10)
