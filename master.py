from Libro import Libro
from Biblioteca import Biblioteca

def esegui_test():
    print("=== ESECUZIONE TEST ===")
    
    # 1. Creazione di un libro
    l1 = Libro("George Orwell", "1984", 1949, "Mondadori", 328)
    print(f"Libro creato: {l1.titolo} di {l1.autore}")
    
    # 2. Test del metodo readingTime
    tempo = l1.readingTime(pagine_ora=40)
    print(f"Tempo stimato di lettura (40 pag/ora): {tempo:.2f} ore")
    
    # 3. Test della Biblioteca (inserimento e conteggio)
    bib = Biblioteca()
    bib.inserisci(l1)
    bib.inserisci(Libro("J.R.R. Tolkien", "Il Signore degli Anelli", 1954, "Bompiani", 1200))
    bib.inserisci(Libro("George Orwell", "La fattoria degli animali", 1945, "Mondadori", 140))
    
    print(f"Totale libri presenti in biblioteca: {bib.conteggio()}")
    
    # 4. Test della ricerca
    risultati = bib.ricerca("Orwell")
    print(f"Libri trovati per 'Orwell': {len(risultati)}")
    for libro in risultati:
        print(f" - {libro.titolo}")
    print("=== TEST COMPLETATI CON SUCCESSO ===\n")

if __name__ == "__main__":
    esegui_test()


def menu_interfaccia():
    bib = Biblioteca()
    
    # Popolamento iniziale di prova
    bib.inserisci(Libro("Alessandro Manzoni", "I Promessi Sposi", 1827, "Recla", 720))
    bib.inserisci(Libro("Italo Calvino", "Il barone rampante", 1957, "Einaudi", 280))

    while True:
        print("\n--- GESTIONE BIBLIOTECA ---")
        print("1. Aggiungi nuovo libro")
        print("2. Cerca un libro (per titolo o autore)")
        print("3. Mostra numero totale libri")
        print("4. Calcola tempo di lettura di un libro di prova")
        print("5. Esegui test automatici")
        print("0. Esci")
        
        scelta = input("Seleziona un'opzione: ").strip()
        
        if scelta == "1":
            autore = input("Autore: ")
            titolo = input("Titolo: ")
            anno = int(input("Anno di pubblicazione: "))
            editore = input("Editore: ")
            pagine = int(input("Numero di pagine: "))
            
            nuovo_libro = Libro(autore, titolo, anno, editore, pagine)
            bib.inserisci(nuovo_libro)
            print("✓ Libro inserito con successo!")
            
        elif scelta == "2":
            query = input("Inserisci il testo da cercare: ")
            trovati = bib.ricerca(query)
            if trovati:
                print(f"\nTrovati {len(trovati)} riscontro/i:")
                for l in trovati:
                    print(f"- '{l.titolo}' di {l.autore} ({l.anno}, {l.editore}) - {l.numero_pagine} pag.")
            else:
                print("Nessun libro trovato.")
                
        elif scelta == "3":
            print(f"\nIn biblioteca ci sono attualmente {bib.conteggio()} libri.")
            
        elif scelta == "4":
            pagine = int(input("Inserisci numero pagine del libro: "))
            vel = int(input("Velocità di lettura (pagine/ora, di default 30): ") or "30")
            temp_libro = Libro("N/D", "Prova", 2024, "N/D", pagine)
            print(f"Tempo di lettura stimato: {temp_libro.readingTime(vel):.2f} ore")
            
        elif scelta == "5":
            esegui_test()
            
        elif scelta == "0":
            print("Chiusura del programma. Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    menu_interfaccia()