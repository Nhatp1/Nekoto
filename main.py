from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore, QtGui, QtWidgets
from login_form import LoginWindow
from mainwindow import MainWindow
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    # login_window = LoginWindow(parent=main_window)
    # login_window.login_confirmed = False
    # login_window.show()
    # app.setWindowIcon(QtGui.QIcon('image/logo.ico'))
    # app.exec()
    # if getattr(login_window, "login_confirmed", False):
    #     main_window.show()
    #     sys.exit(app.exec())
    # else:
    #     sys.exit(0)
    main_window.show()
    sys.exit(app.exec())
# pyinstaller --onefile --noconsole --icon=logo.ico --add-data "C:/Users/DELL/AppData/Local/Programs/Python/Python313/Lib/site-packages/uiautomator2/assets;uiautomator2/assets" main.py
