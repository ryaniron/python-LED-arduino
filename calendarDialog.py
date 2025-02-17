from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 344)
        Dialog.setMinimumSize(QtCore.QSize(448, 344))
        Dialog.setMaximumSize(QtCore.QSize(448, 344))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(119, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Date"))
        self.saveButton.setText(_translate("Dialog", "Save"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))


class CalendarDialog(QtWidgets.QDialog):

    def __init__(self):
        super(CalendarDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.date = None

        self.ui.saveButton.clicked.connect(self.save_button_clicked)
        self.ui.cancelButton.clicked.connect(self.cancel_button_clicked)

    def save_button_clicked(self):
        self.date = self.ui.calendarWidget.selectedDate().toString("MM-dd-yyyy")
        self.done(QtWidgets.QDialog.Accepted)

    def cancel_button_clicked(self):
        self.hide()
