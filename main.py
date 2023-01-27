from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication([])
main = QWidget()
main.setWindowTitle('Какое-то приложение')
main.move(900, 300)
main.resize(600, 600)
main.show()

line = QHBoxLayout()
text = QLabel('Ты что здесь делаешь?')
line.addWidget(text, aligment=Qt.AlignCenter)
main.setLayout(line)
app.exec_()