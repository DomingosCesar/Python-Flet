from flet import *

def main(page : Page):
    page.add(
        Text(f"Rota Inicial: {page.route}")
    )
    
    def nova_rota(route):
        page.add(Text(f"Nova rota: {route}"))
        
    def rota_compra(e):
        page.route = "/compras"
        page.update()
        
    page.on_route_change = nova_rota
    page.add(ElevatedButton("Ir para compras", on_click=rota_compra))
    page.update()

app(target=main, view=WEB_BROWSER)