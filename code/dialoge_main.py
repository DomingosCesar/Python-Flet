from flet import *

def main(page : Page):

    def confirmar(e):
        alerta_dialogo.open = False
        print("Item apagado com sucesso!")
        page.update()
    def cancelar(e):
        alerta_dialogo.open = False
        print("Cancelado com sucesso!")
        page.update()
    # Parte 1 - Criar a alerta
    alerta_dialogo = AlertDialog(
        modal=True,
        title=Text("Confirme a acao!"),
        content=Text("Deseja mesmo apagar os itens que acabaste de selecionar?\nSe continuares com essa acao nao teras mais volta!"),
        actions=[
            TextButton("Apagar", on_click=confirmar),
            TextButton("cancelar", on_click=cancelar)
        ],
        actions_alignment=MainAxisAlignment.END
    )

    # Parte 3 - Criar a funcao para abrir o modal
    def abrir_modal(e):
        page.dialog = alerta_dialogo
        alerta_dialogo.open = True
        page.update()
    # Parte 2 - criar o botao que vai abrir a alerta
    page.add(
        Text("Ola Mundo!"),
        ElevatedButton("Apagar Item",icon=icons.DELETE, icon_color='red', on_click=abrir_modal)
    )
    # PArte 4 - Criar funcao para fechar o modal




app(target=main)