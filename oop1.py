class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def find_area(self):
        area=width*height
        return area
    def find_perimeter(self):
        perimeter=(width + height)*2
        return perimeter
width=int(input("Nhập chiều rộng:"))
height=int(input("Nhập chiều cao:"))
my_rect=rectangle(width,height)
ar=my_rect.find_area()
per=my_rect.find_perimeter()
print(f"Diện tích: {ar}")
print(f"Chu vi: {per}")