'''
(02) 리스트에서 원소 찾아내기
문제 설명
인자로 주어지는 리스트 L 내에서, 또한 인자로 주어지는 원소 x 가 발견되는 모든 인덱스를 구하여 이 인덱스들로 이루어진 리스트를 반환하는 함수 solution 을 완성하세요.

리스트 L 은 정수들로 이루어져 있고 그 순서는 임의로 부여되어 있다고 가정하며, 동일한 원소가 반복하여 들어 있을 수 있습니다. 이 안에 정수 x 가 존재하면 그것들을 모두 발견하여 해당 인덱스들을 리스트로 만들어 반환하고, 만약 존재하지 않으면 하나의 원소로 이루어진 리스트 [-1] 를 반환하는 함수를 완성하세요.

예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 72 인 경우의 올바른 리턴 값은 [1, 3] 입니다.
또 다른 예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 83 인 경우의 올바른 리턴 값은 [2] 입니다.
마지막으로 또 다른 예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 49 인 경우의 올바른 리턴 값은 [-1] 입니다.

힌트 1: 리스트의 index() 메서드와 리스트 슬라이싱을 활용하는 것이 한 가지 방법이 됩니다. 리스트 슬라이싱은 아래와 같이 동작합니다.

L = [6, 2, 8, 7, 3] 인 경우
L[1:3] = [2, 8]
L[2:] = [8, 7, 3]
L[:3] = [6, 2, 8]

힌트 2: 리스트의 index() 메서드는, 인자로 주어지는 원소가 리스트 내에 존재하지 않을 때 ValueError 를 일으킵니다. 이것을 try ... except 로 처리해도 되고, if x in L 과 같은 조건문으로 특정 원소가 리스트 내에 존재하는지를 판단해도 됩니다.
'''

def solution(L, x):
    answer = []
    for i in range(0,len(L)):
        if L[i] == x:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer