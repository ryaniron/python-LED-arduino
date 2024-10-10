from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 317)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.antigenLabel = QtWidgets.QLabel(Dialog)
        self.antigenLabel.setObjectName("antigenLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.antigenLabel)
        self.antigenLineEdit = QtWidgets.QLineEdit(Dialog)
        self.antigenLineEdit.setObjectName("antigenLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.antigenLineEdit)
        self.checkWL1 = QtWidgets.QCheckBox(Dialog)
        self.checkWL1.setObjectName("checkWL1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkWL1)
        self.comboWL1 = QtWidgets.QComboBox(Dialog)
        self.comboWL1.setObjectName("comboWL1")
        self.comboWL1.addItem("460 nm")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboWL1)
        self.checkWL2 = QtWidgets.QCheckBox(Dialog)
        self.checkWL2.setObjectName("checkWL2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkWL2)
        self.comboWL2 = QtWidgets.QComboBox(Dialog)
        self.comboWL2.setObjectName("comboWL2")
        self.comboWL2.addItem("570 nm")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboWL2)
        self.checkWL3 = QtWidgets.QCheckBox(Dialog)
        self.checkWL3.setObjectName("checkWL3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkWL3)
        self.comboWL3 = QtWidgets.QComboBox(Dialog)
        self.comboWL3.setObjectName("comboWL3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboWL3)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(137, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushSave = QtWidgets.QPushButton(Dialog)
        self.pushSave.setObjectName("pushSave")
        self.gridLayout.addWidget(self.pushSave, 1, 1, 1, 1)
        self.pushCancel = QtWidgets.QPushButton(Dialog)
        self.pushCancel.setObjectName("pushCancel")
        self.gridLayout.addWidget(self.pushCancel, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Antigen"))
        self.antigenLabel.setText(_translate("Dialog", "Antigen"))
        self.checkWL1.setText(_translate("Dialog", "Wavelength 1"))
        self.checkWL2.setText(_translate("Dialog", "Wavelength 2"))
        self.checkWL3.setText(_translate("Dialog", "Wavelength 3"))
        self.pushSave.setText(_translate("Dialog", "Save"))
        self.pushCancel.setText(_translate("Dialog", "Cancel"))


class AntigenDialog(QtWidgets.QDialog):

    def __init__(self):
        super(AntigenDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushCancel.clicked.connect(self.cancel_button_clicked)


    def cancel_button_clicked(self):
        self.hide()
