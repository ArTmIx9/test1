from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle("Randomaiser")
window.resize(700,600)

#Створення віджетів
text1 = QLabel("Натисни щобдізнатися переможця")
text2 = QLabel("?")
button = QPushButton("Нитисни щоб згенерувати число")

#Роташування віджетів
vline = QVBoxLayout()
vline.addWidget(text1, alignment=Qt.AlignCenter)
vline.addWidget(text2, alignment=Qt.AlignCenter)
vline.addWidget(button, alignment=Qt.AlignCenter)
window.setLayout(vline)

window.show()
app.exec_()