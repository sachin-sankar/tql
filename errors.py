import rich
	
def error():
	rich.print('[red]Error occured during execution:')

def fileNotFound(fileName):
	error()
	print(f'[FileNotFound] : File with name "{fileName}.csv" not found.')

def methodNotFound(method):
	error()
	print(f'[MethodNotFound] : Method "{method}" is not defined.')

def missingParams():
	error()
	print(f'[MissingParameters] : One or more parameters is missing.')
	
def columnError():
	error()
	print( '[Column Error] : One or more columns does not exist in table.')
	
def inOperation(operation):
	error()
	print(f'[Invalid Operation] : Operation "{operation}" is invalid in use with "in" method')