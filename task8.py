import sqlite3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# conn = sqlite3.connect('bank.db', check_same_thread=False)
conn = sqlite3.connect(':memory:', check_same_thread=False)

@app.on_event('startup')
def startup():
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          name varchar(256)
        )
        """
    )
    # TODO: type should be enum, deposit or savings
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          amount float,
          type varchar(256),
          user_id INTEGER,
          FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """
    )



class UserModel(BaseModel):
    name: str



@app.post('/users')
def create_user(user: UserModel):
    conn.set_trace_callback(print)
    conn.execute(
        """
        INSERT INTO users (name) VALUES (?)
        """,
        [user.name]
    )
    conn.commit()

    return True


@app.get('/users')
def list_users():
    conn.row_factory = sqlite3.Row
    users = conn.execute(
        """
        SELECT *, SUM(transactions.amount) AS deposit_amount
        FROM users 
        LEFT JOIN transactions
        ON users.id = transactions.user_id
        GROUP BY users.id
        """
    )
    users = users.fetchall()

    return users


class DepositTransaction(BaseModel):
    type: str = 'deposit'
    amount: float
    user_id: int


@app.post('/deposit/transactions')
def deposit_to_user(deposit: DepositTransaction):
    conn.set_trace_callback(print)
    conn.execute(
        """
        INSERT INTO transactions (amount, type, user_id) VALUES (?, ?, ?)
        """,
        [deposit.amount, deposit.type, deposit.user_id]
    )
    conn.commit()

    return True


@app.get('/referral')
def referral_link(uid: int):
    conn.set_trace_callback(print)
    conn.execute(
        """
        INSERT INTO transactions (amount, type, user_id) VALUES (?, ?, ?)
        """,
        [250, 'deposit', uid]
    )
    conn.commit()

    return f'250 pesos added to account ${uid}. This should not be the real implementation for this.'
