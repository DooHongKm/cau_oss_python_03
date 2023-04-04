#사용자에게 박스 정보 입력받기
width=float(input("가로 : "))
depth=float(input("세로 : "))
height=float(input("높이 : "))

#입력값으로 부피를 계산하여 출력
volume=width*depth*height
print("부피 :", volume)

#입력값으로 총길이를 계산하여 출력
total_length=width+depth+height
print("총 길이 :", total_length)

#총길이에 따른 요금 계산하여 출력
if total_length<=80: cost=5000
elif total_length<=100: cost=8000
elif total_length<=120: cost=10000
elif total_length<=160: cost=13000
else: cost="Not Defined"
print("요금 :", cost)

#수정