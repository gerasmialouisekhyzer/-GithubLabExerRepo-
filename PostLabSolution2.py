import re
import sqlite3
import os
import datetime

DROP_SQL_PATH = "D:\Lab5\OracleDropSolmaris.sql"
CREATE_SQL_PATH = "D:\Lab5\OracleSolmaris.sql"

def load_file_robust(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"SQL file not found: {path}")
    for enc in ("utf-8", "latin-1", "cp1252"):
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read()
        except Exception:
            continue
    with open(path, "rb") as f:
        return f.read().decode("utf-8", errors="replace")

def convert_oracle_to_sqlite(sql_text):
    s = sql_text
    s = re.sub(r"DROP\s+TABLE\s+([A-Z_0-9]+)\s*;", r"DROP TABLE IF EXISTS \1;", s, flags=re.IGNORECASE)
    s = re.sub(r"DECIMAL\s*\(\s*\d+\s*,\s*\d+\s*\)", "NUMERIC", s, flags=re.IGNORECASE)
    s = re.sub(r"DECIMAL\s*\(\s*\d+\s*\)", "NUMERIC", s, flags=re.IGNORECASE)
    s = re.sub(r"CHAR\s*\(\s*\d+\s*\)", "TEXT", s, flags=re.IGNORECASE)
    s = re.sub(r"\bDATE\b", "TEXT", s, flags=re.IGNORECASE)
    return s

def safe_exec_script(conn, script_text):
    cur = conn.cursor()
    try:
        cur.executescript(script_text)
        conn.commit()
        return
    except Exception:
        statements = [s.strip() for s in script_text.split(';') if s.strip()]
        for stmt in statements:
            try:
                cur.execute(stmt)
            except Exception:
                pass
        conn.commit()

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

def fetch_rows(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    cols = [d[0] for d in cur.description] if cur.description else []
    rows = [dict(zip(cols, row)) for row in cur.fetchall()]
    return rows

def print_table(title, rows, rename_dates=None, maxrows=200):
    print("\n" + "="*80)
    print(title)
    print("-"*80)
    if not rows:
        print("(no rows)")
        return
    if rename_dates is None:
        rename_dates = []
    for r in rows:
        for d in list(r.keys()):
            if d in rename_dates or d.lower() in [x.lower() for x in rename_dates]:
                r[d] = try_parse_date(r[d])
            if d.endswith("_raw"):
                alias = d[:-4]
                if alias not in r or r[alias] is None:
                    r[alias] = try_parse_date(r[d])
    keys = list(rows[0].keys())
    col_widths = {}
    for k in keys:
        maxlen = len(k)
        for r in rows[:maxrows]:
            val = r.get(k, "")
            if isinstance(val, str):
                val = val.strip()
                r[k] = val
            maxlen = max(maxlen, len(str(val)))
        col_widths[k] = maxlen
    header = " | ".join(k.ljust(col_widths[k]) for k in keys)
    sep = "-+-".join('-'*col_widths[k] for k in keys)
    print(header)
    print(sep)
    for r in rows[:maxrows]:
        print(" | ".join(str(r.get(k, "")).ljust(col_widths[k]) for k in keys))
    if len(rows) > maxrows:
        print(f"... (showing {maxrows} of {len(rows)})")

drop_sql_raw = load_file_robust(DROP_SQL_PATH)
create_sql_raw = load_file_robust(CREATE_SQL_PATH)

drop_sql = convert_oracle_to_sqlite(drop_sql_raw)
create_sql = convert_oracle_to_sqlite(create_sql_raw)

full_script = drop_sql + "\n\n" + create_sql

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row

safe_exec_script(conn, full_script)

safe_exec_script(conn, """
DROP TABLE IF EXISTS RENTER;
CREATE TABLE RENTER (
    RENTER_NUM TEXT PRIMARY KEY,
    FIRST_NAME TEXT,
    MIDDLE_INITIAL TEXT,
    LAST_NAME TEXT,
    ADDRESS TEXT,
    CITY TEXT,
    STATE TEXT,
    POSTAL_CODE TEXT,
    PHONE TEXT,
    EMAIL TEXT
);

DROP TABLE IF EXISTS RENTAL_AGREEMENT;
CREATE TABLE RENTAL_AGREEMENT (
    AGREEMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    RENTER_NUM TEXT,
    CONDO_ID NUMERIC,
    START_DATE TEXT,
    END_DATE TEXT,
    WEEKLY_RENTAL_AMOUNT NUMERIC,
    FOREIGN KEY(RENTER_NUM) REFERENCES RENTER(RENTER_NUM),
    FOREIGN KEY(CONDO_ID) REFERENCES CONDO_UNIT(CONDO_ID)
);
""")

sample_renters = [
    ("R001", "Alice", "M", "Johnson", "12 Seabreeze Ln.", "Bowton", "FL", "31313", "555-1001", "alice.j@example.com"),
    ("R002", "Brian", "T", "O'Neil", "34 Harbor Rd.", "Glander Bay", "FL", "31044", "555-2002", "brian.oneil@example.com"),
    ("R003", "Carol", "A", "Nguyen", "77 Sunset Dr.", "Bowton", "FL", "31313", "555-3003", "carol.ng@example.com"),
]
cur = conn.cursor()
cur.executemany("INSERT OR IGNORE INTO RENTER VALUES (?,?,?,?,?,?,?,?,?,?);", sample_renters)
conn.commit()

cur.execute("SELECT CONDO_ID, CONDO_FEE FROM CONDO_UNIT LIMIT 5;")
available_condos = cur.fetchall()

rental_rows = []
if available_condos:
    condo_list = [(row[0], row[1]) for row in available_condos]
    for i, (cid, fee) in enumerate(condo_list[:3], start=1):
        renter_num = f"R00{i}"
        start_date = f"2025-0{6+i}-01"
        end_date = f"2025-0{6+i}-08"
        rental_rows.append((renter_num, cid, start_date, end_date, fee))
    cur.executemany("INSERT INTO RENTAL_AGREEMENT (RENTER_NUM, CONDO_ID, START_DATE, END_DATE, WEEKLY_RENTAL_AMOUNT) VALUES (?,?,?,?,?);", rental_rows)
    conn.commit()

q_combined = """
SELECT
    ra.AGREEMENT_ID AS agreement_id,
    r.RENTER_NUM AS renter_num,
    r.FIRST_NAME AS renter_first_name,
    r.MIDDLE_INITIAL AS renter_middle_initial,
    r.LAST_NAME AS renter_last_name,
    r.ADDRESS AS renter_address,
    r.CITY AS renter_city,
    r.STATE AS renter_state,
    r.POSTAL_CODE AS renter_postal_code,
    r.PHONE AS renter_phone,
    r.EMAIL AS renter_email,
    l.LOCATION_NUM AS location_num,
    l.LOCATION_NAME AS location_name,
    l.ADDRESS AS location_address,
    l.CITY AS location_city,
    l.STATE AS location_state,
    l.POSTAL_CODE AS location_postal_code,
    cu.CONDO_ID AS condo_id,
    cu.UNIT_NUM AS condo_unit_number,
    cu.SQR_FT AS square_footage,
    cu.BDRMS AS bedrooms,
    cu.BATHS AS bathrooms,
    cu.CONDO_FEE AS base_weekly_rate,
    ra.START_DATE AS rental_start_date,
    ra.END_DATE AS rental_end_date,
    ra.WEEKLY_RENTAL_AMOUNT AS weekly_rental_amount
FROM RENTAL_AGREEMENT ra
JOIN RENTER r ON ra.RENTER_NUM = r.RENTER_NUM
JOIN CONDO_UNIT cu ON ra.CONDO_ID = cu.CONDO_ID
LEFT JOIN LOCATION l ON cu.LOCATION_NUM = l.LOCATION_NUM
ORDER BY ra.AGREEMENT_ID;
"""

rows = fetch_rows(conn, q_combined)
print_table("Solmaris — Combined Renters, Properties, and Rental Agreements (qualities 1-3)", rows, rename_dates=["rental_start_date", "rental_end_date"])

q_renters = """
SELECT RENTER_NUM AS renter_num, FIRST_NAME, MIDDLE_INITIAL, LAST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, PHONE, EMAIL
FROM RENTER ORDER BY RENTER_NUM;
"""
q_properties = """
SELECT cu.CONDO_ID, l.LOCATION_NUM, l.LOCATION_NAME, l.ADDRESS AS location_address, l.CITY AS location_city,
       l.STATE AS location_state, l.POSTAL_CODE AS location_postal_code,
       cu.UNIT_NUM AS condo_unit_number, cu.SQR_FT AS square_footage, cu.BDRMS AS bedrooms, cu.BATHS AS bathrooms, cu.CONDO_FEE AS base_weekly_rate
FROM CONDO_UNIT cu
LEFT JOIN LOCATION l ON cu.LOCATION_NUM = l.LOCATION_NUM
ORDER BY cu.CONDO_ID;
"""
q_agreements = """
SELECT AGREEMENT_ID AS agreement_id, RENTER_NUM AS renter_num, CONDO_ID AS condo_id, START_DATE AS rental_start_date, END_DATE AS rental_end_date, WEEKLY_RENTAL_AMOUNT AS weekly_rental_amount
FROM RENTAL_AGREEMENT ORDER BY AGREEMENT_ID;
"""

print_table("1) Renters — (Number, First, Middle Initial, Last, Address, City, State, Postal Code, Phone, Email)", fetch_rows(conn, q_renters))
print_table("2) Properties — (Location Number, Location Name, Address, City, State, Postal Code, Condo Unit Number, SQ ft, Bedrooms, Bathrooms, Base Weekly ate)", fetch_rows(conn, q_properties))
print_table("3) Rental Agreements — (Renter Number, Renter Name/Address shown earlier, Dtart Date, End Date, Weekly Rental amount)", fetch_rows(conn, q_agreements), rename_dates=["rental_start_date","rental_end_date"])

conn.close()

