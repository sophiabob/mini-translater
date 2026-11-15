# pip install pyside6
# pip install PySideSix-Frameless-Window

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from ui_mainwindow import Ui_MainWindow

from qframelesswindow import FramelessMainWindow, StandardTitleBar # для кастомного статус бара
from PySide6.QtCore import Qt


class MyTitleBar(StandardTitleBar):
    def __init__(self, parent):
        super().__init__(parent)

        # скрепка
        self.pin_btn = QPushButton("📎", self)
        self.pin_btn.setFixedSize(30, 30)
        self.pin_btn.setCheckable(True)  # Чтобы кнопка «залипала» при нажатии
        self.hBoxLayout.insertWidget(1, self.pin_btn)


class MainWindow(FramelessMainWindow):
        def __init__(self, parent=None):
                super().__init__(parent)

                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)

                # кастомный заголовок
                self.setTitleBar(MyTitleBar(self))
                self.titleBar.raise_()

                # кнопка
                self.titleBar.pin_btn.clicked.connect(self.toggle_pin)

        def toggle_pin(self, checked):
                if checked:
                        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
                else:
                        self.setWindowFlag(Qt.WindowStaysOnTopHint, False)
                self.show()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
