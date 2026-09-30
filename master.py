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