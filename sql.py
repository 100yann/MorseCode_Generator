import sqlalchemy
from sqlalchemy import create_engine, text
import random

engine = create_engine("sqlite+pysqlite:///morse.db", echo=True)

class DB:
    def __init__(self):
        # Creates a local db, unless one with the same name already exists 
        try:
            with engine.connect() as conn:
                conn.execute(text("CREATE TABLE morse_db (Original_Input, Morse_Code)"))
                conn.commit()
        except sqlalchemy.exc.OperationalError:
            pass
    

    def all_data(self):
        # shows all data in the db for the selected columns)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT Original_Input, Morse_Code FROM morse_db"))
            for row in result:
                print(f"Original Input: {row.Original_Input}  Morse Code: {row.Morse_Code}")


    def log_input(self, string, morse):
        #store the original input and morse code into the temporary db
        with engine.connect() as conn:
            conn.execute(text("INSERT INTO morse_db (Original_Input, Morse_Code) VALUES (:Original_Input, :Morse_Code)"),
                        [{"Original_Input": string, "Morse_Code": morse}]
            )
            conn.commit()
        self.all_data()

    
    def delete_data(self):
        with engine.connect() as conn:
            conn.execute(text("DELETE FROM morse_db "))
            conn.commit()
        self.all_data()



            