import sqlite3
import random


class DatabaseHandler:


    def __init__(self, name):

        dbName = name + ".db"
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS TB1(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        question TEXT,
        answer1 TEXT,
        answer2 TEXT,
        score1 INTEGER,
        score2 INTEGER
        )
        """)
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS TB2(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        question TEXT,
        answer1 TEXT,
        answer2 TEXT
        )
        """)
        
        self.conn.commit()


    def addQuestion(self, q, a1, a2, n):

        if n == 1:
          
            data = {"question" : q, "answer1" : a1, "answer2" : a2, "score1" : 0, "score2" : 0}
            self.cursor.execute("INSERT INTO TB1(question, answer1, answer2, score1, score2) VALUES(:question, :answer1, :answer2, :score1, :score2)", data)
            id = self.cursor.lastrowid

            self.conn.commit()

            return id

        elif n == 2:
  
            data = {"question" : q, "answer1" : a1, "answer2" : a2}
            self.cursor.execute("INSERT INTO TB2(question, answer1, answer2) VALUES(:question, :answer1, :answer2)", data)
            id = self.cursor.lastrowid

            self.conn.commit()

            return id

        else:

            print("Unknown table.")


    def deleteQuestion(self, id, n):

        tbName = "TB" + str(n)
        self.cursor.execute("DELETE FROM {} WHERE id=?".format(tbName), (id,))
            
        self.conn.commit()


    def addScore(self, id, n):
        print('ok')
        if n == 1:
            print('ok1')
            self.cursor.execute("SELECT score1 FROM TB1 WHERE id=?", (id,))
            s = int(self.cursor.fetchone()[0]) + 1
            
            self.cursor.execute("""UPDATE TB1 SET score1 = ? WHERE id = ?""", (s, id,))


        elif n == 2:
            print('ok2')
            self.cursor.execute("""SELECT score2 FROM TB1 WHERE id=?""", (id,))
            s = int(self.cursor.fetchone()[0])+1   

            self.cursor.execute("""UPDATE TB1 SET score2 = ? WHERE id = ?""", (s, id,))

        self.conn.commit()


    def searchQuestion(self, id, n):

        tbName = "TB" + str(n)

        if n == 1:
            
            self.cursor.execute("SELECT question, answer1, answer2, score1, score2 FROM {} WHERE id=?".format(tbName), (id,))
            q = self.cursor.fetchone()

            return q

        elif n == 2:

            self.cursor.execute("SELECT question, answer1, answer2 FROM {} WHERE id=?".format(tbName), (id,))
            q = self.cursor.fetchone()

            return q


    def searchScore(self, id):

        self.cursor.execute("""SELECT score1, score2 FROM TB1 WHERE id=?""", (id,))
        score = self.cursor.fetchone()

        return score


    def getIDs(self, n):

        tbName = "TB" + str(n)
        self.cursor.execute("SELECT id FROM {} ORDER BY id ASC".format(tbName))
        l = list(self.cursor.fetchall())
        ids = list()

        for i in l:
                
            ids.append(i[0])

        return ids


    def randomID(self, l):

        return random.choice(l)
