from model.datosActa import datosActa

def crearActa(st, ctrl):
    st.title("Crear acta")
    columna1, columna2, columna3, columna4 = st.columns(4)
    columna5, columna6, columna7 = st.columns(3)
    columna8, columna9, columna10, columna11, columna12, columna13 = st.columns(6)
    acta = datosActa(ctrl.criterios)
    with columna1:
        acta.autor = st.text_input("AUTOR")
    with columna2:
        acta.nombreDelTrabajo = st.text_input("NOMBRE DEL TRABAJO ELABORADO")
    with columna3:
        acta.tipoDeTrabajo = st.selectbox('TIPO DE TRABAJO', ('APLICADO', 'INVESTIGACIÓN'))
    with columna4:
        acta.fecha = st.date_input("FECHA")
    verificarCoDirector = st.checkbox("¿Existe codirector?")
    if(verificarCoDirector):
        acta.nombreDelCoDirector = st.text_input("NOMBRE DEL CODIRECTOR")

    with columna5:
        acta.jurado1 = st.text_input("NOMBRE DEL JURADO 1")
    with columna6:
        acta.jurado2 = st.text_input("NOMBRE DEL JURADO 2")
    with columna7:
        acta.director = st.text_input("NOMBRE DEL DIRECTOR")
    with columna8:
        acta.numero = st.text_input("NÚMERO")

    #Verificar datos
    if (acta.autor != "" and acta.numero != "" and acta.director != "" and acta.nombreDelTrabajo != "" and acta.jurado1 != "" and acta.jurado2 != "" and (not(verificarCoDirector) or acta.nombreDelCoDirector != "")):
        enviar = st.button("ENVIAR")
        if(enviar):
            ctrl.agregarActa(acta)
            historicos = st.button("VER HISTORICOS")
    else:
        st.info("Querido usuario. Recuerde llenar todos los campos :)")

def historicos(st, ctrl):
    for i in ctrl.actas:
        with st.expander(label="Acta #" + i.numero, expanded=False):
            columna1, columna2, columna3, columna4 = st.columns(4)
            with columna1:
                st.write("#### AUTOR")
                st.write(i.autor)
                st.write("#### JURADO 1")
                st.write(i.jurado1)
                if(i.actaCalificada):
                    st.write("##### Nota")
                else:
                    st.write("Acta pendiente por calificar")
            with columna2:
                st.write("#### NOMBRE DEL TRABAJO")
                st.write(i.nombreDelTrabajo)
                st.write("#### JURADO 2")
                st.write(i.jurado2)
                if (i.actaCalificada):
                    st.write(i.notaFinal)
            with columna3:
                st.write("#### TIPO DE TRABAJO")
                st.write(i.tipoDeTrabajo)
                st.write("#### DIRECTOR")
                st.write(i.director)
                if (i.actaCalificada):
                    if(i.notaFinal < 3.5):
                        st.write("*REPROBADO*")
                    else:
                        st.write("*APROBADO*")
            with columna4:
                st.write("#### FECHA")
                st.write(i.fecha)
                if(i.nombreDelCoDirector != ""):
                    st.write("#### CO-DIRECTOR")
                    st.write(i.nombreDelCoDirector)

def valorarCriterios(st, ctrl):
    st.title("Valoración")
    num = 1
    acumuladoDeNotas = 0
    st.write("### Bienvenido, aquí podras calificar cada trabajo pendiente por evaluar.")
    calificar = st.selectbox("NOMBRE DEL TRABAJO A CALIFICAR", (i.nombreDelTrabajo for i in ctrl.actas if(not(i.actaCalificada))))
    if not calificar:
        st.warning("Querido jurado, aún no hay actas pendientes por calificar.")
    else:
        st.write("### Criterios a evaluar.")
        for actas in ctrl.actas:
            for criterios in actas.criterios:
                st.write("##### " + criterios)
                actas.criterios[criterios].nota1 = st.slider(str(actas.jurado1) + " nota " + str(num), 0.0, 5.0, step=0.5)
                num += 1
                actas.criterios[criterios].nota2 = st.slider(str(actas.jurado2) + " nota " + str(num-1), 0.0, 5.0, step=0.5)
                actas.criterios[criterios].observacion = st.text_input("Observaciones " + str(num-1))
                actas.notaFinal = ((actas.criterios[criterios].nota1 + actas.criterios[criterios].nota2) / 2) * actas.criterios[criterios].porcentaje
                acumuladoDeNotas += actas.notaFinal
        actas.notaFinal = acumuladoDeNotas

        if st.button("Calificar"):
            st.write("### Nota final: " + str(actas.notaFinal))
            actas.actaCalificada = True
        else:
            st.warning("Recuerde pulsar el botón calificar.")