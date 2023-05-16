import ZODB
import ZODB.FileStorage
import transaction
class zodbComponent:
    def __init__(self, fitxer):
        storage = ZODB.FileStorage.FileStorage(fitxer)
        self.db = ZODB.DB(storage)
    def insert(self,taula, objecte):
        # Abrir la base de datos

        connection = self.db.open()
        root = connection.root()
        root[taula]=objecte
        transaction.commit()
        connection.close()


    def recuperar(self,fitxer,taula):
        pepe=[]

        connection = self.db.open()
        root = connection.root()
        for p in root[taula]:
            pepe.append(p)
        return pepe



