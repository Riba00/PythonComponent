import psycopg2
from config import config

from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
from flask import Flask, redirect, url_for, session
from flask_session import Session
from backend import Selectsentencia, insertsentencia

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


def newGame():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    session["tokens1"] = 1
    session["tokens2"] = 0
    session["board"] = board
    session["playerActive"] = 1
    session["movimients"] = 0


@app.route('/')
def default():
    enviroment = Environment(loader=FileSystemLoader("Template/"))
    template = enviroment.get_template("register.html")
    info = {"tokens1": session['tokens1'], "tokens2": session['tokens2'], "board": session["board"]}
    contingut = template.render(info)
    return f'{contingut}'


@app.route('/login')
def defaultlogin():
    enviroment = Environment(loader=FileSystemLoader("Template/"))
    template = enviroment.get_template("login.html")
    info = {"tokens1": session['tokens1'], "tokens2": session['tokens2'], "board": session["board"]}
    contingut = template.render(info)
    return f'{contingut}'


@app.route('/joc')
def game():
    newGame()
    enviroment = Environment(loader=FileSystemLoader("Template/"))
    template = enviroment.get_template("base.html")
    info = {"tokens1": session['tokens1'], "tokens2": session['tokens2'], "board": session["board"]}
    contingut = template.render(info)
    return f'{contingut}'


@app.route('/joccarregat')
def game2():
    enviroment = Environment(loader=FileSystemLoader("Template/"))
    template = enviroment.get_template("base.html")
    info = {"tokens1": session['tokens1'], "tokens2": session['tokens2'], "board": session["board"]}
    contingut = template.render(info)
    return f'{contingut}'


def checkWiner(fixa, player):
    if fixa[0] == fixa[1] == fixa[2] != 0:
        return player
    if fixa[3] == fixa[4] == fixa[5] != 0:
        return player
    if fixa[6] == fixa[7] == fixa[8] != 0:
        return player

    if fixa[0] == fixa[3] == fixa[6] != 0:
        return player
    if fixa[1] == fixa[4] == fixa[7] != 0:
        return player
    if fixa[2] == fixa[5] == fixa[8] != 0:
        return player

    if fixa[0] == fixa[4] == fixa[8] != 0:
        return player
    if fixa[2] == fixa[4] == fixa[6] != 0:
        return player

    session["movimients"] = session["movimients"] + 1
    print(session["movimients"])
    if session["movimients"] == 9:
        return 3


@app.route('/movement', methods=['POST', 'GET'])
def move():
    position = request.form['position']
    print(position)
    session["board"][int(position) - 1] = session["playerActive"]
    if session["playerActive"] == 1:
        session["playerActive"] = 2
        session["tokens1"] = 0
        session["tokens2"] = 1
    else:
        session["playerActive"] = 1
        session["tokens1"] = 1
        session["tokens2"] = 0

    winer = checkWiner(session["board"], session["playerActive"])
    if winer == 1:
        info = {"info": "Victoria per a Jugador 2"}
        enviroment = Environment(loader=FileSystemLoader("Template/"))
        template = enviroment.get_template("finalGame.html")
        contingut = template.render(info)
        return f'{contingut}'

    elif winer == 2:
        info = {"info": "Victoria per a Jugador 1"}
        enviroment = Environment(loader=FileSystemLoader("Template/"))
        template = enviroment.get_template("finalGame.html")
        contingut = template.render(info)
        return f'{contingut}'

    elif winer == 3:
        info = {"info": "Empat!"}
        enviroment = Environment(loader=FileSystemLoader("Template/"))
        template = enviroment.get_template("finalGame.html")
        contingut = template.render(info)
        return f'{contingut}'

    info = {"tokens1": session['tokens1'], "tokens2": session['tokens2'], "board": session["board"]}
    enviroment = Environment(loader=FileSystemLoader("Template/"))
    template = enviroment.get_template("base.html")
    contingut = template.render(info)
    print(info)
    return f'{contingut}'


@app.route('/register', methods=['POST'])
def createUser():
    arrayNoms = []
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    user = request.form.get('user')
    password = request.form.get('password')
    consulta = ("SELECT name FROM account;")
    cerca = Selectsentencia(consulta)
    for row in cerca:
        arrayNoms.append(row[0])
    print(arrayNoms)
    if user in arrayNoms:
        return redirect('/')
    else:
        consulta = (f"insert into account (name, password) VALUES  ('" + user + "','" + password + "');")
        insertsentencia(str(consulta))
        consulta2 = ("SELECT id FROM account WHERE name = '" + user + "' ;")
        cerca2 = Selectsentencia(consulta2)
        numero2 = str(cerca2)
        numerostr2 = numero2.strip("[]'(),")
        session["userId"] = numerostr2

    return redirect("/joc")


@app.route('/loginaccept', methods=['POST'])
def searchUser():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        user = request.form.get('user')
        password = request.form.get('password')
        consulta = "SELECT COUNT(*) FROM account WHERE name ='" + user + "' AND password ='" + password + "';"
        consulta2 = "SELECT id from account where name ='" + user + "' AND password ='" + password + "';"

        cerca = Selectsentencia(consulta2)
        num = Selectsentencia(consulta)
        for i in num:
            count = i
        count = count[0]
        numero = str(cerca[0])
        numerostr = numero.strip('(),')
        session["userId"] = numerostr

        if count > 0:
            return redirect("/joc")  # Redirigir a "/joc" si hay una coincidencia exitosa
        else:
            return redirect("/login")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


@app.route('/saveGame', methods=['GET'])
def saveGame():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        print(3)

        board_str = ",".join(str(num) for num in session["board"])

        consulta = f"""INSERT INTO games
              (playerActive, board, idplayer)
              VALUES
              ({session["playerActive"]}, '{board_str}', {session["userId"]});
           """
        print(2)

        print(consulta)
        cur = conn.cursor()
        insertsentencia(consulta)

        return redirect("/joc")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


@app.route('/recuperarPartida')
def recoverGame():
    registredGames = []
    try:

        consulta = f"""SELECT * from games where
        idplayer = '{session["userId"]}' order by fecha desc;
           """

        resultados = Selectsentencia(consulta)

        for x in resultados:
            registredGames.append(x)
        registredGames = {"registredGames": registredGames}

        enviroment = Environment(loader=FileSystemLoader("Template/"))
        template = enviroment.get_template("recoverGame.html")
        contingut = template.render(registredGames)
        return f'{contingut}'


    except (Exception, psycopg2.DatabaseError) as error:

        print(error)


@app.route('/game/<idGame>')
def choseGame(idGame):
    session["idGame"] = idGame
    resultatGame = []
    consulta = f"""SELECT playeractive,board from games where 
              id = '{idGame}';
                 """

    resultados = Selectsentencia(consulta)
    print(resultados)
    session["board"] = resultados[0][1].replace(",", " ")
    print(session["board"])
    for i in session["board"].split():
        resultatGame.append(int(i))

    session['board'] = resultatGame
    if resultados[0][1] == 1:
        session['tokens1'] = 1
        session['tokens2'] = 0
        session["playerActive"] = 1
    else:
        session['tokens1'] = 0
        session['tokens2'] = 1
        session["playerActive"] = 2

    return redirect('/joccarregat')
