selected = None
while selected not in ['가위','바위','보']:
	selected = input('가위, 바위, 보 중에 선택하세요>')
	
print('선택된 값은: ',selected)

patterns = ['가위','바위','보']


for pattern in patterns:
	print(pattern)
	
for i in range(len(patterns)):
	print(patterns[i])

length = len(patterns)
i = 0
	
while i < length:
	print(patterns[i])
	i = i + 1