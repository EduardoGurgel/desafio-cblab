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


    for guestCheck in data["guestChecks"]:
        cur.execute("""
            INSERT INTO guestChecks (guestCheckId, chkNum, opnBusDt, clsdBusDt, clsdFlag, gstCnt, subTtl, chkTtl, payTtl)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (guestCheckId) DO NOTHING
        """, (
            guestCheck["guestCheckId"], guestCheck["chkNum"],
            guestCheck["opnBusDt"], guestCheck["clsdBusDt"],
            guestCheck["clsdFlag"], guestCheck["gstCnt"],
            guestCheck["subTtl"], guestCheck["chkTtl"],
            guestCheck["payTtl"]
        ))


        if "taxes" in guestCheck:
            for tax in guestCheck["taxes"]:
                cur.execute("""
                    INSERT INTO taxes (guestCheckId, taxNum, taxRate, taxCollTtl)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT DO NOTHING
                """, (
                    guestCheck["guestCheckId"], tax["taxNum"],
                    tax["taxRate"], tax["taxCollTtl"]
                ))


        if "detailLines" in guestCheck:
            for detailLine in guestCheck["detailLines"]:
                menu_item = detailLine.get("menuItem")
                if menu_item:

                    cur.execute("""
                        INSERT INTO menuItem (menuItemId, inclTax, activeTaxes)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (menuItemId) DO NOTHING
                    """, (
                        menu_item["miNum"], menu_item["inclTax"], menu_item["activeTaxes"]
                    ))


                cur.execute("""
                    INSERT INTO detailLines (guestCheckId, lineNum, menuItemId)
                    VALUES (%s, %s, %s)
                    ON CONFLICT DO NOTHING
                """, (
                    guestCheck["guestCheckId"], detailLine["lineNum"],
                    menu_item["miNum"] if menu_item else None
                ))


    conn.commit()
    cur.close()
    conn.close()
    print("Dados carregados com sucesso!")

if __name__ == "__main__":
    load_data()
