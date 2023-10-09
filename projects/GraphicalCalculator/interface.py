from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from logica import evaluate_expression, reset_lists


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 400, 200)
        self.expression = ""
        self.result = QLineEdit(self)
        self.result.setAlignment(Qt.AlignRight)
        self.result.setPlaceholderText("0")
        self.result.setFont(QFont("Arial", 24))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.result)

        self.buttons = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "←"],
            ["1", "2", "3", "-", "^"],
            ["0", ".", "=", "+"]
        ]

        button_grid = QGridLayout()
        button_grid.setHorizontalSpacing(6)
        button_grid.setVerticalSpacing(6)

        for i, row_buttons in enumerate(self.buttons):
            for j, button_text in enumerate(row_buttons):
                button = QPushButton(button_text)
                if button_text.isnumeric():
                    self.style_button(button, "number")
                elif button_text in "+-*/^":
                    self.style_button(button, "operator")
                else:
                    self.style_button(button, "other")
                button.setFixedHeight(50)
                button.setFont(QFont("Arial", 18))
                button.clicked.connect(self.button_click)
                button_grid.addWidget(button, i, j)
        self.layout.addLayout(button_grid)
        self.setLayout(self.layout)

    def style_button(self, button, button_type):
        if button_type == "number":
            button.setStyleSheet(
                "QPushButton { background-color: #3498DB; color: white; border: none; border-radius: 5px; }"
                "QPushButton:hover { background-color: #2980B9; }"
            )
        elif button_type == "operator":
            button.setStyleSheet(
                "QPushButton { background-color: #E74C3C; color: white; border: none; border-radius: 5px; }"
                "QPushButton:hover { background-color: #C0392B; }"
            )
        else:
            button.setStyleSheet(
                "QPushButton { background-color: #95A5A6; color: white; border: none; border-radius: 5px; }"
                "QPushButton:hover { background-color: #7F8C8D; }"
            )

    def button_click(self):
        button = self.sender()
        text = button.text()
        if text == "=":
            try:
                if self.expression[-1] in "+-*/^":
                    raise Exception("Expressão inválida")

                result = evaluate_expression(self.expression)
                self.result.setText(str(result))
                self.expression = str(result)
            except Exception as e:
                self.result.setText("Erro")
                self.expression = ""
        elif text == "C":
            self.expression = ""
            self.result.setText("0")
            reset_lists()
        elif text == "←":
            self.expression = self.expression[:-1]
            self.result.setText(self.expression)
        elif text == "^":
            self.expression += "^"
            self.result.setText(self.expression)
        else:
            if text in "+-*/^" and self.expression and self.expression[-1] in "+-*/^":
                return
            self.expression += text
            self.result.setText(self.expression)
