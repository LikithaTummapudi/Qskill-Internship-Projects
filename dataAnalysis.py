#Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class dataAnalyzer:
    def __init__(self,csv_file):
        self.df=pd.read_csv(csv_file,index_col=0)
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

            #Average=Mean
            mean=self.df[column_name].mean()
            median=self.df[column_name].median()
            std=self.df[column_name].std()

            print(f"\nStatistics Of {column_name}")
            print("\nAverage: ",mean)
            print("\nMedian: ",median)
            print("\n Standard Deviation: ",std)

        else:
            print(f"Column {column_name} is not found.")


    def scatter_plot(self,x_col,y_col):

        plt.figure(figsize=(10, 6))
        plt.scatter(x_col,y_col,c="red")
        plt.xlabel(x_col,fontsize=12)
        plt.ylabel(y_col,fontsize=12)
        plt.title("Scatter plot",fontsize=15,fontweight="bold")

        #light grid for readability(alpha -> transperancy)
        plt.grid(True,alpha=0.3)

        #Adding a trendline
        z=np.polyfit(self.df[x_col].dropna(),self.df[y_col].dropna(),1)
        p=np.poly1d(z)  #stores the cofficients of z in p in a vector form
         
        #plotting the trend line
        plt.plot(self.df[x_col],p(self.df[y_col]),"r--",alpha=0.8,linewidth=2,label="TrendLine")
        plt.lengend()
        plt.tight_layout()
        plt.savefig(f'scatter plot:{x_col} VS {y_col}.png',dip=300,bbox_inches='tight')
        plt.show()

        print(f"\n Scatter plot saved as 'scatter_plot_{x_col}_vs_{y_col}.png'")

        #Calculating Correlation
        correlation=self.df[x_col].corr(self.df[y_col])
        print(f"Correlation between {x_col} and {y_col}: {correlation:.3f}")

    def bar_graph(self,col_name):

        plt.figure(figsize=(10,6))

        #If the value has too many unique values,consider only the top 10
        value_counts=self.df[col_name].value_counts().head(10)

        plt.bar(range(len(value_counts)),value_counts.values,color="blue",edgecolor="navy")
        plt.xlabel(col_name,fontsize=12)
        plt.ylabel('Frequency',fontsize=12)
        plt.title(f"Bar Chart for {col_name}")
        plt.xticks(range(len(value_counts)),value_counts.index,rotation=45,ha='right')
        plt.tight_layout()
        plt.savefig(f'bar_chart_of_{col_name}.png',dpi=300,bbox_inches='tight')
        plt.show()
        print(f"\nbar_chart_of_{col_name}.png saved!")



    