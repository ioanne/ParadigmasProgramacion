class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()


with FileManager("archivo.txt", "r") as archivo:
    print(archivo.readline())

archivo.readline()
