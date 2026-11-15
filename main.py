# pip install pyside6
# pip install PySideSix-Frameless-Window

'''
translator/
├── main.py                 # Точка входа (QApplication, запуск MainWindow)
├── mainwindow.ui           # Исходный дизайн (Qt Designer)
├── ui_mainwindow.py        # Сгенерированный из .ui (pyside6-uic)
├── mainwindow.py          # Контроллер главного окна (наследует FramelessMainWindow)
├── titlebar.py             # Кастомный заголовок (MyTitleBar)
├── settings_window.py      # Заготовка для окна настроек (позже)
└── logic/                  # Бизнес-логика
    └── actions.py          # Функции перевода, не зависящие от UI
'''

import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
