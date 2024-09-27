import os
from dotenv import load_dotenv


def cargar_entorno(entorno):
    if entorno == "dev":
        load_dotenv(".env.dev")
    elif entorno == "pro":
        load_dotenv(".env.pro")
    else:
        raise ValueError("Entorno no válido. Debes elegir 'dev' o 'pro'.")


entorno = input("Selecciona el entorno ('dev' para desarrollo, 'pro' para producción): ").strip()


cargar_entorno(entorno)


USER_NAME = os.getenv("USER_NAME")
API_KEY = os.getenv("API_KEY")
EMAIL = os.getenv("EMAIL")
DATABASE_URL = os.getenv("DATABASE_URL")


print(f"Entorno seleccionado: {entorno}")
print(f"USER_NAME: {USER_NAME}")
print(f"API_KEY: {API_KEY}")
print(f"EMAIL: {EMAIL}")
print(f"DATABASE_URL: {DATABASE_URL}")
