### 3_44 ###

# 未定義__str__只能印出類別
class Name:
    def __init__(self,name):
        self.name=name
a=Name('Hung')
print(a)
print()

class Name:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return '%s' % self.name
a=Name('Hung')
print(a)