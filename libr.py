import psycopg2 as pg

try:
    conn = pg.connect(
        host='localhost',
        database='Pharmacy',
        port=5432,
        user='postgres',
        password='admin'
    )

    cursor = conn.cursor()
    print("Connection established.")

except Exception as err:
    print("Something went wrong.")
    print(err)


def fetch_data():
    cursor.execute('''SELECT * FROM medicine''')
    data = cursor.fetchall()
    return data
details = fetch_data()
for row in details:
    print(row)
