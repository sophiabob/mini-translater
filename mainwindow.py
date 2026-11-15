# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.ui = Ui_MainWindow()   # <-- эта строка создаёт атрибут ui
        self.ui.setupUi(self)       # <-- эта строка применяет виджеты к окну

'''
        # Подключаем кнопку к функции
        self.ui.translateButton.clicked.connect(self.on_translate)

    def on_translate(self):
        print("Кнопка нажата — здесь будет логика перевода")
        '''


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
