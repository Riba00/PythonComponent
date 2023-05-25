import pymongo
import json
import Usuari

from Usuari import Usuari

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MP06"]
mycol = mydb["tictactoe"]


def guardarPartida(partida):
    return mycol.insert_one(partida.__dict__)


def reocuperarPartides(usuari):
    query = {"id_usuari":usuari._id}
    return mycol.find(query)
def reocuperarPartida(usuari,idpartida):
    partida = getobject(usuari,idpartida)
    return partida
    #varchar tauler
    #torn id?

def getobject(usuari,idpartida):
    query = {"usuari":usuari}
    return mycol.find_one(query)

def getuser(nom):
    query = {"nom": nom}
    u = Usuari.from_dict(mycol.find_one(query))
    return u

def newuser(nom, contra):#already checked if exists
    usuari = Usuari(nom,contra)
    return mycol.insert_one(usuari.__dict__)
