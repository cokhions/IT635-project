import psycopg2

conn = psycopg2.connect("postgresql://fashion_item:testing@localhost/fashion_item")
cur = conn.cursor()

print("Please enter an order ID")
order_id = int(input())
cur.execute("""
    SELECT customers.name, parts.name, orders.quantity
    FROM orders, customers, parts
    WHERE orders.customer_id=customers.customer_id
        AND orders.part_id=parts.part_id
        AND order_id=%s
""", (order_id,));
for row in cur:
    item_name = row[1]
    quantity = row[2]
    print(f"{item_name} x {quantity}")
print(f"Deliver to: {row[0]}")

cur.close()
conn.close()