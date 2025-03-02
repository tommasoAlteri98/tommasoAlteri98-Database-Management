class Hotel:
    def __init__(self, db):
        self.db = db
    
    def aggiungi(self, nome, descrizione):
        self.db.cursor.execute("INSERT INTO hotel (nome, descrizione) VALUES (?, ?)", (nome, descrizione))
        self.db.conn.commit()
        print("Risorsa aggiunta con successo.")
        

class PrenotazioneHotel:
    def __init__(self, db):
        self.db = db
    
    def effettuaPrenotazione(self, utente_id, hotel_id, data_prenotazione, stato = "attiva"):
        self.db.cursor.execute("INSERT INTO prenotazioni (utente_id, hotel_id, data_prenotazione, stato) VALUES (?, ?, ?, ?)", (utente_id, hotel_id, data_prenotazione, stato))
        self.db.conn.commit()
        print("Prenotazione della camera di hotel effettuata con successo.")
    
    def visualizzaPrenotazione(self):
        self.db.cursor.execute("SELECT * FROM prenotazioni")
        prenotazioni = self.db.cursor.fetchall()
        for prenotazione in prenotazioni:
            print(prenotazione)
    
    def cancellaPrenotazione(self, prenotazione_id):
        self.db.cursor.execute("UPDATE prenotazioni SET stato = 'cancellata' WHERE id = ?", (prenotazione_id,))
        self.db.conn.commit()
        print("Prenotazione cancellata con successo.")
    
    def reportPrenotazioni(self):
        self.db.cursor.execute("SELECT stato, COUNT(*) FROM prenotazioni GROUP BY stato")
        report = self.db.cursor.fetchall()
        for row in report:
            print(row)

