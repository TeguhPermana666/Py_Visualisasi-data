"""
Histogam digunakan untuk menjelaskan distribusi suatu kategori data
sumbu x nya digunakan untuk menunjukan rentang nilai 
"""
import pandas as pd
corona_data=pd.read_csv("D:/TeguhPermana_data/Visualisasi_data/main_table_countries_today.csv",error_bad_lines=False)
corona_data=corona_data.iloc[5:,:]
#menampilkan dara
print(corona_data)