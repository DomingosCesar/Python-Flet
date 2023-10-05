from flet import *

def main(page : Page):
    page.title = "Sistema de Rotas"
    
    def mudanca_rotas(route):
        page.views.clear()
        page.views.append(
        View(
            "/",
            [
                AppBar(title=Text("Flet Ap"), bgcolor=colors.SURFACE_VARIANT),
                ElevatedButton("Visite a Loja", on_click=lambda _: page.go('/loja'))
            ]
        )
            )
        if page.route == "/loja":
            page.views.append(
                View(
                    "/loja",
                    
                    [
                        AppBar(title=Text("Loja"), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                        TextField(label = "Digite o seu nome"),
                        ElevatedButton("Send", on_click=say_hi)
                    ]
                )
            )
        page.update()
    
    def say_hi(e):
        print("Hello World!")
        
    def view_Pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    
    page.on_route_change = mudanca_rotas
    page.on_view_pop = view_Pop
    page.go(page.route)

app(target=main, view=WEB_BROWSER)