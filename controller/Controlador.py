from model.Criterio import criterios

class Controlador:

    def __init__(self) -> None:
        super().__init__()
        self.actas = []
        self.criterios = {"Desarrollo y profundidad en el tratamiento del tema" : criterios("Desarrollo y profundidad en el tratamiento del tema", 0.2),
               "Desafío académico y científico del tema": criterios("Desafío académico y científico del tema", 0.15),
               "Cumplimiento de los objetivos propuestos": criterios("Cumplimiento de los objetivos propuestos", 0.1),
               "Creatividad e innovación de las soluciones y desarrollos propuestos": criterios("Creatividad e innovación de las soluciones y desarrollos propuestos", 0.1),
               "Validez de los resultados y conclusiones": criterios("Validez de los resultados y conclusiones", 0.2),
               "Manejo y procesamiento de la información y bibliografía": criterios("Manejo y procesamiento de la información y bibliografía", 0.1),
               "Calidad y presentación del documento escrito": criterios("Calidad y presentación del documento escrito", 0.075),
               "Presentación oral": criterios("Presentación oral", 0.075)}

    def agregar_acta(self, acta):
        self.actas.append(acta)
    def agregar_criterio(self, criterio, porcentaje):
        self.criterios[criterio] = criterios(criterio, porcentaje)