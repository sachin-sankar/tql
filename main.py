import errors as error
import defaults as default

global csv, filename
csv = []
filename = ['[unloaded]']

def load(name):
	try:
		with open(f'{name}.csv','r') as file:
			filename[0] = f'{name}.csv'
			rows = file.read().split('\n')
			columnData = rows.pop(0).split(',')
			fileData = []
			for row in rows:
				fileData.append(row.split(','))
			csv.append(columnData)
			csv.append(fileData)
			print(f'Loaded file "{name}.csv"')
	except FileNotFoundError:
		error.fileNotFound(name)

def parse(queryString):
	# Query formatting 
	queryParams = queryString.strip().split()
	queryMethod = queryParams.pop(0)
	
	# Query Validation
	if queryMethod not in default.MethodsMap.keys():
		error.methodNotFound(queryMethod)
		return
	if len(queryParams) != default.MethodsMap[queryMethod]:
		error.missingParam()
		return
	
	#Query Processing
	# Load
	if queryMethod == 'load':
		load(queryParams[0])
	
	#In
	elif queryMethod == 'in':
		columns = queryParams[0].split(',')
		operation = queryParams[1]
		condition = queryParams[2]
		# Query Parameter Validation
		for column in columns:
			if column not in csv[0]:
				error.columnError()
				return
		if operation not in default.ValidInOperations:
			error.inOperation(operation)
		
		# Select * condition
		if condition == '*':
			 columnDataSets = []
			 for column in columns:
			 	index = csv[0].index(column)
			 	columnDataSet = []
			 	for row in csv[1]:
			 		columnDataSet.append(row[index])
			 	columnDataSets.append(columnDataSet)
			 queryResult = []
			 for i in range(len(columnDataSets[0])):
			 	row = []
			 	for column in columnDataSets:
			 		row.append(column[i])
			 	queryResult.append(row)
			 
			 print(queryResult)
			 
def client():
	while True:
		parse(input('\n'+filename[0]+'/>'))

client()