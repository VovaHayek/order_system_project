# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

import requests

class DictionaryTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers):
        super(DictionaryTableModel, self).__init__()
        self._data = data
        self._headers = headers

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Look up the key by header index.
            column = index.column()
            column_key = self._headers[column]
            if column_key == 'menu':
                menu = ' '.join(self._data[index.row()][column_key])
                return menu
            return self._data[index.row()][column_key]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The length of our headers.
        return len(self._headers)

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if self._headers[section] == 'amount':
                    return str(self._headers[section] + ' $')
                return str(self._headers[section])

            if orientation == Qt.Vertical:
                return str(section)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1001, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 10, 200, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 50, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(25, 100, 950, 550))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 950, 550))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.l = []
        self.response = requests.get('http://127.0.0.1:8000/get-order-data?restaurant=McDonalds')
        for index, data in self.response.json().items():
            self.l.append(data)
        self.headers = ['restaurant', 'amount', 'menu']

        self.show_rest_name()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def show_rest_name(self):
        self.pushButton.clicked.connect(lambda: self.show_restaurant(self.lineEdit.text()))

    def show_restaurant(self, rest):
        print(self.l)
        self.model = DictionaryTableModel(self.l, self.headers)
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 250)
        self.tableView.setColumnWidth(2, 550)
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
