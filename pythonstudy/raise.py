#def rsp(mine,yours):
#	allowed = ['가위','바위','보']
#	if mine not in allowed:
#		raise ValueError
#	if yours not in allowed:
#		raise ValueError
#	#가위바위보 승패를 판단하는 코드
#	
#try:
#	rsp('가위','바')
#except ValueError:
#	print('잘못된 값을 넣은 것 같습니다.')
	
school = {'1반': [172,185,198,177,165,199], '2반':[165,177,167,180,191]}
try:
	for class_number, students in school.items():
		for student in students:
			if student>190:
				print(class_number, '반에 190을 넘는 학생이 있습니다')
				raise StopIteration
				#break
except StopIteration:
	print('정상종료')