class Libro:
	def __init__(self, autore: str, titolo: str, anno: int, editore: str, numero_pagine: int):
		self.autore = autore
		self.titolo = titolo
		self.anno = anno
		self.editore = editore
		self.numero_pagine = numero_pagine

	def readingTime(self, pagine_ora: int = 30) -> float:
		if pagine_ora <= 0:
			raise ValueError("La velocita di lettura deve essere maggiore di zero.")
		return self.numero_pagine / pagine_ora
