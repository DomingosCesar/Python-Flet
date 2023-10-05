from flet import *

def main(page : Page):
    page.add(
        Text("Ola Mundo como estao?", size=30, color="red"),
        Container(
            width=200,
            height=200,
            bgcolor=colors.AMBER_100
        )
    )
    page.update()

app(target=main)