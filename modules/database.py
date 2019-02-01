
import sqlite3

class SQLite:
    """ Provides methods for tasks related with SQLite databases. """

    def connector(self, dbname):
        return sqlite3.connect(dbname)
