import math

class line:
    
    # 외부에서 접근 불가능한 필드 __length, 초기값 = 0
    # 생성자를 통해 초기 __length의 값을 지정할 수 있음
    def __init__(self, length=0):
        self.__length = length
        
    # set_length를 통해 필드에 접근하여 length 값을 바꿀 수 있음
    def set_length(self, length):
        self.__length = length
        
    # get_length를 통해 필드에 접근하여 length 값을 받을 수 있음
    def get_length(self):
        return self.__length

# 인자로 length를 받아 (length^2)를 반환하는 함수  
def area_square(length):
    return length ** 2

# 인자로 length를 받아 (length^2 * pi)를 반환하는 함수
def area_circle(length):
    return length ** 2 * math.pi

# 인자로 length를 받아 (length^2 * root(3) / 4)를 반환하는 함수
def area_regular_triangle(length):
    return (math.sqrt(3) / 4) * (length ** 2)