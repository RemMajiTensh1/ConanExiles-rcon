import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from qt_material import apply_stylesheet
from ConRcon import ConanExilesRCON

#Form, Window = uic.loadUiType("interface.ui")

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi("interface.ui", self)
        self.setFixedSize(961, 685)
        self.load_theme()


        # dark themes
        self.actionDark_Red_2.triggered.connect(self.dark_red)
        self.actionDark_Blue_2.triggered.connect(self.dark_blue)
        self.actionDark_Yellow_2.triggered.connect(self.dark_yellow)
        self.actionDark_Cyan_2.triggered.connect(self.dark_cyan)
        self.actionDark_Amber_2.triggered.connect(self.dark_amber)
        self.actionDark_Lightgreen_2.triggered.connect(self.dark_lightgreen)
        self.actionDark_Pink_2.triggered.connect(self.dark_pink)
        self.actionDark_Purple_2.triggered.connect(self.dark_purple)
        self.actionDark_Teal_2.triggered.connect(self.dark_teal)

        # light themes
        self.actionLight_Red.triggered.connect(self.light_red)
        self.actionLight_Orange.triggered.connect(self.light_red_500)
        self.actionLight_Blue.triggered.connect(self.light_blue)
        self.actionLight_Turquoise.triggered.connect(self.light_blue_500)
        self.actionLight_Cyan.triggered.connect(self.light_cyan)
        self.actionLight_Diamond.triggered.connect(self.light_cyan_500)
        self.actionLight_Yellow_2.triggered.connect(self.light_yellow)
        self.actionLight_Lightgereen.triggered.connect(self.light_lightgreen)
        self.actionLight_Lime.triggered.connect(self.light_lightgreen_500)
        self.actionLight_Pink.triggered.connect(self.light_pink)
        self.actionLight_Crimson.triggered.connect(self.light_pink_500)
        self.actionLight_Purple.triggered.connect(self.light_purple)
        self.actionLight_Violet.triggered.connect(self.light_purple_500)
        self.actionLight_Amber.triggered.connect(self.light_amber)
        self.actionLight_Teal.triggered.connect(self.light_teal)
        self.actionLight_Sea.triggered.connect(self.light_teal_500)

        #button
        self.ClikBut.clicked.connect(self.ClickOnbut)
        self.pushButton1.clicked.connect(self.List)
        self.conButton.clicked.connect(self.con_rcon)
        self.saveButton.clicked.connect(self.SaveConf)
        self.MessButton_2.clicked.connect(self.BroadMess)
        self.Mess3.clicked.connect(self.CommandAdm)
        self.KickButton.clicked.connect(self.Kick)
        self.BanButton_2.clicked.connect(self.Ban)
        self.BanListButton.clicked.connect(self.BanLi)
        self.UnBanButton_4.clicked.connect(self.UnBn)
        self.checkBox.stateChanged.connect(self.listauto)

        self.rcon = None
        self.update_timer = QTimer(self)
        self.update_timer.setInterval(30000)  # 30 sec auto update playerlist
        self.update_timer.timeout.connect(self.List)


        self.load_config()

    def load_config(self):
        if os.path.exists("config.ini"):
            self.plainTextEditConsole.setPlainText("Конфиг найден")
            with open('config.ini') as f:
                lines = f.readlines()
                if len(lines) >= 3:
                    a = lines[0].strip()
                    b = lines[1].strip()
                    r = lines[2].strip()
                    self.rcon = ConanExilesRCON(host=a, port=int(r), password=b)
                else:
                    self.plainTextEditConsole.setPlainText("Конфиг содержит неправильное количество строк.")
        else:
            self.plainTextEditConsole.setPlainText("Конфиг не найден, создаю новый.")
            with open("config.ini", "w+") as conf:
                conf.write("(ip)\n(pass)\n(7778)")

    def dark_red(self):
        apply_stylesheet(app, theme='dark_red.xml')
        self.save_theme("dark_red")
    def dark_blue(self):
        apply_stylesheet(app, theme='dark_blue.xml')
        self.save_theme("dark_blue")
    def dark_yellow(self):
        apply_stylesheet(app, theme='dark_yellow.xml')
        self.save_theme("dark_yellow")

    def dark_cyan(self):
        apply_stylesheet(app, theme='dark_cyan.xml')
        self.save_theme("dark_cyan")
    def dark_amber(self):
        apply_stylesheet(app, theme='dark_amber.xml')
        self.save_theme("dark_amber")
    def dark_lightgreen(self):
        apply_stylesheet(app, theme='dark_lightgreen.xml')
        self.save_theme("dark_lightgreen")
    def dark_pink(self):
        apply_stylesheet(app, theme='dark_pink.xml')
        self.save_theme("dark_pink")
    def dark_purple(self):
        apply_stylesheet(app, theme='dark_purple.xml')
        self.save_theme("dark_purple")
    def dark_teal(self):
        apply_stylesheet(app, theme='dark_teal.xml')
        self.save_theme("dark_teal")

#LIGHT THEMES---------------------------------------------------------------------------------
    def light_red(self):
        apply_stylesheet(app, theme='light_red.xml')
        self.save_theme("light_red")
    def light_red_500(self):
        apply_stylesheet(app, theme='light_red_500.xml')
        self.save_theme("light_red_500")
    def light_blue(self):
        apply_stylesheet(app, theme='light_blue.xml')
        self.save_theme("light_blue")
    def light_blue_500(self):
        apply_stylesheet(app, theme='light_blue_500.xml')
        self.save_theme("light_blue_500")
    def light_cyan(self):
        apply_stylesheet(app, theme='light_cyan.xml')
        self.save_theme("light_cyan")
    def light_cyan_500(self):
        apply_stylesheet(app, theme='light_cyan_500.xml')
        self.save_theme("light_cyan_500")
    def light_yellow(self):
        apply_stylesheet(app, theme='light_yellow.xml')
        self.save_theme("light_yellow")
    def light_lightgreen(self):
        apply_stylesheet(app, theme='light_lightgreen.xml')
        self.save_theme("light_lightgreen")
    def light_lightgreen_500(self):
        apply_stylesheet(app, theme='light_lightgreen_500.xml')
        self.save_theme("light_lightgreen_500")
    def light_pink(self):
        apply_stylesheet(app, theme='light_pink.xml')
        self.save_theme("light_pink")
    def light_pink_500(self):
        apply_stylesheet(app, theme='light_pink_500.xml')
        self.save_theme("light_pink_500")
    def light_purple(self):
        apply_stylesheet(app, theme='light_purple.xml')
        self.save_theme("light_purple")
    def light_purple_500(self):
        apply_stylesheet(app, theme='light_purple_500.xml')
        self.save_theme("light_purple_500")
    def light_amber(self):
        apply_stylesheet(app, theme='light_amber.xml')
        self.save_theme("light_amber")
    def light_teal(self):
        apply_stylesheet(app, theme='light_teal.xml')
        self.save_theme("light_teal")
    def light_teal_500(self):
        apply_stylesheet(app, theme='light_teal_500.xml')
        self.save_theme("light_teal_500")



    def save_theme(self, theme_name):
        with open("theme_config.ini", "w") as theme_file:
            theme_file.write(f"theme={theme_name}\n")

    def load_theme(self):
        if os.path.exists("theme_config.ini"):
            with open("theme_config.ini", "r") as theme_file:
                for line in theme_file:
                    if line.startswith("theme="):
                        theme_name = line.split("=")[1].strip()
                        # Применяем загруженную тему
                        apply_stylesheet(app, theme=f"{theme_name}.xml")
                        self.plainTextEditConsole.setPlainText(f"Тема {theme_name} загружена")
        else:
            # Если файла нет, применяем тему по умолчанию и создаём файл с темой по умолчанию
            apply_stylesheet(app, theme="dark_cyan.xml")
            self.save_theme("dark_cyan")
    def con_rcon(self):
        if self.rcon:
            try:
                self.rcon.connect()
                if self.rcon.socket is None:
                    self.plainTextEditConsole.setPlainText("Не удалось авторизоваться. Проверьте пароль и настройки.")
                else:
                    self.plainTextEditConsole.setPlainText("Соединение с сервером установлено! help для помощи")
            except Exception as e:
                self.plainTextEditConsole.setPlainText(f"Ошибка при подключении: {e}")

    def SaveConf(self):
        ip = self.ip_edit.text()
        pas = self.Pass_Edit.text()
        por = self.Port_Edit.text()
        with open("config.ini", "w+") as conf:
            conf.write(f"{ip}\n{pas}\n{por}")
        self.plainTextEditConsole.setPlainText("Конфиг изменен")

    def ClickOnbut(self):
        if self.rcon:
            resul = self.rcon.command(self.lineEditCmd.text())
            self.plainTextEditConsole.setPlainText(str(resul))
        else:
            self.plainTextEditConsole.setPlainText("RCON не настроен.")

    def List(self):
        if self.rcon:
            result = self.rcon.command("listplayers")
            self.plainTextEdit.setPlainText(str(result))
        else:
            self.plainTextEditConsole.setPlainText("RCON не настроен.")

    def Kick(self):
        if self.rcon:
            KickPlay = f"KickPlayer platformid {self.IdxEdit.text()} {self.IdxEdit_2.text()}"
            self.rcon.command(KickPlay)
            self.plainTextEditConsole.setPlainText(str(KickPlay))
        else:
            self.plainTextEditConsole.setPlainText("RCON не настроен.")

    def Ban(self):
        if self.rcon:
            BanPlay = f"BanPlayer platformid {self.IdxEdit.text()} {self.IdxEdit_2.text()}"
            self.rcon.command(BanPlay)
            self.plainTextEditConsole.setPlainText(str(BanPlay))
            with open("banlist.txt", "a") as file:
                file.write(f"{self.IdxEdit.text()} {self.IdxEdit_2.text()}\n")
        else:
            self.plainTextEditConsole.setPlainText("RCON не настроен.")

    def BanLi(self):
        if self.rcon:
            BnLi = "listbans"
            BnList = self.rcon.command(BnLi)
            self.plainTextEditConsole.setPlainText(str(BnList))
        else:
            self.plainTextEditConsole.setPlainText("RCON не настроен.")

    def UnBn(self):
        if self.rcon:
            UnB = f"UnbanPlayer {self.IdxEdit.text()}"
            self.rcon.command(UnB)
            self.plainTextEditConsole.setPlainText(str(UnB))

            # Удаление из бан-листа
            keyword_to_delete = self.IdxEdit.text()
            with open("banlist.txt", "r") as f:
                lines = f.readlines()

            with open("banlist.txt", "w") as f:
                for line in lines:
                    if keyword_to_delete not in line:
                        f.write(line)
        else:
            self.plainTextEditConsole.setPlainText("RCON не настроен.")

    def listauto(self, state):
        if state == 2:
            self.plainTextEditConsole.setPlainText("Автообновление включено")
            self.update_timer.start()
        else:
            self.plainTextEditConsole.setPlainText("Автообновление выключено")
            self.update_timer.stop()

    def BroadMess(self):
        if self.rcon:
            Broad = f"broadcast {self.MesslineEdit.text()}"
            self.rcon.command(Broad)
        else:
            self.plainTextEditConsole.setPlainText("RCON не настроен.")
            self.plainTextEditConsole.repaint()
    def CommandAdm(self):
        if self.rcon:
            idplay = f"con {self.IdxEdit.text()}{self.comboBox.currentText()} {self.IdxEdit_2.text()}"
            self.rcon.command(idplay)
            self.plainTextEditConsole.setPlainText(str(idplay))
        else:
            self.plainTextEditConsole.setPlainText("RCON не настроен.")
            self.plainTextEditConsole.repaint()

app = QApplication(sys.argv)
ui = MainUI()
ui.show()
sys.exit(app.exec_())
