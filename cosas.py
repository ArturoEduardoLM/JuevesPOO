class Autor:
    def __init__ (self, nom, pseudo):
        self.__nombre= nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom
    @property
    def pseudonimo (self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"Nombre: {self.__nombre} Pseudonimo: {self.__pseudonimo}"

    def ecribir(self):
        print(f"{self.__pseudonimo} está escribiendo su siguiente obra")

class Libro:
    def __init__(self, tit, aut, an, edit):
        self.__titulo = tit
        self.__autor = aut
        self.__año = an
        self.__editorial = edit

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, tit):
        self.__titulo = tit

    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, an):
        self.__año = an

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, edit):
        self.__editorial = edit


    def __str__(self):
        return f""" 
        Titulo = {self.__titulo}
        Año = {self.__año}
        Editorial = {self.__editorial}
        Autor = {self.__autor}
        """

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, aut):
        self.__autor = aut
    @classmethod
    def libro_planeta (cls, titulo, autor, año):
        return cls(titulo, autor, año, "planeta")

    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")

class Persona:
    def __init__(self,nom, ed):
        self.__nombre = nom
        self.__edad = ed

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, ed):
        self.__edad = ed



class Alumno(Persona):
        def __init__(self, nombre, edad, numer_cuenta, carrera, promedio):
            super().__init__(nombre, edad)
            self.__numero_cuenta = numer_cuenta
            self.__carrera = carrera
            self.__promedio = promedio