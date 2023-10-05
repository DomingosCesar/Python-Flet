from flet import *

def main(page : Page):
    page.title = "Alert"
    page.theme_mode = ThemeMode.LIGHT
    #Funcoes
    def atualizar(e):
        page.banner.open = False
        print("Atualizando...")
        page.theme_mode = ThemeMode.DARK
        page.update()
        
    def lembrar_mais_tarde(e):
        page.banner.open = False
        print("Lembrar mais tarde...")
        page.theme_mode = ThemeMode.LIGHT
        page.update()
        
    def cancelar(e):
        page.banner.open = False
        print("Cancelando...")
        page.update()
        
    page.banner = Banner(
        bgcolor=colors.AMBER_900,
        leading=Icon(icons.WARNING_SHARP),
        content=Text("Ola, pronto para o proximo passo na sua aplicacao, atualize e mantem te sempre fresco."),
        actions=[
            TextButton("Atualizar agora", on_click=atualizar),
            TextButton("Atualizar mais tarde", on_click=lembrar_mais_tarde),
            TextButton("Cancelar", on_click=cancelar)
        ]
    )
    
    def abrir_banner(e):
        page.banner.open = True
        page.update()
    
    page.add(
        Text('Ola mundo!'),
        ElevatedButton('Executar', on_click=abrir_banner)
    )

app(target=main)