def czy_sa_anagramami(lista_slow):
  
    if len(lista_slow) < 2:
        raise ValueError("Podaj co najmniej dwa słowa do porównania.")
    
    wzor = sorted(lista_slow[0])
    
    for slowo in lista_slow[1:]:
        if sorted(slowo) != wzor:
            return False
    
    return True


lista_slow = ["test", "test", "test"]
print(czy_sa_anagramami(lista_slow))  # Powinno zwrócić True