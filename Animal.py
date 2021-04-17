# 史少博
# 开发时间 2021/4/17 23:31
class Dog:
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def set(self):
        print(f"{self.age}岁的{self.name}正在坐下")

    def over(self):
        print(f"{self.age} 今年8岁了")


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self):
        print(f"{self.name} 正在坐下")

    def over(self):
        print(f"{self.age} 今年8岁了")
