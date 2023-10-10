import flet
from flet import Page, Text, ElevatedButton, Row

def main(page: Page):
    page.title = "Calculator APP"
    result = Text(value="0")
    page.add(
        Row(controls=[result]),
        Row(
            controls=[

            ]
        )

        ElevatedButton("7"),
        ElevatedButton("8"),
        ElevatedButton("9"),
        ElevatedButton("*"),
        ElevatedButton("4"),
        ElevatedButton("5"),
        ElevatedButton("6"),
        ElevatedButton("-"),
        ElevatedButton("1"),
        ElevatedButton("2"),
        ElevatedButton("3"),
        ElevatedButton("+"),
        ElevatedButton("0"),
        ElevatedButton("."),
        ElevatedButton("="),
    )
    page.add(Text(value="Calc"))


flet.app(target=main)