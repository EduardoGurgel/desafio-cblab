import json
import psycopg2

DB_HOST = "db"
DB_NAME = "restaurant"
DB_USER = "user"
DB_PASSWORD = "password"
JSON_PATH = "/app/data/ERP.json"

def load_data():
    with open(JSON_PATH, 'r') as file:
        data = json.load(file)

    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
    )
    cur = conn.cursor()

    # Inserir dados de guestChecks
    for guestCheck in data["guestChecks"]:
        cur.execute("""
            INSERT INTO guestChecks (guestCheckId, chkNum, opnBusDt, clsdBusDt, clsdFlag, gstCnt, subTtl, chkTtl, payTtl)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            guestCheck["guestCheckId"], guestCheck["chkNum"],
            guestCheck["opnBusDt"], guestCheck["clsdBusDt"],
            guestCheck["clsdFlag"], guestCheck["gstCnt"],
            guestCheck["subTtl"], guestCheck["chkTtl"],
            guestCheck["payTtl"]
        ))

    conn.commit()
    cur.close()
    conn.close()
    print("Dados carregados com sucesso!")

if __name__ == "__main__":
    load_data()
