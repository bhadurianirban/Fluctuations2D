import pandas as pd
import numpy as np
from scipy import sparse


class ReadCSV:

    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.csv_matrix_df = None

    def read_matrix_in_dataframe(self):
        self.csv_matrix_df = pd.read_csv(self.csv_file_path, header=None, names=['Row', 'Col', 'Val'],)
        orig_size = self.csv_matrix_df.shape
        self.csv_matrix_df = self.csv_matrix_df.sort_values(['Row', 'Col']).drop_duplicates().reset_index(drop=True)
        uniq_size = self.csv_matrix_df.shape
        diff = orig_size[0] - uniq_size[0]
        print("Dropped duplicates : ", diff)
        row_max = self.csv_matrix_df['Row'].max()
        col_max = self.csv_matrix_df['Col'].max()
        # print(self.csv_matrix_df.head())
        # myval = [29451,695717]
        # if (myval in self.csv_matrix_df['Row','Col']):
        #     print('Gheu')
        # for row_counter in range(row_max):
        #     for col_counter in range(col_max):





