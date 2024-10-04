import pandas as pd 
data = pd.read_csv("C:\Users\rouna\OneDrive\Desktop\machine-readable-business-employment-data-Jun-2024-quarter.csv") 
n=9
series = data["business-employment"] 
top = series.head(n = n) 
top 