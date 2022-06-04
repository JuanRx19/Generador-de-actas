from fpdf import FPDF
import base64


def generar_link(val, filename):
    b64 = base64.b64encode(
        val)  # Codifica el objeto similar a bytes s utilizando Base64 y retorna los bytes codificados
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


def lineas(pdf, num):
    pdf.set_font('Arial', size=11)
    for i in range(num):
        pdf.cell(200, 10, txt="_____________________________________________________________________________________",
                 ln=1, align='L')


def numero_a_texto(ent):
    nota = str(ent)
    mayusculas = ['Cero', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco']
    minusculas = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    primer_caracter = mayusculas[int(nota[0])]
    segundo_caracter = minusculas[int(nota[2])]
    return str(primer_caracter) + " punto " + str(segundo_caracter)


def definir_codirector(acta):
    if (acta.nombre_del_codirector != ""):
        return acta.nombre_del_codirector
    else:
        return "NA"


def generar_datos(pdf, acta):
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 7, txt='Trabajo de grado denominado: "' + acta.nombre_del_trabajo + '"', align='L', border=0)
    pdf.cell(40, 10, txt='Autor: ', ln=0, align='L', border=0)
    pdf.cell(100, 10, txt=str(acta.autor), ln=0, align='L')
    pdf.cell(50, 10, txt='ID: ' + str(0), ln=1, align='L')
    pdf.cell(40, 10, txt='Periodo: ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(acta.fecha), ln=1, align='L')
    pdf.cell(40, 10, txt='Director: ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(acta.director), ln=1, align='L')
    pdf.cell(40, 10, txt='Co-Director: ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(definir_codirector(acta)), ln=1, align='L')
    pdf.cell(40, 10, txt='Énfasis en:  ', ln=0, align='L')
    pdf.cell(100, 10, txt="Sistemas y Computación", ln=1, align='L')
    pdf.cell(40, 10, txt='Modalidad:  ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(acta.tipo_de_trabajo), ln=1, align='L')
    pdf.cell(40, 10, txt='Jurado 1:  ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(acta.jurado1), ln=1, align='L')
    pdf.cell(40, 10, txt='Jurado 2:  ', ln=0, align='L')
    pdf.cell(100, 10, txt=str(acta.jurado2), ln=1, align='L')


def generar_acta(st, acta, key):
    from datetime import datetime
    class PDF(FPDF):
        def header(self):
            from datetime import datetime
            año = datetime.today().strftime('%Y')
            dia = datetime.today().strftime('%Y-%m-%d')
            pdf.set_font('Arial', "B", size=17)
            pdf.image('img\puj.jpeg', 15,
                      10, 40)
            pdf.cell(200, 10, txt='Facultad de Ingeniería', ln=1, align='C')
            pdf.cell(200, 10, txt='Maestría en Ingeniería', ln=2, align='C')
            pdf.set_font('Arial', "B", size=13)
            pdf.cell(150, 10, txt='ACTA: 3 -' + año, ln=0, align='L')
            pdf.cell(16, 10, txt='Fecha: ', ln=0, align='L')
            pdf.cell(0, 10, txt=dia, ln=1, align='L')

    pdf = PDF()
    pdf.add_page()
    pdf.auto_page_break
    pdf.set_right_margin(3)
    pdf.set_top_margin(15)
    pdf.alias_nb_pages()
    pdf.set_font('Arial', size=13)
    pdf.set_font('Arial', "B", size=13)
    pdf.cell(200, 10, txt='ACTA DE EVALUACIÓN DE TRABAJO DE GRADO', ln=1, align='C')
    pdf.set_font('Arial', size=13)
    contador = 0
    observaciones = st.text_input("Observaciones adicionales", key=key)
    generar_datos(pdf, acta)
    pdf.set_font('Arial', size=12)
    enunciado_uno = 'En atención al desarrollo de este Trabajo de Grado y al documento y sustentación que presentó el(la) autor(a), los Jurados damos las siguientes calificaciones parciales y observaciones (los criterios a evaluar y sus ponderaciones se estipulan en el artículo 7.1 de las Directrices para Trabajo de Grado de Maestría)'
    pdf.multi_cell(0, 7, txt=enunciado_uno)
    num = 1

    for criterio in acta.criterios:
        pdf.set_font('Arial', "B", size=12)
        pdf.cell(100, 10, txt=str(str(num) + '. ' + criterio), ln=1, align='L')
        num += 1
        pdf.set_font('Arial', size=13)
        nota_redondeada = ((acta.criterios[criterio].nota1 + acta.criterios[criterio].nota2) / 2)
        nota_redondeada = nota_redondeada.__round__(1)
        pdf.set_font('Arial', size=11)
        pdf.cell(150, 10, txt=str('Calificación parcial: ' + str(nota_redondeada)), ln=0, align='L')
        pdf.cell(100, 10,
                 txt=str('Ponderacion: ' + str((acta.criterios[criterio].porcentaje * 100).__round__(1)) + '%'), ln=1,
                 align='L')
        pdf.multi_cell(0, 10, txt=str('Observaciones: ' + acta.criterios[criterio].observacion), align='L')
        lineas(pdf, 2)
        pdf.set_font('Arial', size=11)

    pdf.set_font('Arial', "B", size=11)
    pdf.cell(40, 7,
             txt="Como resultado de estas calificaciones parciales y sus ponderaciones, la calificación del Trabajo de",
             ln=1, align='L')
    pdf.cell(40, 3, txt="Grado es: " + str(acta.nota_final), ln=1, align='L')
    nota_letras = numero_a_texto(str(acta.nota_final))
    pdf.cell(100, 7, txt='', ln=1, align='L')
    pdf.cell(150, 3, txt=str(acta.nota_final), ln=0, align='L')
    pdf.cell(100, 3, txt=nota_letras, ln=1, align='L')
    pdf.cell(150, 5, txt="Números", ln=0, align='L')
    pdf.cell(100, 5, txt="Letras", ln=1, align='L')
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, txt=str('Observaciones adicionales: ' + observaciones), align='L')
    lineas(pdf, 3)
    pdf.cell(100, 10, txt=str('La calificación final queda sujeta a que se implementen las siguientes correciones: '),
             ln=1, align='L')
    lineas(pdf, 3)
    pdf.cell(100, 40, txt='', ln=1, align='L')
    pdf.cell(100, 5, txt="___________________________________", ln=0, align='L')
    pdf.cell(100, 5, txt="___________________________________", ln=1, align='L')
    pdf.cell(100, 5, txt="Firma del Jurado 1", ln=0, align='C')
    pdf.cell(100, 5, txt="Firma del Jurado 2", ln=2, align='C')
    contador += 1

    if (acta.nota_final > 4.5):
        pdf.add_page()
        pdf.set_font('Arial', "B", size=12)
        pdf.cell(0, 10, txt='RECOMENDACIÓN DE MENCIÓN DE HONOR AL TRABAJO DE GRADO', ln=1, align='C')
        generar_datos(pdf, acta)
        enunciado_dos = "En atención a que el Trabajo de Grado se distingue porque la calificación del trabajo es superior a 4,50 y se destaca por dos condiciones (que indicamos) de las siguientes tres como se estipula en el artículo 7.6 de las Directrices para Trabajo de Grado de Maestría:"
        pdf.multi_cell(0, 7, txt=enunciado_dos)
        pdf.cell(100, 5, txt="", ln=1, align='L')
        pdf.cell(100, 5, txt="- El estudiante superó los objetivos propuestos. _____ ", ln=1, align='L')
        pdf.cell(100, 5,
                 txt="- El estudiante demostró una profundidad destacable en el conocimiento y tratamiento del tema. _____ ",
                 ln=1, align='L')
        pdf.cell(100, 5, txt="- El tema ofrecia una dificultad superior a lo ordinario. _____ ", ln=1, align='L')
        pdf.cell(100, 5, txt="", ln=1, align='L')
        pdf.cell(100, 5, txt="", ln=1, align='L')
        enunciado_tres = "Los Jurados recomendamos que el Consejo de la Facultad otorgue Mención de Honor a este Trabajo de Grado, y motivamos esta recomendación con base en las siguientes apreciaciones:"
        pdf.multi_cell(0, 7, txt=enunciado_tres)
        pdf.cell(100, 5, txt="", ln=1, align='L')
        lineas(pdf, 1)
        pdf.cell(100, 20, txt="", ln=1, align='L')
        pdf.cell(100, 5, txt="___________________________________", ln=0, align='L')
        pdf.cell(100, 5, txt="___________________________________", ln=1, align='L')
        pdf.cell(100, 5, txt="Firma del Jurado 1", ln=0, align='C')
        pdf.cell(100, 5, txt="Firma del Jurado 2", ln=2, align='C')
        pdf.cell(100, 5, txt="", ln=1, align='L')
        pdf.set_font('Arial', "B", size=12)
        pdf.cell(100, 5, txt="Decisión del Consejo de la Facultad:", ln=1, align='L')
        pdf.set_font('Arial', size=12)
        pdf.cell(100, 5, txt="- Conceder Mención de Honor al Proyecto de Grado. _______ ", ln=1, align='L')
        pdf.cell(100, 5, txt="- No Conceder Mención de Honor al Proyecto de Grado. _____ ", ln=1, align='L')
        pdf.cell(100, 5, txt="- Tal y como se consigna en el Acta No. _____ del Consejo de la Facultad.", ln=1,
                 align='L')

    if st.button('Generar PDF', key=key):
        st.markdown(generar_link(pdf.output(dest="S").encode("latin-1"), str(acta.autor) + '-' + str(acta.fecha)),
                    unsafe_allow_html=True)
