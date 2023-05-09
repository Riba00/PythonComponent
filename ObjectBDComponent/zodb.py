import ZODB
import ZODB.FileStorage
import transaction
def insert(fitxer, taula, objecte):
    # Abrir la base de datos
    storage = ZODB.FileStorage.FileStorage(fitxer)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()
    root[taula]=objecte
    transaction.commit()
    connection.close()


def recuperar(fitxer,taula):
    pepe=[]
    storage = ZODB.FileStorage.FileStorage(fitxer)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()
    for p in root[taula]:
        pepe.append(p)
    return pepe