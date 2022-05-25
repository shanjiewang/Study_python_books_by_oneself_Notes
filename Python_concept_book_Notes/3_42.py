class Person(object):
    def __new__(cls,name,age):
        print('__new__:name={},age={}'.format(name,age))
        instance=object.__new__(cls)
        return instance

    def __init__(self,name,age):
        print('__new__:name={},age={}'.format(name,age))
p=Person('Peter',59)