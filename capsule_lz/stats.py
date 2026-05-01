import pandas as pd
import matplotlib.pyplot as plt


class GraphicalStatistics:
    def __init__(self, data_input):
        if type(data_input) != str:
            self.df = data_input
        else:
            self.df = pd.read_csv(data_input)
        
    def make_chart(self):
        country_counts = self.df['country'].value_counts()
        top_countries = country_counts.head(10)
        labels = top_countries.index
        values = top_countries.values
        plt.figure(figsize=(10, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('TOP 10 COUNTRES STATS')
        plt.legend(labels, title="", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
        plt.show()
