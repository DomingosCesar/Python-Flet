'''Configuracao da pagina'''

import flet as ft

def main(page : ft.Page):
    #Titulo da pagina 
    page.title = "Aplicacao Teste"
    #Tema da pagina
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    pass



ft.app(target=main)