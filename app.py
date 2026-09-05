import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QVBoxLayout, QLineEdit, QPushButton, QTextEdit
)
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QTextCursor
from model_chat import AnteaterChat


class WorkerThread(QThread):
    token_received = Signal(str)
    finished_signal = Signal()

    def __init__(self, chat_engine, user_text):
        super().__init__()
        self.chat_engine = chat_engine
        self.user_text = user_text

    def run(self):
        for token in self.chat_engine.send_message_stream(self.user_text):
            self.token_received.emit(token)
        self.finished_signal.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Anteater')
        self.resize(500, 500)

        self.chat_engine = AnteaterChat()

        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("Napíš správu pre Anteater...")
        self.button = QPushButton("Submit")

        layout = QVBoxLayout()
        layout.addWidget(self.chat_history)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.button.clicked.connect(self.on_submit)
        self.input.returnPressed.connect(self.on_submit)

    def on_submit(self):
        text = self.input.text().strip()
        if not text:
            return

        self.chat_history.append(f"<b>Ty:</b> {text}")
        self.chat_history.append("<b>Anteater:</b> ")
        
        self.input.clear()
        self.button.setEnabled(False)
        
        self.worker = WorkerThread(self.chat_engine, text)
        self.worker.token_received.connect(self.append_token)
        self.worker.finished_signal.connect(self.on_finished)
        self.worker.start()

    def append_token(self, token):
        
        cursor = self.chat_history.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)  
        cursor.insertText(token)
        self.chat_history.setTextCursor(cursor)

    def on_finished(self):
        
        self.chat_history.append("\n")
        self.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())