class Acta:

    def __init__(self, criterios) -> None:
        super().__init__()

        self.numero = ""
        self.autor = ""
        self.nombre_del_trabajo = ""
        self.tipo_de_trabajo = ""
        self.fecha = ""
        self.jurado1 = ""
        self.jurado2 = ""
        self.director = ""
        self.nombre_del_codirector = ""
        self.nota_final = 0
        self.criterios = criterios
        self.acta_calificada = False
        self.observacion_estudiante = ""