from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
import sys

from LoginWindow import Ui_MainWindow
from sqlConnection import Connection
from encryption import Password_Hash
class MainWindow:
    def __init__(self):
        self.Sql = Connection()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

        self.ui.LoginBtn.clicked.connect(self.loginpg)
        self.ui.SingupBtn.clicked.connect(self.signpg)
        self.ui.backBtn.clicked.connect(self.backBtn)
        self.ui.pushButton.clicked.connect(self.backBtn)
        self.ui.singUpBtn.clicked.connect(self.userReg)
    def show(self):
        self.main_win.show()
        self.Sql.connection()
    def loginpg(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Login)
    
    def signpg(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.singup)
    def backBtn(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)
    def show_dialog(self,text):
        dialog  = QMessageBox()
        dialog.setText(text)
        dialog.setWindowTitle("Warning")
        dialog.setIcon(QMessageBox.Warning)
        dialog.exec_()
    def show_dialog2(self,text):
        dialog  = QMessageBox()
        dialog.setText(text)
        dialog.setWindowTitle("Info")
        dialog.setIcon(QMessageBox.Information)
        dialog.exec_()
    def userReg(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        conf_password = self.ui.lineEdit_3.text()
        user_exists = False
        if not username:
           self.show_dialog("Please choose your username")
        elif len(username) > 16:
            self.show_dialog("Username cannot be more than 16 characters long")
        elif not password:
            self.show_dialog("Please choose your password")
        elif password != conf_password or not conf_password:
            self.show_dialog("Please confirm your password")
        else:
            query = "Insert into login values(%s,%s)"
            hash = Password_Hash.encrypt(password)
            values = username,hash
            sql_data = self.Sql.fetch_all()
            for data in sql_data:
                if data[0] == username:
                    user_exists = True
                    break
            if user_exists:
                self.show_dialog("Username Exists")
            else:
                self.Sql.insert_data(query,values)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())