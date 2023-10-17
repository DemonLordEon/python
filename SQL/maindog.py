import os 
import sqlite3
from sqlite3 import Error

#mainin()-----------------------------
def main():
    while True:
            add_dog_to_table()
            list_dog_table()
        
            svar = input("\n Vill du mata in en hund till j/n: ")
            if (svar != "j"):
                break
        
def add_dog_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    hundnamn = input("mata in hundnamn: ")
    hundras = input("Mata in hundras: ")
    
    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = f""" INSERT into dogs
                               (namn, ras)
                                VALUES
                               ('{hundnamn}', '{hundras}') """
                               
    cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("\nLa till till Hund till DB\n")
    cursor.close()
    sqliteConnection.close()

def list_dog_table():
    
    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()
    sqlite_select_query = """SELECT * from dogs ORDER by namn"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        print(f"\tID: {row[0]}, \tNAMN: {row[1]}, \tRAS: {row[2]}")
        
    cursor.close()
    sqliteConnection.close()
    print("the SQLite Connection is closed")
    
main()