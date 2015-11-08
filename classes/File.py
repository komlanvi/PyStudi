import pickle


class File:
    """Classe per la gestione di File
    """

    def __init__(self, name):
        self.name = name
        self.myPickler = None
        self.myUnpickler = None

    def readLine(self):
        with open(self.name, "rb") as myFile:
            self.myUnpickler = pickle.Unpickler(myFile)
            return self.myUnpickler.load()

    def readLines(self):
        lista = []
        line = ""
        with open(self.name, "rb") as myFile:
            self.myUnpickler = pickle.Unpickler(myFile)
            while 1:
                try:
                    line = self.myUnpickler.load()
                    if line == "":
                        break
                    lista.append(line)
                except EOFError:
                    break
        return lista

    def write(self, *arg):
        with open(self.name, "wb") as myFile:
            self.myPickler = pickle.Pickler(myFile)
            for item in arg:
                self.myPickler.dump(item)