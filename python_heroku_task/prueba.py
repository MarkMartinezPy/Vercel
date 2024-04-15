from os import environ
from pathlib import Path
from dotenv import load_dotenv
load_dotenv ()

diccionario = {
    "programa":"5",
    "lección": environ.get("llave_secreta")
}
print(diccionario["lección"])