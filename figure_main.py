import figure

# width=10, height=20인 line 객체 생성
myline = figure.line(10, 20)
width, height = myline.get_length()

# area_rectangle 함수를 이용하여 직사각형 넓이 출력
# width, height가 음수인 경우, ValueError가 발생하여 경고문 출력
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("please input positive number for width and height")

# width=20, height=30으로 변경
myline.set_length(20, 30)
width, height = myline.get_length()

# area_right_triangle 함수를 이용하여 직각삼각형 넓이 출력
# width, height가 음수인 경우, ValueError가 발생하여 경고문 출력
try:
    triangle = figure.area_right_triangle(width, height)
    print(triangle)
except ValueError:
    print("please input positive number for width and height")

# width=30, height=40으로 변경
myline.set_length(30, 40)
width, height = myline.get_length()

# area_ellipse 함수를 이용하여 타원 넓이 출력
# width, height가 음수인 경우, ValueError가 발생하여 경고문 출력
try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("please input positive number for width and height")