# Mòdul MongoDB per a la gestió del joc Tic Tac Toe

Aquest mòdul proporciona funcionalitat per a desar i recuperar partides del joc Tic Tac Toe utilitzant una base de dades MongoDB.

## Requisits

- Servidor MongoDB en execució a l'adreça `localhost` i al port `27017`
- Llibreria `pymongo`
- Classe `Usuari` i `Partida` per a la gestió del joc

## Funcions

### `guardarPartida(partida)`

Desa una partida a la base de dades.

- `partida`: Objecte partida a desar
- Retorna: Identificador únic generat per MongoDB per a la partida desada

### `recuperarPartides(usuari)`

Recupera les partides associades a un usuari de la base de dades.

- `usuari`: Objecte Usuari
- Retorna: Cursor de MongoDB amb les partides trobades

### `recuperarPartida(usuari, idpartida)`

Recupera una partida específica d'un usuari de la base de dades.

- `usuari`: Objecte Usuari
- `idpartida`: Identificador de la partida a recuperar
- Retorna: Objecte partida recuperada o `None` si no s'ha trobat

### `getobject(usuari, idpartida)`

Recupera una partida específica d'un usuari de la base de dades.

- `usuari`: Objecte Usuari
- `idpartida`: Identificador de la partida a recuperar
- Retorna: Objecte partida recuperada o `None` si no s'ha trobat

### `getuser(nom)`

Recupera un usuari a partir del seu nom d'usuari.

- `nom`: Nom d'usuari
- Retorna: Objecte Usuari o `None` si no s'ha trobat cap usuari amb aquest nom

### `newuser(nom, contra)`

Crea un nou usuari a la base de dades.

- `nom`: Nom d'usuari
- `contra`: Contrasenya de l'usuari
- Utilitzem `del` per eliminar el camp _id i que mongodb s'encarregui de crear-la random
- Retorna: Identificador únic generat per MongoDB per a l'usuari creat
