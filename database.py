from PyQt5 import QtSql
from PyQt5.QtSql import *
import pandas as pd
import sqlite3
from PyQt5.QtCore import QAbstractTableModel, Qt


class Database:
    is_instantiated = False
    path = "D:/EEE489/nano2RED/nano2RED/database.db"

    def __init__(self):
        if not Database.is_instantiated:
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName(self.path)
            self.db.open()
            Database.is_instantiated = True
            self.db.close()

    def get_results(self, num_show):

        results_string = """SELECT Results.sample_id as ID, Results.date as "Date",
                            Results.antigen as "Antigen", Results.wavelength as "Wavelength",
                            Results.reading as "Reading", Results.normalized as "Normalized",
                            Results.result as "Result" FROM Results ORDER BY rec_num DESC LIMIT {}""".format(num_show)
        con = sqlite3.connect(self.path)
        results_db = pd.read_sql_query(results_string, con)
        con.close()
        return results_db

    def results_search(self, num_show, condition_list):

        search_string = """SELECT Results.sample_id as ID, Results.date as "Date",
                           Results.antigen as "Antigen", Results.wavelength as "Wavelength",
                           Results.reading as "Reading", Results.normalized as "Normalized",
                           Results.result as "Result" FROM Results """

        condition_length = len(condition_list)
        condition = ""

        for i in range(condition_length-1):
            condition += condition_list[i][0] + " = " + condition_list[i][1] + " and "

        if condition_length > 0:
            condition += condition_list[-1][0] + " = " + condition_list[-1][1] + " "

        if condition:
            search_string += "WHERE " + condition

        search_string += "ORDER BY rec_num DESC LIMIT {}".format(num_show)

        con = sqlite3.connect(self.path)
        search_db = pd.read_sql_query(search_string, con)
        con.close()
        return search_db

    def antigen_list(self):

        antigens_string = """SELECT Antigens.antigenName as "antigen", Antigens.wavelength1 as WL1,
                            Antigens.wavelength2 as WL2, Antigens.wavelength3 as WL3 FROM Antigens"""
        con = sqlite3.connect(self.path)
        antigen_db = pd.read_sql_query(antigens_string, con)
        con.close()
        return antigen_db

    def calibration_list(self, num_show):

        calibration_string = """SELECT Calibration.date as "Date", Calibration.sample_num as "Sample Number",
                                Calibration.WL1 as "Wavelength 1", Calibration.WL2 as "Wavelength 2",
                                Calibration.WL3 as "Wavelength 3", Calibration.Empty as "Empty",
                                Calibration.Threshold as "Threshold" FROM Calibration ORDER BY date
                                DESC LIMIT {}""".format(num_show)

        con = sqlite3.connect(self.path)
        calibration_db = pd.read_sql_query(calibration_string, con)
        con.close()
        return calibration_db

    def add_results(self, data):

        add_string = """insert into Results (sample_id, date, antigen, wavelength, reading, normalized, result)
                               values (?,?,?,?,?,?,?)"""

        con = sqlite3.connect(self.path)
        cursor = con.cursor()
        cursor.executemany(add_string, data)
        con.commit()
        con.close()


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
