import psycopg2
from config import config
def insertsentencia(sentencia):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database = "componentsuf6",
            user = "estudiante",
            password = "3stud14nt3"
        )
    except psycopg2.Error as e:
        print(f"Error conectando a la base de datos: {e}")
    cur = conn.cursor()
    cur.execute(sentencia)
    conn.commit()

    conn.close()



def Selectsentencia(sentencia):
    try:
        conn = psycopg2.connect (
            host="localhost",
            database = "componentsuf6",
            user = "estudiante",
            password = "3stud14nt3"
        )
        cur = conn.cursor()
        cur.execute(sentencia)
        conn.commit()
        prova = cur.fetchall()
    except psycopg2.Error as e:
        print(f"Error conectando a la base de datos: {e}")
    finally:
        conn.close()
    return prova