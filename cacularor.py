from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle("Калькулятор")
window.resize(700,600)

#Створення віджетів
text = QLabel("1234567890")
btn1 = QPushButton("1")
btn2 = QPushButton("2")
btn3 = QPushButton("3")
btn4 = QPushButton("4")
btn5 = QPushButton("5")
btn6 = QPushButton("6")
btn7 = QPushButton("7")
btn8 = QPushButton("8")
btn9 = QPushButton("9")
btn0 = QPushButton("0")
btn_point = QPushButton(".")

f_btn_ac = QPushButton("AC")
f_btn_cancel = QPushButton("◄")
f_btn_minus = QPushButton("-")
f_btn_plus = QPushButton("+")
f_btn_dorivnuye = QPushButton("=")
f_btn_mnozheniya = QPushButton("x")
f_btn_dileniya = QPushButton("/")

#Розташування віджетів
horizontal_line1 = QHBoxLayout()
horizontal_line1.addWidget(f_btn_ac)
horizontal_line1.addWidget(f_btn_cancel)
horizontal_line1.addWidget(f_btn_mnozheniya)

horizontal_line2 = QHBoxLayout()
horizontal_line2.addWidget(btn7)
horizontal_line2.addWidget(btn8)
horizontal_line2.addWidget(btn9)
horizontal_line2.addWidget(f_btn_dileniya)

horizontal_line3 = QHBoxLayout()
horizontal_line3.addWidget(btn4)
horizontal_line3.addWidget(btn5)
horizontal_line3.addWidget(btn6)
horizontal_line3.addWidget(f_btn_plus)

horizontal_line4 = QHBoxLayout()
horizontal_line4.addWidget(btn1)
horizontal_line4.addWidget(btn2)
horizontal_line4.addWidget(btn3)
horizontal_line4.addWidget(f_btn_minus)

horizontal_line5 = QHBoxLayout()
horizontal_line5.addWidget(btn_point)
horizontal_line5.addWidget(btn0)
horizontal_line5.addWidget(f_btn_dorivnuye)


vertical_line = QVBoxLayout()
vertical_line.addWidget(text)
vertical_line.addLayout(horizontal_line1)
vertical_line.addLayout(horizontal_line2)
vertical_line.addLayout(horizontal_line3)
vertical_line.addLayout(horizontal_line4)
vertical_line.addLayout(horizontal_line5)


window.setLayout(vertical_line)




window.show()
app.exec_()