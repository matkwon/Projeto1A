import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database():
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(name+".db")
        command = f"CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);"
        self.conn.execute(command)

    def add(self, note):
        command = f"INSERT INTO {self.name} (title, content) VALUES ('{note.title}','{note.content}');"
        self.conn.execute(command)
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute(f"SELECT id, title, content FROM {self.name};")
        lista = []
        for linha in cursor:
            lista.append(Note(linha[0],linha[1],linha[2]))
        return lista

    def update(self, entry):
        command = f"UPDATE {self.name} SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id};"
        self.conn.execute(command)
        self.conn.commit()

    def delete(self, note_id):
        command = f"DELETE FROM {self.name} WHERE id = {note_id};"
        self.conn.execute(command)
        self.conn.commit()