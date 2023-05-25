# Component amb PostgreSQL
## Requisits
~~~ 
sudo apt install postgresql 
~~~
## Importació
~~~
from backend import Selectsentencia, executarsentencia
~~~
## Manera d'ús
Primer de tot ficar les teves dades a les dos funcions del component
~~~
 conn = psycopg2.connect(
            host="localhost",
            database = "Nom de la base de dades",
            user = "Usuari",
            password = "Contrasenya"
        )
~~~
Una vegada tens els parametres ben ficats sol tenim que ficar la consulta dins de executar sentencia i ell s'encarregara de insertar-ho, aquí tens un exemple:
( El nom de la funsió per insertar és insertsentencia )
~~~
 consulta = (f"insert into account (name, password) VALUES  ('" + user + "','" + password + "');")
        insertsentencia(str(consulta))
~~~
I per recuperar les dades sera de la mateixa manera però amb una consulta d'una busqueda i amb el nom de la funcio Selectsentencia. Aquí tenim un exemple:
~~~
consulta2 = "SELECT id from account where name ='"+ user +"' AND password ='" + password +"';"
        cerca = Selectsentencia(consulta2)
~~~
