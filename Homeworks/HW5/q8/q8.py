# question 8
sql_q8 = '''select * from employees limit 10;'''
import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="********", 
                        database="postgres"
                       )
cur = conn.cursor()
cur.execute(sql_q8)
print("Unformatted Results:")
print(cur.description)
for row in cur:
    print (row)
conn.commit()
cur.close()
conn.close()
