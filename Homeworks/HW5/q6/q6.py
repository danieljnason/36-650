# question 6
sql_q6 = '''create table employees(id serial, fname varchar(10), lname varchar(10));'''
import psycopg2
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="******", 
                        database="postgres"
                       )
cur = conn.cursor()
cur.execute(sql_q6)
cur.execute("select *  from employees;")
print("Unformatted Results:")
print (cur.description)
conn.commit()
cur.close()
conn.close()
