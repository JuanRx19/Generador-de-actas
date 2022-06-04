from model.Acta import Acta
from model.GenerarPDF import generar_acta


def crear_acta_partial(st, ctrl):
    st.title("Crear acta")
    columna1, columna2, columna3, columna4 = st.columns(4)
    columna5, columna6, columna7 = st.columns(3)
    columna8, columna9, columna10, columna11, columna12, columna13 = st.columns(6)
    acta = Acta(ctrl.criterios)
    with columna1:
        acta.autor = st.text_input("AUTOR")
    with columna2:
        acta.nombre_del_trabajo = st.text_input("NOMBRE DEL TRABAJO ELABORADO")
    with columna3:
        acta.tipo_de_trabajo = st.selectbox('TIPO DE TRABAJO', ('APLICADO', 'INVESTIGACIÓN'))
    with columna4:
        acta.fecha = st.date_input("FECHA")
    verificar_co_director = st.checkbox("¿Existe codirector?")
    if(verificar_co_director):
        nombre_del_codirector = st.text_input("NOMBRE DEL CODIRECTOR")
    with columna5:
        acta.jurado1 = st.text_input("NOMBRE DEL JURADO 1")
    with columna6:
        acta.jurado2 = st.text_input("NOMBRE DEL JURADO 2")
    with columna7:
        acta.director = st.text_input("NOMBRE DEL DIRECTOR")
    with columna8:
        acta.numero = st.text_input("NÚMERO")

    #Verificar datos
    if (acta.autor != "" and acta.numero != "" and acta.director != "" and acta.nombre_del_trabajo != "" and acta.jurado1 != "" and acta.jurado2 != "" and (not(verificar_co_director) or nombre_del_codirector != "")):
        enviar = st.button("ENVIAR")
        if(enviar):
            ctrl.agregar_acta(acta)
            st.info("Ahora puedes ver tu acta en historicos :)")
    else:
        st.info("Querido usuario. Recuerde llenar todos los campos :)")

def ver_historicos_partial(st, ctrl):
    num = 0
    for actas in ctrl.actas:
        with st.expander(label="Acta #" + actas.numero, expanded=False):
            columna1, columna2, columna3, columna4 = st.columns(4)
            with columna1:
                st.write("#### AUTOR")
                st.write(actas.autor)
                st.write("#### JURADO 1")
                st.write(actas.jurado1)
                if(actas.acta_calificada):
                    st.write("##### Nota")
                    generar_acta(st, actas, actas.autor + actas.nombre_del_trabajo)
                else:
                    st.write("Acta pendiente por calificar")
                if (actas.nota_final < 3 or (actas.criterios["Calidad y presentación del documento escrito"].nota1 + actas.criterios["Calidad y presentación del documento escrito"].nota2) / 2 < 3):
                    actas.observacion_estudiante = st.text_input("Observaciones del estudiante", key=num)
                    st.write(actas.observacion_estudiante)
                    num+=1
            with columna2:
                st.write("#### NOMBRE DEL TRABAJO")
                st.write(actas.nombre_del_trabajo)
                st.write("#### JURADO 2")
                st.write(actas.jurado2)
                if (actas.acta_calificada):
                    st.write(actas.nota_final)
            with columna3:
                st.write("#### TIPO DE TRABAJO")
                st.write(actas.tipo_de_trabajo)
                st.write("#### DIRECTOR")
                st.write(actas.director)
                if (actas.acta_calificada):
                    if(actas.nota_final < 3.5):
                        st.write("*REPROBADO*")
                    else:
                        st.write("*APROBADO*")
            with columna4:
                st.write("#### FECHA")
                st.write(actas.fecha)
                if (actas.nombre_del_codirector != ""):
                    st.write("#### CO-DIRECTOR")
                    st.write(actas.nombre_del_codirector)

def valorar_criterios_partial(st, ctrl):
    st.title("Valoración")
    num = 1
    acumulado_de_notas = 0
    st.write("### Bienvenido, aquí podras calificar cada trabajo pendiente por evaluar.")
    calificar = st.selectbox("NOMBRE DEL TRABAJO A CALIFICAR", (actas.nombre_del_trabajo for actas in ctrl.actas if(not(actas.acta_calificada))))
    if not calificar:
        st.warning("Querido jurado, aún no hay actas pendientes por calificar.")
    else:
        st.write("### Criterios a evaluar.")
        for actas in ctrl.actas:
            if calificar == actas.nombre_del_trabajo:
                num = 1
                for criterios in actas.criterios:
                    st.write("##### " + criterios + " " + str(actas.criterios[criterios].porcentaje*100) + "%")
                    actas.criterios[criterios].nota1 = st.number_input("Nota de " + str(actas.jurado1), 0.0, 5.0, step=0.5, key=num)
                    num += 1
                    actas.criterios[criterios].nota2 = st.number_input("Nota de " + str(actas.jurado2), 0.0, 5.0, step=0.5, key=num)
                    num += 1
                    actas.criterios[criterios].observacion = st.text_input("Observaciones ", key=num)
                    num += 1
                    actas.nota_final = ((actas.criterios[criterios].nota1 + actas.criterios[criterios].nota2) / 2) * actas.criterios[criterios].porcentaje
                    acumulado_de_notas += actas.nota_final
                actas.nota_final = acumulado_de_notas
                if st.button("Calificar"):
                    st.write("### Nota final: " + str(actas.nota_final))
                    actas.acta_calificada = True
                    st.snow()
                else:
                    st.warning("Recuerde pulsar el botón calificar.")

def modificar_criterios_partial(st, ctrl):
    excedente = -0.2 / (len(ctrl.criterios) - 1)
    st.title("Modificar y/o agregar criterios")
    st.write("### Modificar criterio")
    with st.expander(label="", expanded=False):
        st.write("##### Por favor digite el criterio que desea modificar")
        opcion = st.selectbox("NOMBRE DEL TRABAJO A CALIFICAR", (criterios for criterios in ctrl.criterios))
        nuevo_porcentaje = st.number_input("Por favor digite el nuevo porcentaje")
        nuevo_porcentaje = nuevo_porcentaje / 100
        cantidad_restar = nuevo_porcentaje / (len(ctrl.criterios) - 1)
        if(st.button("Modificar criterio")):
            for criterios in ctrl.criterios:
                if(not(opcion == ctrl.criterios[criterios].criterio)):
                    ctrl.criterios[criterios].porcentaje -= cantidad_restar + excedente
                elif(opcion == ctrl.criterios[criterios].criterio and nuevo_porcentaje != 0):
                    ctrl.criterios[criterios].porcentaje = nuevo_porcentaje
            for actas in ctrl.actas:
                if(not(actas.acta_calificada)):
                    actas.criterios = ctrl.criterios


def agregar_criterios_partial(st, ctrl):
    excedente = -0.2 / (len(ctrl.criterios) - 1)
    st.write("### Agregar criterio")
    with st.expander(label="", expanded=False):
        st.write("##### Información del criterio a adicionar")
        criterio_nuevo = st.text_input("Por favor digite el criterio")
        nuevo_porcentaje = st.number_input("Por favor digite el porcentaje del criterio")
        nuevo_porcentaje = nuevo_porcentaje / 100
        cantidad_restar = nuevo_porcentaje / (len(ctrl.criterios))
        if (st.button("Agregar criterio")):
            for criterio in ctrl.criterios:
                ctrl.criterios[criterio].porcentaje -= cantidad_restar
            ctrl.agregar_criterio(criterio_nuevo, nuevo_porcentaje)
            for actas in ctrl.actas:
                if (not (actas.acta_calificada)):
                    actas.criterios = ctrl.criterios