import streamlit as st

from pydataxm.pydataxm import ReadDB
from streamlit_option_menu import option_menu
from view.ActaPartial import *
from view.AboutPartial import *
from controller.Controlador import Controlador

class MainView:

    def __init__(self) -> None:
        super().__init__()

        if 'main_view' not in st.session_state:
            self.menu_actual = "Acerca de nosotros"
            # Inicialización de las variables necesarias
            self.controller = Controlador()
            st.session_state['main_view'] = self
        else:
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller
             # Carga de las variables necesarias
        self._inicialializar_layout()

    def _inicialializar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Actas de grado", page_icon='https://www2.javerianacali.edu.co/sites/ujc/files/node/announcement/field_image_box/logo_javeriana_cali_0_0_0.jpg', layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3, self.col4 = st.columns([1, 1, 1, 1])

        # Define lo que abrá en la barra de menu
        self.menu_actual = option_menu(menu_title=None,
                                       options=["Acta - Asistente", 'Calificar - Jurado', 'Criterios', 'Historicos', 'Acerca de nosotros'],
                                       icons=['person-lines-fill', 'file-earmark', 'pencil-square', 'list-check', 'people-fill'],
                                       menu_icon="cast",
                                       default_index=4,
                                       orientation="horizontal",
                                       styles={
                                           "icon": {"color": "#5B68FF", "font-size": "25px"},
                                           "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px",
                                                        "--hover-color": "#585858"},
                                           "nav-link-selected": {"background-color": "#585858"},
                                       }
                                       )

    def controlar_menu(self):
        # Filtro opciones de menu
        if self.menu_actual == "Acerca de nosotros":
            st.markdown(mostrar())
            columna1, columna2, columna3, columna4 = st.columns(4)
            with columna2:
                #..\img\img
                st.image("img\juan.jpeg",  caption="Juan", width=250, use_column_width=None, clamp=False, channels="RGB",
                        output_format="auto")
            with columna3:
                st.image("img\santa.jpeg", caption="Santa", width=430, use_column_width=None, clamp=False, channels="RGB",
                         output_format="auto")
            st.write("")
        elif self.menu_actual == "Acta - Asistente":
            crear_acta_partial(st, self.controller)
        elif self.menu_actual == "Criterios":
            modificar_criterios_partial(st, self.controller)
        elif self.menu_actual == "Historicos":
            st.title("Historicos")
            ver_historicos_partial(st, self.controller)
        elif self.menu_actual == "Calificar - Jurado":
            valorar_criterios_partial(st, self.controller)


# Main call
if __name__ == "__main__":
    gui = MainView()
    gui.controlar_menu()
