import pandas as pd
dict = {'name':["rounak", "adarsh", "siddhant", "Girish"],
		'degree': ["AIML", "CA", "ENTC", "MBA"],
		'score':[60, 75, 80, 65]}
df = pd.DataFrame(dict)
print(df)