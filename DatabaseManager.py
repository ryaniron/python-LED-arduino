import sqlite3
import Batch
import Sample
import Measurement

class DatabaseManager:
    def __init__ (self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        create_batches_table_query = '''
        CREATE TABLE IF NOT EXISTS Batches (
            batch_id INTEGER PRIMARY KEY,
            batch_name TEXT NOT NULL
        )
        '''

        create_samples_table_query = '''
        CREATE TABLE IF NOT EXISTS Samples (
            sample_id INTEGER PRIMARY KEY,
            batch_id INTEGER NOT NULL,
            sample_name TEXT NOT NULL,
        )
        '''
        create_ref_table_query = '''
        CREATE TABLE IF NOT EXISTS Ref_Meas (
            meas_id INTEGER PRIMARY KEY,
            sample_id INTEGER NOT NULL,
            ref_meas INTEGER NOT NULL,
            meas_index INTEGER NOT NULL
        )
        '''

        create_sample_table_query = '''
        CREATE TABLE IF NOT EXISTS Sample_Meas (
            meas_id INTEGER PRIMARY KEY,
            sample_id INTEGER NOT NULL,
            sample_meas INTEGER NOT NULL,
            meas_index INTEGER NOT NULL
        )'''


        # Execute the table creation queries
        self.cursor.execute(create_batches_table_query)
        self.cursor.execute(create_samples_table_query)
        self.cursor.execute(create_ref_table_query)
        self.cursor.execute(create_sample_table_query)

    def insert_batch(self, batch):
        query = 'INSERT INTO Batches (batch_name) VALUES (?)'
        data = (batch.batch_name)
        self.cursor.execute(query, data)
        self.connection.commit()

        batch_id = self.cursor.lastrowid
        return batch_id

    def insert_sample(self, sample):
        query = 'INSERT INTO Samples (batch_id, sample_name) VALUES (?, ?)'
        data = (sample.batch_id, sample.sample_name)
        self.cursor.execute(query, data)
        self.connection.commit()

        sample_id = self.cursor.lastrowid
        return sample_id

    def insert_ref_meas(self, measurement):
        query = 'INSERT INTO Ref_Meas (sample_id, ref_meas, meas_index) VALUES (?, ?, ?)'
        data = (measurement.sample_id, measurement.value, measurement.index)
        self.cursor.execute(query, data)
        self.connection.commit()

    def insert_sample_meas(self, measurement):
        query = 'INSERT INTO Sample_Meas (sample_id, sample_meas, meas_index) VALUES (?, ?, ?)'
        data = (measurement.sample_id, measurement.value, measurement.index)
        self.cursor.execute(query, data)
        self.connection.commit()

    def get_batch():
        pass

    def get_sample():
        pass

    def get_ref_meas():
        pass

    def get_sample_meas():
        pass

    def close_db(self):
        self.cursor.close()
        self.connection.close()