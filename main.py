import flet as ft
from clock import ChessClock
from config import INITIAL_TIME


def main(page: ft.Page):
    page.title = "Reloj de Ajedrez"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Crear instancia del reloj de ajedrez
    chess_clock = ChessClock(INITIAL_TIME)

    # Definir los botones para cada reloj
    player1_button = ft.TextButton(
        text=chess_clock.format_time(chess_clock.player1_time),
        on_click=lambda _: chess_clock.switch_clock(1),
    )
    player2_button = ft.TextButton(
        text=chess_clock.format_time(chess_clock.player2_time),
        on_click=lambda _: chess_clock.switch_clock(2),
    )

    # Área intermedia para resetear y cambiar opciones
    reset_button = ft.TextButton(
        text="Reset", on_click=lambda _: chess_clock.reset_clocks()
    )

    # Actualizar el tiempo de los botones
    def update_clocks():
        player1_button.text = chess_clock.format_time(chess_clock.player1_time)
        player2_button.text = chess_clock.format_time(chess_clock.player2_time)
        page.update()

    chess_clock.on_update = update_clocks

    # Disposición de los botones en la página
    page.add(ft.Row(controls=[player1_button, player2_button]), reset_button)


ft.app(target=main)
