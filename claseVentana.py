class Ventana:
    __t = ""
    __XvSup = float
    __YvSup = float
    __XvInf = float
    __YvInf = float

    def __init__(self, tit="ventana", Xs=0, Ys=0, Xi=500, Yi=500):
        self.__t = tit
        self.__XvSup = Xs
        self.__YvSup = Ys
        self.__XvInf = Xi
        self.__YvInf = Yi

    def mostrar(self):
        print("Titulo:", self.__t, "Xsup:", self.__XvSup, "Ysup:", self.__YvSup, "Xinf:", self.__XvInf, "Yinf:", self.__YvInf)

    def getTitulo(self):
        return self.__t


    def alto(self):
        return (self.__YvInf - self.__YvSup)

    def ancho(self):
        return (self.__XvInf - self.__XvSup)


    def moverDerecha(self, derecha=1):
        if self.__XvSup+derecha>=0:
            self.__XvSup+=derecha

        if self.__XvInf+derecha<=500:
            self.__XvInf+=derecha



    def moverIzquierda(self, izquierda=1):
        if self.__XvSup-izquierda>=0:
            self.__XvSup-=izquierda

        if self.__XvInf-izquierda<=500:
            self.__XvInf-=izquierda


    def bajar(self, baja=1):
        if self.__YvSup-baja>=0:
            self.__YvSup-=baja

        if self.__YvInf-baja<=500:
            self.__YvInf-=baja

    def subir(self, sube=1):
        if self.__YvSup+sube>=0:
            self.__YvSup+=sube
        if self.__YvInf+sube<=500:
            self.__YvInf+=sube
