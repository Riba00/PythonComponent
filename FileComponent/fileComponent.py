import pickle


def saveObject(object1, filePath):
    with open(filePath, "ab") as file:
        pickle.dump(object1, file)
    file.close()


def deleteFileContent(file):
    with open(file, "wb") as file:
        pass
    file.close()


def getAll(filePath):
    data = []
    with open(filePath, "rb") as file:
        while True:
            try:
                object1 = pickle.load(file)
                data.append(object1)
            except EOFError:
                break
    file.close()
    return data
