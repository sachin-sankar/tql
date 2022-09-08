global csv, filename
csv = []
filename = ['unloaded']

def load(name):
	try:
		with open(f'{name}.csv','r') as file:
			filename[0] = name
			data = file.read()
			list = data.split('\n')
			column = list.pop(0).split(',')
			data = []
			for i in list:
				data.append(i.split(','))
			csv.append(column)
			csv.append(data)
			print(f'[S200] : Loaded {name}')
	except FileNotFoundError:
		print(f'[E404] : No such file {name}')

def parse(com):
	com = com.split()
	if com[0] == 'load':
		try:
			load(com[1])
		except IndexError:
			print('[E400] Incomplete query')
	elif com[0] == 'in':
		columns = com[1].split(',')
		if com[2] == 'select':
			data = []
			if com[3] == '*':
				 for column in columns:
				 	index = csv[0].index(column)
				 	columnData = []
				 	for row in csv[1]:
				 		columnData.append(row[index])
				 	data.append(columnData)
		if len(columns) > 1:
			newdata = []
			for index in range(len(data[0])):
				buffer = []
				for column in data:
					buffer.append(column[index])
				newdata.append(buffer)
		for row in newdata:
			print(row)
	else:
		print(f'[E402] Unknown command "{com[0]}"')
		
		
def client():
	while True:
		parse(input('\n'+filename[0]+'/>'))

client()