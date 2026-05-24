import flet as ft
import os
def main(page: ft.Page):
    page.title = "Hola"
    txt = ft.Text(value="Hola MI AMOR TE AMO MUCHO")
    page.controls.append(txt)
    page.update()
ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000))
)
