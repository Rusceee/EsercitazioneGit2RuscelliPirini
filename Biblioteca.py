from Libro import Libro


class Biblioteca:
	def __init__(self):
		self.libri: list[Libro] = []

	def inserisci(self, libro: Libro) -> None:
		self.libri.append(libro)

	def ricerca(self, testo: str) -> list[Libro]:
		query = testo.casefold()
		return [
			libro
			for libro in self.libri
			if query in libro.titolo.casefold() or query in libro.autore.casefold()
		]

	def conteggio(self) -> int:
		return len(self.libri)
