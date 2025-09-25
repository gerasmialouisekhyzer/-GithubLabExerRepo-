DROP_SQL_PATH = "D:\Lab5\OracleDropColonial.sql"
CREATE_SQL_PATH = "D:\Lab5\OracleColonial.sql"

import sqlite3, os, datetime
from pprint import pprint

use_pandas = True
try:
    import pandas as pd
except Exception:
    use_pandas = False

def try_parse_date(s):
    if s is None:
        return None
    s = str(s).strip()
    for fmt in ("%m-%d-%Y","%m/%d/%Y","%m-%d-%y","%m/%d/%y","%Y-%m-%d"):
        try:
            dt = datetime.datetime.strptime(s, fmt)
            return dt.strftime("%Y-%m-%d")
        except Exception:
            continue
    return s

def safe_exec_script(conn, script_text):
    cur = conn.cursor()
    try:
        cur.executescript(script_text)
    except Exception:
        statements = [s.strip() for s in script_text.split(';') if s.strip()]
        for stmt in statements:
            try:
                cur.execute(stmt)
            except Exception:
                pass
    conn.commit()

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

if not os.path.exists(DROP_SQL_PATH) or not os.path.exists(CREATE_SQL_PATH):
    raise FileNotFoundError

with open(DROP_SQL_PATH, "r", encoding="utf-8") as f:
    drop_sql = f.read()
with open(CREATE_SQL_PATH, "r", encoding="utf-8") as f:
    create_sql = f.read()

safe_exec_script(conn, drop_sql)
safe_exec_script(conn, create_sql)

q1 = """
SELECT CUSTOMER_NUM AS customer_num,
       LAST_NAME, FIRST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, PHONE,
       'N/A' AS date_of_birth
FROM CUSTOMER
ORDER BY CUSTOMER_NUM;
"""

q2 = """
SELECT t.TRIP_ID AS class_number,
       TRIM(t.TRIP_NAME) AS class_description,
       t.MAX_GRP_SIZE AS max_people,
       ROUND(AVG(r.TRIP_PRICE), 2) AS average_class_fee
FROM TRIP t
LEFT JOIN RESERVATION r ON t.TRIP_ID = r.TRIP_ID
GROUP BY t.TRIP_ID, t.TRIP_NAME, t.MAX_GRP_SIZE
ORDER BY t.TRIP_ID;
"""

q3 = """
SELECT c.CUSTOMER_NUM AS customer_num,
       c.LAST_NAME, c.FIRST_NAME,
       r.TRIP_ID AS class_number,
       TRIM(t.TRIP_NAME) AS class_description,
       r.TRIP_DATE AS class_date_raw
FROM CUSTOMER c
JOIN RESERVATION r ON c.CUSTOMER_NUM = r.CUSTOMER_NUM
JOIN TRIP t ON r.TRIP_ID = t.TRIP_ID
ORDER BY c.CUSTOMER_NUM, r.TRIP_DATE;
"""

q4 = """
SELECT r.TRIP_DATE AS class_date_raw,
       r.TRIP_ID AS class_number,
       TRIM(t.TRIP_NAME) AS class_description,
       c.CUSTOMER_NUM AS customer_num,
       c.LAST_NAME, c.FIRST_NAME
FROM RESERVATION r
JOIN TRIP t ON r.TRIP_ID = t.TRIP_ID
JOIN CUSTOMER c ON r.CUSTOMER_NUM = c.CUSTOMER_NUM
ORDER BY r.TRIP_ID, r.TRIP_DATE, c.LAST_NAME, c.FIRST_NAME;
"""

def fetch_rows(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = [dict(r) for r in cur.fetchall()]
    return rows

def normalize_and_print(title, rows, rename_dates=None, maxrows=200):
    print("\n" + "="*80)
    print(title)
    print("-"*80)
    if not rows:
        print("(no rows)")
        return
    if rename_dates is None:
        rename_dates = []
    for r in rows:
        for d in rename_dates:
            if d in r and r[d] is not None:
                r[d] = try_parse_date(r[d])
            if d.endswith("_raw") and d in r:
                r[d[:-4]] = r.pop(d)
    if use_pandas:
        df = pd.DataFrame(rows)
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(lambda v: v.strip() if isinstance(v, str) else v)
        if len(df) > maxrows:
            print(df.head(maxrows).to_string(index=False))
            print(f"... (showing {maxrows} of {len(df)})")
        else:
            print(df.to_string(index=False))
    else:
        keys = list(rows[0].keys())
        col_widths = {k: max(len(k), max((len(str(r.get(k,''))) for r in rows))) for k in keys}
        header = " | ".join(k.ljust(col_widths[k]) for k in keys)
        sep = "-+-".join('-'*col_widths[k] for k in keys)
        print(header)
        print(sep)
        for r in rows[:maxrows]:
            print(" | ".join(str(r.get(k,'')).ljust(col_widths[k]) for k in keys))
        if len(rows) > maxrows:
            print(f"... (showing {maxrows} of {len(rows)})")

rows1 = fetch_rows(conn, q1)
rows2 = fetch_rows(conn, q2)
rows3 = fetch_rows(conn, q3)
rows4 = fetch_rows(conn, q4)

normalize_and_print("1) Participants (Customer List) — Columns: Number, Last, First, Address, City, State, Postal Code, Phone, Date of Birth", rows1)
normalize_and_print("2) Adventure Classes (Trip List) — Columns: Class number, Class Description, Max People, Average Class Fee", rows2)
normalize_and_print("3) Participant Enrollments: Customer → Class (Includes Class Date)", rows3, rename_dates=["Class Date Raw"])
normalize_and_print("4) Classes with Participants: Class Date, Class number, Class Description, Participant Info", rows4, rename_dates=["Class Date Raw"], maxrows=500)

conn.close()
