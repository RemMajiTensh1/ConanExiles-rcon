from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from ConRcon import ConanExilesRCON
import os

Form, Window = uic.loadUiType("interface.ui")

app = QApplication([])
window = Window()
window.setFixedSize(762, 603)
form = Form()
form.setupUi(window)
window.show()

auto_update_active = False

if os.path.exists("config.ini"):
    form.plainTextEditConsole.setPlainText(str("Конфиг найден"))
    conf = open('config.ini', "r")
    conf.close()
    with open('config.ini') as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                a = line
            elif i == 1:
                b = line
            elif i == 2:
                r = line
    rcon = ConanExilesRCON(host=a, port=int(r), password=b)
else:
    form.plainTextEditConsole.setPlainText(str("Конфиг не найден"))
    conf = open("config.ini", "w+")
    confin = f"(ip)\n(pass)\n(7778)"
    conf.write(str(confin))
    conf.close()


update_timer = QTimer()

# Интервал таймера 30 секунд
update_timer.setInterval(30000)

def SaveConf():
    conf = open("config.ini", "w+")
    ip = form.ip_edit.text()
    pas = form.Pass_Edit.text()
    por = form.Port_Edit.text()
    confin = f"{ip}\n{pas}\n{por}"
    conf.write(str(confin))
    form.plainTextEditConsole.setPlainText(str("Конфиг изменен"))

def con_rcon():
    rcon.connect()
    if rcon.socket == None:
        form.plainTextEditConsole.setPlainText(str("Не удалось авторизоваться. Проверьте пароль и настройки."))
    else:
        form.plainTextEditConsole.setPlainText(str("Подключение выполнено! help для помощи"))

def List():
    her = str("listplayers")
    result = rcon.command(her)
    form.plainTextEdit.setPlainText(str(result))
    print(result)

# Функция для управления таймером
def listauto(state):
    if state == 2:
        form.plainTextEditConsole.setPlainText(str("Автообновление включено"))
        print("Автообновление включено")
        update_timer.start()
    else:
        form.plainTextEditConsole.setPlainText(str("Автообновление выключено"))
        print("Автообновление выключено")
        update_timer.stop()


def ClickOnbut():
    resul = rcon.command(str(form.lineEditCmd.text()))
    form.plainTextEditConsole.setPlainText(str(resul))

def BroadMess():
    Broad = str(f"broadcast {form.MesslineEdit.text()}")
    rcon.command(Broad)

def CommandAdm():
    idplay = str(f"con {form.IdxEdit.text()}{form.comboBox.currentText()} {form.IdxEdit_2.text()}")
    rcon.command(idplay)
    form.plainTextEditConsole.setPlainText(str(idplay))

def Kick():
    KickPlay = str(f"KickPlayer platformid {form.IdxEdit.text()} {form.IdxEdit_2.text()}")
    rcon.command(KickPlay)
    form.plainTextEditConsole.setPlainText(str(KickPlay))

def Ban():
    BanPlay = str(f"BanPlayer platformid {form.IdxEdit.text()} {form.IdxEdit_2.text()}")
    rcon.command(BanPlay)
    form.plainTextEditConsole.setPlainText(str(BanPlay))
    if not os.path.exists("banlist.txt"):
        with open("banlist.txt", "w") as file:
            file.write(f"{form.IdxEdit.text()} {form.IdxEdit_2.text()}\n")
    else:
        with open("banlist.txt", "a") as file:
            file.write(f"{form.IdxEdit.text()} {form.IdxEdit_2.text()}\n")

def BanLi():
    BnLi = str("listbans")
    BnList = rcon.command(BnLi)
    form.plainTextEditConsole.setPlainText(str(BnList))

def UnBn():
    UnB = str(f"UnbanPlayer {form.IdxEdit.text()}")
    rcon.command(UnB)
    form.plainTextEditConsole.setPlainText(str(UnB))
    keyword_to_delete = form.IdxEdit.text()
    file_path = "banlist.txt"

    with open(file_path, "r") as f:
        lines = f.readlines()

    with open(file_path, "w") as f:
        for line in lines:
            if keyword_to_delete not in line:
                f.write(line)


form.ClikBut.clicked.connect(ClickOnbut)
form.pushButton1.clicked.connect(List)
form.conButton.clicked.connect(con_rcon)
form.saveButton.clicked.connect(SaveConf)
form.MessButton_2.clicked.connect(BroadMess)
form.Mess3.clicked.connect(CommandAdm)
form.KickButton.clicked.connect(Kick)
form.BanButton_2.clicked.connect(Ban)
form.BanListButton.clicked.connect(BanLi)
form.UnBanButton_4.clicked.connect(UnBn)
form.checkBox.stateChanged.connect(listauto)

# подключение таймера к list
update_timer.timeout.connect(List)

app.exec()
