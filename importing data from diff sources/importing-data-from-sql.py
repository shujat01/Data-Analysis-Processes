import mysql.connector
import pandas as pd

conn = mysql.connector.connect(host="localhost",user="root",password="",database="supermarket")

invoices = pd.read_sql_query('SELECT * FROM invoices',conn)
order_lead = pd.read_sql_query('SELECT * FROM order_leads',conn)
sales_sql = pd.read_sql_query('SELECT * FROM sales_sql',conn)


with pd.ExcelWriter('supermarketnewdash.xlsx') as writer:
    invoices.to_excel(writer,sheet_name="invoices")
    order_lead.to_excel(writer,sheet_name="order_lead")
    sales_sql.to_excel(writer,sheet_name="sales_sql")
