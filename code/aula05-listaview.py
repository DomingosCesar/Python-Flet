'''Aula 05 - Lista de Itens usando listaView'''
import flet as ft


def main(page : ft.Page):
    lista = ft.ListView(spacing=2, expand=True)
    
    for i in range(50):
        lista.controls.append(ft.Text(f"Estamos na linha {i}"))
        
    # page.update()
    # page.scroll = "always"
    page.add(lista)
    


ft.app(target=main)