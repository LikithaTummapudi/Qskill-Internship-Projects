#Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class dataAnalyzer:
    def __init__(self,csv_file):
        self.df=pd.read_csv(csv_file)
        print("Data set loaded successfully")
        print(f"Shape:{self.df.shape}")
        print("The first 5 rows: ")
        print(self.df.head())

    def dataset_info(self):
        print("Dataset Info:\n")
        self.df.info()
        print("Dataset Description:\n",self.df.describe())
        print("Checking for Missing Values:\n",self.df.isnull().sum())

    def calculate_centraltendancies(self,column_name):
        '''In this method,we calculate the mean, median 
        and standard deviation of a particular column.'''
        if column_name in self.df.columns:

            mean=self.df[column_name].mean()
            median=self.df[column_name].median()
            std=self.df[column_name].std()

            print(f"\nStatistics Of {column_name}")
            print("\nMean: ",mean)
            print("\nMedian: ",median)
            print("\n Standard Deviation: ",std)

        else:
            print(f"Column {column_name} is not found.")


        

