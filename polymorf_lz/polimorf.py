import pandas as pd


class Polimorf:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        
    def __invert__(self):
        count_before = len(self.df)
        self.df = self.df.drop_duplicates()
        count_after = len(self.df)
        res = count_before - count_after
        print(f'Количество повторяющихся строк в наборе данных: {res}')
        return self

    def split_data(self):
        fiz_data = self.df[self.df['Участники гражданского оборота'] == 'физ. лицо']
        fiz_data.to_csv('fiz_litsa.csv', index=False)
        ur_data = self.df[self.df['Участники гражданского оборота'] == 'юр. лицо']
        ur_data.to_csv('ur_litsa.csv', index=False)
