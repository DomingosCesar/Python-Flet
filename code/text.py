import flet as ft

def main(page: ft.Page):
    page.title = "Text custom styles"
    page.scroll = "adaptive"
    
    page.add(
        ft.Text("Size 10", size=10),
        ft.Text("Size 30, Italic", size=30, color="pink600", italic=True),
        ft.Text(
            "Size 40, w100", size=40, color= ft.colors.WHITE,
            bgcolor= ft.colors.BLUE_600, weight=ft.FontWeight.W_100,
        ),
        ft.Text(
            "Size 50, Normal", size=50, color=ft.colors.WHITE,
            bgcolor=ft.colors.ORANGE_800,
            weight=ft.FontWeight.NORMAL,
        ),
        ft.Text(
            "Size 60, Bold, Italic", size=60,
            color=ft.colors.WHITE, bgcolor=ft.colors.GREEN_700,
            weight=ft.FontWeight.BOLD, italic=True,
        ),
        ft.Text("Size 70, w900, selectable", size=70,
            weight=ft.FontWeight.W_900, selectable=True,        
        ),
        ft.Text(
            "Limite Long text to 1 line with ellipsis",
            style=ft.TextThemeStyle.HEADLINE_SMALL
        ),
        ft.Text(
            "Proin rutrum, purus sit amet elementum volutpat, nunc lacus vulputate orci, cursus ultrices neque dui quis purus. Ut ultricies purus nec nibh bibendum, eget vestibulum metus varius. Duis convallis maximus justo, eu rutrum libero maximus id. Donec ullamcorper arcu in sapien molestie, non pellentesque tellus pellentesque. Nulla nec tristique ex. Maecenas euismod nisl enim, a convallis arcu laoreet at. Ut at tortor finibus, rutrum massa sit amet, pulvinar velit. Phasellus diam lorem, viverra vitae leo vitae, consequat suscipit lorem.",
            max_lines=1, overflow="ellipsis",
            ),
        ft.Text("Limit long text to 2 lines and fading", style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.",
            max_lines=2,
            ),
        ft.Text("Limit the width and height of long text", style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.",width=700,
            height=100,
            ),
    )
    
def main2(page : ft.Page):
    page.title = "Text theme styles" 
    page.scroll = "adaptive"
    page.add(
    ft.Text("Display Large",
    style=ft.TextThemeStyle.DISPLAY_LARGE), ft.Text("Display Medium",
    style=ft.TextThemeStyle.DISPLAY_MEDIUM), ft.Text("Display Small",
    style=ft.TextThemeStyle.DISPLAY_SMALL), ft.Text("Headline Large",
    style=ft.TextThemeStyle.HEADLINE_LARGE), ft.Text("Headline Medium",
    style=ft.TextThemeStyle.HEADLINE_MEDIUM), ft.Text("Headline Small", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
    ft.Text("Title Large", style=ft.TextThemeStyle.TITLE_LARGE), ft.Text("Title Medium", style=ft.TextThemeStyle.TITLE_MEDIUM), ft.Text("Title Small", style=ft.TextThemeStyle.TITLE_SMALL), ft.Text("Label Large", style=ft.TextThemeStyle.LABEL_LARGE), ft.Text("Label Medium", style=ft.TextThemeStyle.LABEL_MEDIUM), ft.Text("Label Small", style=ft.TextThemeStyle.LABEL_SMALL), ft.Text("Body Large", style=ft.TextThemeStyle.BODY_LARGE), ft.Text("Body Medium", style=ft.TextThemeStyle.BODY_MEDIUM), ft.Text("Body Small", style=ft.TextThemeStyle.BODY_SMALL),
    )

   
def main3(page: ft.Page):
        # page.fonts = {
        # "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bw"
        # }

        t = ft.Text(
            "This is rendered with Roboto Slab", size=30,
            font_family="RobotoSlab", weight=ft.FontWeight.W_100,
        )
        def width_changed(e):
            t.weight = f"w{int(e.control.value)}" 
            t.update()
        page.add( t,
            ft.Slider( min=100,
            max=900,
            divisions=8, label="{value}", width=500, on_change=width_changed,
            ), 
        )

   
def main4(page: ft.Page):
    page.add(
        ft.Text("Plain text with default style"), 
        ft.Text( "Some text",
            size=30,
            spans=[
                    ft.TextSpan("here goes italic",
                        ft.TextStyle(italic=True, size=20, color=ft.colors.GREEN),
                        spans=[ 
                            ft.TextSpan(
                            "bold and italic", 
                                ft.TextStyle(weight=ft.FontWeight.BOLD), ),
                            ft.TextSpan("just italic",
                                        spans=[
                                            ft.TextSpan("smaller italic",ft.TextStyle(size=15))],
                                    ),   
                            ], 
                        ) 
                    ], 
            ),
        ft.Text( 
            disabled=False,
            spans=[ 
                   ft.TextSpan(
                       "underlined and clickable",
                       ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                       on_click=lambda e: print(f"Clicked span: {e.control.uid}"),
                       on_enter=lambda e: print(f"Entered span: {e.control.uid}"),
                       on_exit=lambda e: print(f"Exited span: {e.control.uid}"),
                       ),
                       ft.TextSpan(" "), 
                       ft.TextSpan("underlined red wavy", 
                            ft.TextStyle(
                                decoration=ft.TextDecoration.UNDERLINE, decoration_color=ft.colors.RED, decoration_style=ft.TextDecorationStyle.WAVY,),
                         on_enter=lambda e: print(f"Entered span: {e.control.uid}"),
                         on_exit=lambda e: print(f"Exited span: {e.control.uid}"),
                         ),
                        ft.TextSpan(" "), 
                        ft.TextSpan("overlined blue", 
                            ft.TextStyle(decoration=ft.TextDecoration.OVERLINE, decoration_color="blue"),
                        ),
                
                ft.TextSpan(" "), 
                ft.TextSpan(
                    "overlined and underlined", 
                    ft.TextStyle(decoration=ft.TextDecoration.OVERLINE | ft.TextDecoration.UNDERLINE ),),
                ft.TextSpan(" "), 
                ft.TextSpan("line through thick", 
                            ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH,decoration_thickness=3, ),
                            ), 
                ],), )
    
    def highlight_link(e): 
        e.control.style.color = ft.colors.BLUE 
        e.control.update()
    def unhighlight_link(e): 
        e.control.style.color = None 
        e.control.update()

    page.add( ft.Text(
            disabled=False,
            spans=[
                ft.TextSpan("AwesomeApp 1.0 "), 
                ft.TextSpan(
                    "Visit our website", 
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://google.com",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link, ),
                ft.TextSpan(" All rights reserved. "), 
                ft.TextSpan(
                    "Documentation", 
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://google.com",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link, ),
                ],
            ),
        )
    
# ft.app(main)                       
   
ft.app(target=main3)