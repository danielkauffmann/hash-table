import pandas as pd


class DataSet:
    def __init__(self):
        self.data: pd.DataFrame

        self._prepare()

    def _prepare(self):
        self.data = pd.read_csv('data.csv')

    def columns(self):
        return self.data.columns

    def values(self):
        return self.data.values

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return 'DataSet from "data.csv" file'

    def __repr__(self):
        return 'DataSet from "data.csv" file'
