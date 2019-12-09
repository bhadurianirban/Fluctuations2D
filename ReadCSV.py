import pandas as pd
import numpy as np
from scipy import sparse


class ReadCSV:

    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.csv_matrix_df = None

    def read_matrix_in_dataframe(self):
        self.csv_matrix_df = pd.read_csv(self.csv_file_path, header=None, names=['Row', 'Col', 'Val'],)
        self.csv_matrix_df = self.csv_matrix_df.sort_values(['Row', 'Col']).drop_duplicates().reset_index(drop=True)
        row_ind = self.csv_matrix_df['Row']
        col_ind = self.csv_matrix_df['Col']
        data = self.csv_matrix_df['Val']
        mat_coo = sparse.coo_matrix((data, (row_ind, col_ind)))

        print(mat_coo)

