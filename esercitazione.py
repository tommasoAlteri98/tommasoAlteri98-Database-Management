# Crea un gestionale scolastico, l'utente
# puÃ² visualizzare il nome degli studenti presenti o inserire nuovi studenti

import mysql.connector

def connessionedatabase(host, user, password, database):
    try:
        mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
        )
    except:
        mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password
        )
        mycursor = mydb.cursor()
        query = "create database " + database
        mycursor.execute(query)
        query1 = "create or replace table " + database +".Studenti(id int auto_increment primary key, nome varchar(100), cognome varchar(100), VotoItaliano int, VotoMatematica int, VotoInglese int)"
        mycursor.execute(query1)
        mydb = connessionedatabase("localhost", "root", "", "GestionaleScuola2")
    return mydb
mydb = connessionedatabase("localhost", "root", "", "GestionaleScuola2")
mycursor = mydb.cursor()
    
#query1 = "create or replace table Studenti(id int auto_increment primary key, nome varchar(100), cognome varchar(100), VotoItaliano int, VotoMatematica int, VotoInglese int)"
#mycursor.execute(query1)

def VisualizzaStudenti():
    query3 ="select * from Studenti"
    mycursor.execute(query3)
    myresult = mycursor.fetchall()
    if len(myresult)>=1:
        for riga in myresult:
            print(f"ID: {riga[0]} - Nome {riga[1]} - Cognome {riga[2]} - Voto Italiano {riga[3]} - Voto Matematica {riga[4]} - Voto Inglese {riga[5]}")
    else:
        print("Database vuoto")

def aggiungiAlunno(nome, cognome, VotoItaliano = 6, VotoMatematica = 6, VotoInglese = 6):
    query = "insert into Studenti(nome, cognome, VotoItaliano, VotoMatematica, VotoInglese) values(%s, %s, %s, %s, %s)"
    valnome =(nome, cognome, VotoItaliano, VotoMatematica, VotoInglese)
    mycursor.execute(query, valnome)
    mydb.commit()
    print(mycursor.rowcount, "righe inserite!")
 
def rimuoviStudente(val):
    query = "delete from studenti where id = %s"
    mycursor.execute(query,(val,))
    mydb.commit()
    print(mycursor.rowcount, "righe eliminate!")
    
def modificaStudente(val,scelta):
    if scelta=="1":
        nuovo=input("Nuovo Nome: ")
        query = "update studenti set nome = %s where id = %s"
        mycursor.execute(query,(nuovo,val))
        mydb.commit()
        print(mycursor.rowcount, "righe modificate!")
    elif scelta=="2":
        nuovo=input("Nuovo Cognome: ")
        query = "update studenti set cognome = %s where id = %s"
        mycursor.execute(query,(nuovo,val))
        mydb.commit()
        print(mycursor.rowcount, "righe modificate!")
    else:
        print("Valore non valido")
        
def modificaVoto(val,scelta):
    if scelta=="1":
        nuovo=input("Nuovo Voto Italiano: ")
        query = "update studenti set VotoItaliano = %s where id = %s"
        mycursor.execute(query,(nuovo,val))
        mydb.commit()
        print(mycursor.rowcount, "righe modificate!")
    elif scelta=="2":
        nuovo=input("Nuovo Voto Matematica: ")
        query = "update studenti set VotoMatematica = %s where id = %s"
        mycursor.execute(query,(nuovo,val))
        mydb.commit()
        print(mycursor.rowcount, "righe modificate!")
    elif scelta=="3":
        nuovo=input("Nuovo Voto Inglese: ")
        query = "update studenti set VotoInglese = %s where id = %s"
        mycursor.execute(query,(nuovo,val))
        mydb.commit()
        print(mycursor.rowcount, "righe modificate!")
    else:
        print("Valore non valido")
        
def eliminaVoto(val,scelta):
    if scelta=="1":
        query = "update studenti set VotoItaliano = %s where id = %s"
        mycursor.execute(query,(None,val))
        mydb.commit()
        print(mycursor.rowcount, "righe modificate!")
    elif scelta=="2":
        query = "update studenti set VotoMatematica = %s where id = %s"
        mycursor.execute(query,(None,val))
        mydb.commit()
        print(mycursor.rowcount, "righe modificate!")
    elif scelta=="3":
        query = "update studenti set VotoInglese = %s where id = %s"
        mycursor.execute(query,(None,val))
        mydb.commit()
        print(mycursor.rowcount, "righe modificate!")
    else:
        print("Valore non valido")
         
def menu():
    condizione = True
    while condizione:

        print("\n------| MENU |------")
        print("1. Aggiungi alunno")
        print("2. Visualizza alunni")
        print("3. Rimuovi alunno")
        print("4. Modifica alunno")
        print("5. Modifica voto")
        print("6. Elimina voto")
        print("7. Stop")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            sceltaNome = input("inserisci il nome dell'alunno: ")
            sceltaCognome = input("inserisci il cognome dell'alunno: ")
            sceltaV1 = int(input("inserisci il Voto di Italiano: "))
            sceltaV2 = int(input("inserisci il Voto di Matematica: "))
            sceltaV3 = int(input("inserisci il Voto di Inglese: "))
            aggiungiAlunno(sceltaNome, sceltaCognome, sceltaV1, sceltaV2, sceltaV3)   
        elif scelta == "2":
            VisualizzaStudenti()
        elif scelta == "3":
            id = int(input("ID dell'alunno da eliminare: "))
            rimuoviStudente(id)
        elif scelta == "4":
            id = int(input("ID dell'alunno da modificare: "))
            sceltaColonna = input("1.Modifica Nome; 2.Modifica Cognome: ")
            modificaStudente(id,sceltaColonna)
        elif scelta == "5":
            id = int(input("ID dell'alunno da modificare: "))
            sceltaColonna = input("1.Modifica Voto Italiano; 2.Modifica Voto Matematica: , 3.Modifica Voto Inglese")
            modificaVoto(id,sceltaColonna)
        elif scelta == "6":
            id = int(input("ID dell'alunno da modificare: "))
            sceltaColonna = input("1.Elimina Voto Italiano; 2.Elimina Voto Matematica: , 3.Elimina Voto Inglese")
            eliminaVoto(id,sceltaColonna)
        elif scelta=="7":
            condizione = False
            print("Programma terminato.")
        else:
            print("Opzione non valida! Inserisci un numero tra 1 e 3.")
            
menu()
