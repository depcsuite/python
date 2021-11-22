from random import randint
def aleatorios():
    yield randint(0,100)

print(aleatorios().__next__())