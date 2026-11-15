from PySide6.QtWidgets import QPushButton
from qframelesswindow import StandardTitleBar

class MyTitleBar(StandardTitleBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # скрепка - исправить
        self.pin_btn = QPushButton("📎", self)
        self.pin_btn.setFixedSize(30, 30)
        self.pin_btn.setCheckable(True)
        self.pin_btn.setToolTip("Закрепить поверх окон")

        self.hBoxLayout.insertWidget(1, self.pin_btn)
