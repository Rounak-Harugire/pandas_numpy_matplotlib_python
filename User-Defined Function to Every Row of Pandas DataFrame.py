import pandas as pd
def add_values(row):
	return row['A'] + row['B'] + row['C']

def main():
	data = {
		'A': [1, 2, 3],
		'B': [4, 5, 6],
		'C': [7, 8, 9]}
	
	df = pd.DataFrame(data)
	print("Original DataFrame:\n", df)

	df['add'] = df.apply(add_values, axis=1)

	print('\nAfter Applying Function: ')
	print(df)

if __name__ == '__main__':
	main()