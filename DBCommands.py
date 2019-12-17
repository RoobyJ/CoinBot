import sqlite3
import os


class DataManager:
    def __init__(self):
        self.path = f"{os.getcwd()}\coinbotdata\ServersUserData.db"
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()

    def close(self):
        self.c.close()
        self.conn.close()

    def create_table(self, guild_id):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute(f"CREATE TABLE IF NOT EXISTS '{guild_id}'(user_id INTEGER UNIQUE, coins INTEGER DEFAULT 0)")
        conn.commit()
        self.close()

    def data_entry(self, guild_id, user_id):
        self.c.execute(f"INSERT INTO '{guild_id}'(user_id) VALUES({user_id})")
        self.conn.commit()
        self.close()

    def get_data(self, guild_id, arg, user_id=None):
        self.c = self.conn.cursor()
        if user_id is None:
            self.c.execute(f"SELECT {arg} FROM '{guild_id}'")
        else:
            self.c.execute(f"SELECT {arg} FROM '{guild_id}' WHERE user_id={user_id}")
        data = self.c.fetchall()
        data_to_return = []
        for x in data:
            data_to_return.append(x[-1])
        self.conn.commit()
        self.close()
        return data

    def update_data(self):
        pass
    '''this needs to be done'''


def create_db():
    conn = sqlite3.connect('ServersUserData.db')
    c = conn.cursor()
    c.close()
    conn.close()
