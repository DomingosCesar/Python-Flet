from flet import *
def main(page : Page):
    # Parte 1 - Criar a alerta
    alerta = AlertDialog(
        title=Text("Informacao Importante"),
        content= Text("Ola usuario da nossa aplicacao, estamos felizes por te ter aqui connosco"),
        on_dismiss= lambda e:print("Alerta fechada!")
    )

    # Parte 3 - Criar a funcao que permite abrir a alerta
    def abrir_alerta(e):
        page.dialog = alerta
        alerta.open = True
        page.update()

    # Parte 2 - criar o botao que vai abrir a alerta
    page.add(
        Text("Ola Mundo!"),
        ElevatedButton("Informacao", on_click=abrir_alerta)
    )

app(target=main)