import psycopg2

conn = psycopg2.connect(database="syntaxboard",
                        user='syntaxboard',
                        password='syntaxboard',
                        host='127.0.0.1',
                        port='5432')

cursor = conn.cursor()
sql = "set search_path='loans';"
cursor.execute(sql)

# --------------------------------

# sql = "select * from customer;"
sql = "select * from loan_rules;"
cursor.execute(sql)

for i in cursor.fetchall():
    print(i)

# --------------------------------
# Execute this only once. Which we did.
# Otherwise it will insert values again and again in to the loan_rules table in the database.
with open('loan_rules.csv', 'r') as f:
    next(f)  # Skip the header row
    cursor.copy_from(f, 'loan_rules', sep=',')
# --------------------------------

conn.commit()
conn.close()
