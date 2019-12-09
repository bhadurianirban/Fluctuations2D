import pandas as pd

class ReadCSV :

    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.csv_matrix_df = None

    def read_matrix_in_dataframe(self):
        self.csv_matrix_df = pd.read_csv(self.csv_file_path, header=None, names=['Row', 'Col', 'Val'])
        self.csv_matrix_df = self.csv_matrix_df.sort_values('Row')
        print(self.csv_matrix_df.head())
