from PyQt5 import QtWidgets, uic, QtGui
import pickle
import os
import numpy as np
import json


def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    f.close()


def verif():
    if len(u.NUMBER.text()) == 8 and len(u.IMEI.text()) == 15 and u.NUMBER.text().isnumeric() and u.IMEI.text().isnumeric():
        with open('data.json') as jsonfile:
            data = json.load(jsonfile)
            temp = data["data"]
            v = False
            for i in range(len(temp)):
                if u.NUMBER.text() == temp[i]['number'] and u.IMEI.text() == temp[i]['IMEI']:
                    v = True
                    x = str(temp[i]['state'])
                    if x == 'True':
                        x = 'valide'
                    else:
                        x = 'bloquer'
            if v:
                QtWidgets.QMessageBox.information(
                    u, 'information numero', x, QtWidgets.QMessageBox.Ok)
            else:

                y = {"number": u.NUMBER.text(), "IMEI": u.IMEI.text(),
                     "state": True}
                temp.append(y)
                write_json(data, 'data.json')
                jsonfile.close()
                QtWidgets.QMessageBox.information(
                    u, 'Numero ajouter', "votre numero a bien étè ajouter avec success", QtWidgets.QMessageBox.Ok)
    else:
        QtWidgets.QMessageBox.warning(
            u, 'erreur', "verifier votre IMEI ou votre numero", QtWidgets.QMessageBox.Ok)


def blq():
    if len(u.NUMBER.text()) == 8 and len(u.IMEI.text()) == 15 and u.NUMBER.text().isnumeric() and u.IMEI.text().isnumeric():
        imei = u.IMEI.text()
        res = [int(i) for i in imei]
        res.append(0)
        arr = np.array(res)
        arr = arr.reshape(4, 4)
        s = np.sum(arr)

        rev = np.fliplr(arr)
        d1 = arr.diagonal()
        d2 = rev.diagonal()
        totdiag = [x + y for x, y in zip(d1, d2)]
        mdp = list()
        for i in range(len(totdiag)):
            asc = totdiag[i] + 64
            mdp.append(chr(asc))
        password = ''.join(mdp) + str(s)
        msg = 'Le code blocage :\n' + str(password)
        QtWidgets.QMessageBox.information(
            u, 'Le code blocage ', msg, QtWidgets.QMessageBox.Ok)
    else:
        QtWidgets.QMessageBox.warning(
            u, 'erreur', "verifier votre IMEI ou votre numero", QtWidgets.QMessageBox.Ok)


def init():
    u.IMEI.setFocus()


app = QtWidgets.QApplication([])
u = uic.loadUi("sajalni-interface.ui")
u.show()
init()
u.verifier.clicked.connect(lambda: verif())
u.bloquer.clicked.connect(lambda: blq())
onlyInt = QtGui.QIntValidator()
u.NUMBER.setValidator(onlyInt)

app.exec_()
