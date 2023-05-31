import math

class line:
    
    # 외부에서 접근 불가능한 필드 __length, 초기값 = 0
    # 생성자를 통해 초기 __length의 값을 지정할 수 있음
    __width = 0
    __height = 0
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    # set_length를 통해 필드에 접근하여 length 값을 바꿀 수 있음
    def set_length(self, width, height):
        self.__width = width
        self.__height = height
        
    # get_length를 통해 필드에 접근하여 length 값을 받을 수 있음
    def get_length(self):
        return self.__width, self.__height

# 인자로 length를 받아 (length^2)를 반환하는 함수  
def area_rectangle(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height

# 인자로 length를 받아 (length^2 * pi)를 반환하는 함수
def area_ellipse(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi

# 인자로 length를 받아 (length^2 * root(3) / 4)를 반환하는 함수
def area_right_triangle(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2