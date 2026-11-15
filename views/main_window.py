from PySide6.QtCore import Qt
from qframelesswindow import FramelessMainWindow
from ui_mainwindow import Ui_MainWindow
from widgets import MyTitleBar

class MainWindow(FramelessMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # кастомный заголовок
        self.setTitleBar(MyTitleBar(self))
        self.titleBar.raise_()

        # сигналы
        self.titleBar.pin_btn.clicked.connect(self.toggle_pin)

    def toggle_pin(self, checked: bool): # закрепление окна поверх
        self.setWindowFlag(Qt.WindowStaysOnTopHint, checked)
        self.show()
