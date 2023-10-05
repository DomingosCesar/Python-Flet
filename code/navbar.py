from flet import *


def main(page : Page):
    page.title = "Barra de navegacao"
    
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME, label="Home"),
            NavigationDestination(icon=icons.EXPLORE, label="Explore"),
            NavigationDestination(icon=icons.COMMUTE, label="Rotas"),
        ]
    )

    page.add(Text("Corpo da Aplicacao"))

app(target=main)