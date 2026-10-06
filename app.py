import os # en haut du fichier (import inutilisé)
DB_PASSWORD = "admin123" # mot de passe en dur

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Division par zero")
    return a / b


def is_even(n):
    return n % 2 == 0

def read_config(path):
 f = open(path) # fichier jamais fermé
 try:
 return f.read()
 except: # "except" trop large
 pass

 def classify(x):
 if x > 10:
 return "grand"
 return "petit" # fonctions non couvertes par les tests
