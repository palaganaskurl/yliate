import sqlite3


customer_data = [
    {
        'id': 1,
        'first_name': 'Jason',
        'last_name': 'Smith',
        'gender': 'male',
        'date_of_birth': '1982-05-28',
        'country': 'USA'
    },
    {
        'id': 2,
        'first_name': 'Max',
        'last_name': 'Mustermann',
        'gender': 'male',
        'date_of_birth': '1980-07-18',
        'country': 'Germany'
    },
    {
        'id': 3,
        'first_name': 'Will',
        'last_name': 'Myer',
        'gender': 'male',
        'date_of_birth': '1981-03-30',
        'country': 'England'
    },
    {
        'id': 4,
        'first_name': 'Christin',
        'last_name': 'Dawn',
        'gender': 'female',
        'date_of_birth': '1978-08-02',
        'country': 'USA'
    },
    {
        'id': 5,
        'first_name': 'Angela',
        'last_name': 'Gutierez',
        'gender': 'female',
        'date_of_birth': '1986-01-16',
        'country': 'Spain'
    },
    {
        'id': 6,
        'first_name': 'Peter',
        'last_name': 'Jackson',
        'gender': 'male',
        'date_of_birth': '1958-12-05',
        'country': 'USA'
    }
]
orders = [
    {
        'id': 1,
        'order_nr': 2783292423,
        'sum': 100.85,
        'fk_customer': 2
    },
    {
        'id': 2,
        'order_nr': 4784232411,
        'sum': 77.34,
        'fk_customer': 3
    },
    {
        'id': 3,
        'order_nr': 3783292423,
        'sum': 30.99,
        'fk_customer': 5
    },
    {
        'id': 4,
        'order_nr': 9368315313,
        'sum': 33.55,
        'fk_customer': 2
    }
]
order_items = [
    {
        'id': 1,
        'sku': 'ABCDEF',
        'fk_order': 1,
    },
    {
        'id': 2,
        'sku': 'ABCDEF',
        'fk_order': 1,
    },
    {
        'id': 3,
        'sku': 'OHSDLF',
        'fk_order': 1,
    },
    {
        'id': 4,
        'sku': '1737234',
        'fk_order': 2,
    },
    {
        'id': 5,
        'sku': 'KLSHA',
        'fk_order': 3,
    },
    {
        'id': 6,
        'sku': 'OHSDLF',
        'fk_order': 3,
    },
]


conn = sqlite3.connect(':memory:')
conn.execute(
    """
    CREATE TABLE customers (
      id int PRIMARY KEY,
      first_name varchar(256),
      last_name varchar(256),
      gender varchar(256),
      date_of_birth varchar(256),
      country varchar(256)
    )
    """
)
conn.execute(
    """
    CREATE TABLE orders (
      id int PRIMARY KEY,
      order_nr int,
      sum float,
      fk_customer int,
      FOREIGN KEY(fk_customer) REFERENCES customers(id)
    )
    """
)
conn.execute(
    """
    CREATE TABLE order_items (
      id int PRIMARY KEY,
      sku varchar(256),
      fk_order int,
      FOREIGN KEY(fk_order) REFERENCES orders(id)
    )
    """
)
conn.executemany(
    'INSERT INTO customers (id, first_name, last_name, gender, date_of_birth, country) '
    'VALUES (?, ?, ?, ?, ?, ?)',
    [list(customer.values()) for customer in customer_data]
)
conn.executemany(
    'INSERT INTO orders (id, order_nr, sum, fk_customer) '
    'VALUES (?, ?, ?, ?)',
    [list(order.values()) for order in orders]
)
conn.executemany(
    'INSERT INTO order_items (id, sku, fk_order) '
    'VALUES (?, ?, ?)',
    [list(order_item.values()) for order_item in order_items]
)
conn.commit()


all_females = conn.execute('SELECT * FROM customers WHERE gender == ?', ['female'])
all_females = all_females.fetchall()

print('All Females', all_females)

orders_by_names = conn.execute(
    """
    SELECT customers.first_name, customers.last_name, COUNT(*) 
    FROM customers 
    INNER JOIN orders 
    ON customers.id = orders.fk_customer
    GROUP BY customers.id
    """,
)
orders_by_names = orders_by_names.fetchall()

print('Customer Names with Number of Orders', orders_by_names)

customers_with_money_spent = conn.execute(
    """
    SELECT customers.first_name, customers.last_name, SUM(orders.sum)
    FROM customers 
    INNER JOIN orders 
    ON customers.id = orders.fk_customer
    GROUP BY customers.id
    """,
)
customers_with_money_spent = customers_with_money_spent.fetchall()

print('Customers with Money Spent', customers_with_money_spent)

order_nrs_with_at_least_2_item = conn.execute(
    """
    SELECT orders.order_nr, COUNT(*) as order_item_count
    FROM orders 
    INNER JOIN order_items 
    ON orders.id = order_items.fk_order
    GROUP BY orders.id
    HAVING order_item_count >= 2
    """,
)
order_nrs_with_at_least_2_item = order_nrs_with_at_least_2_item.fetchall()

print('Order NRs with At Least 2 Items', order_nrs_with_at_least_2_item)

conn.close()
