#포인트 50으로 시작 ! 
print("신호등에 걸리셨습니다. 기다리시겠습니까?")
a=input("입력해보세요: ")
if a==1: #a가 1일때	
	print("1번 기다린다. 30초 후에 초록불로 바뀝니다.")
elif a==2: #a가 2일때
	print("2번 기다리지 않는다.신호위반입니다. 기다리세요. 30 초 후에 초록불로 바뀝니다.")
else: #a가 1이 아닐때
	print("잘못된 선택입니다.")

#score +20
#score -10

print("초록불로 바뀌었습니다 출발하세요.")

print("cctv 단속 구간입니다. 30km이상으로 운전하면 벌금입니다. 30km이상으로 운전하시겠습니까?")
print(" 30km이하로 달린다. 2번 : 30km 이상으로 달린다.")
a=input("입력해보세요: ")
if a==1:
	print("통과입니다.")
else:
	print("벌금 30만원입니다.")
 #1번 입력했을 경우
#포인트 +30
 #2번 입력했을 경우
#포인트 -30

print("서행하세요. 앞에 장애물이 있습니다. 피해가겠습니까?")
print("1번 : 피해간다. 2번 : 그냥간다")
print("===========")
a=input("입력해보세요: ")
print("======{}=====".format(type(a)))
if a=="1":
	print("SUCCESS! ! ! ") #1번 입력했을 경우 ==1
else:
	print("게임이 끝났습니다. 다시 도전하시겠습니까?") #2번 입력했을 경우