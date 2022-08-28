# question 7
sql_q7 = '''insert into employees(select generate_series(1,500) as id, substr(MD5(random()::text), 0, 3) AS fname, substr(MD5(random()::text), 0, 3) AS lname);'''
import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="*********", 
                        database="postgres"
                       )
cur = conn.cursor()
cur.execute(sql_q7)
cur.execute("select * from employees limit 5;")
print("Unformatted Results:")
print (cur.description)

print("\n\n Formatted Results:")
for row in cur:
    print (row)
conn.commit()
cur.close()
conn.close()
