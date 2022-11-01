import random

def random_list():
    """Random function - free rows/columns"""
    lista_1 = []
    lista_2 = []
    lista_3 = []

    for i in range(3):
        lista_1.append(random.randint(1, 3))
        lista_2.append(random.randint(1, 3))
        lista_3.append(random.randint(1, 3))
    
    return lista_1, lista_2, lista_3