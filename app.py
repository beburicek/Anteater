from model_chat import chat
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,QLineEdit,QPushButton, QTextEdit
from PySide6.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Anteater')
        
        container=QWidget()
        layout=QVBoxLayout()
        layout.addWidget(QTextEdit())
        layout.addWidget(QPushButton("Click me"))
        
        container.setLayout(layout)
        self.setCentralWidget(container)
        
app=QApplication()
window= MainWindow()
window.show()
app.exec()