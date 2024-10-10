from PyQt5 import QtCore, QtGui, QtWidgets
from testWindow import TestWindow
from resultsWindow import ResultsWindow
from settingsWindow import SettingsWindow
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.logoTop = QtWidgets.QLabel(self.centralwidget)
        self.logoTop.setText("")
        self.logoTop.setPixmap(QtGui.QPixmap(":/resources/logoNamed.png"))
        self.logoTop.setObjectName("logoTop")
        self.gridLayout_2.addWidget(self.logoTop, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushTest = QtWidgets.QPushButton(self.centralwidget)
        self.pushTest.setMinimumSize(QtCore.QSize(200, 0))
        self.pushTest.setObjectName("pushTest")
        self.gridLayout.addWidget(self.pushTest, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.pushResults = QtWidgets.QPushButton(self.centralwidget)
        self.pushResults.setMinimumSize(QtCore.QSize(200, 0))
        self.pushResults.setObjectName("pushResults")
        self.gridLayout.addWidget(self.pushResults, 1, 1, 1, 1)
        self.pushSettings = QtWidgets.QPushButton(self.centralwidget)
        self.pushSettings.setMinimumSize(QtCore.QSize(200, 0))
        self.pushSettings.setObjectName("pushSettings")
        self.gridLayout.addWidget(self.pushSettings, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.pushExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushExit.setObjectName("pushExit")
        self.gridLayout.addWidget(self.pushExit, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushTest.setText(_translate("MainWindow", "Test"))
        self.pushResults.setText(_translate("MainWindow", "View Results"))
        self.pushSettings.setText(_translate("MainWindow", "Settings"))
        self.pushExit.setText(_translate("MainWindow", "Exit"))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushTest.clicked.connect(self.test_button_clicked)
        self.ui.pushResults.clicked.connect(self.results_button_clicked)
        self.ui.pushSettings.clicked.connect(self.settings_button_clicked)
        self.ui.pushExit.clicked.connect(self.exit_button_clicked)


    def test_button_clicked(self):
        self.hide()
        self.testWindow = TestWindow(self)
        self.testWindow.show()


    def results_button_clicked(self):
        self.hide()
        self.resultsWindow = ResultsWindow(self)
        self.resultsWindow.show()


    def settings_button_clicked(self):
        self.hide()
        self.settingsWindow = SettingsWindow(self)
        self.settingsWindow.show()


    def exit_button_clicked(self):
        QtCore.QCoreApplication.instance().quit()


