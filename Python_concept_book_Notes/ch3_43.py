class Grandfather():
    '''定義祖父類別'''
    pass
class Father(Grandfather):
    '''定義祖父類別'''
    pass
class Ivan(Father):
    '''定義祖父類別'''
    def fn(self):
        pass

grandfather=Grandfather()
father=Father()
ivan=Ivan()

print('ivan屬於Ivan類別:',isinstance(ivan,Ivan))
print('ivan屬於Father類別:',isinstance(ivan,Father))
print('ivan屬於Grandfather類別:',isinstance(ivan,Grandfather))
print('father屬於Ivan類別:',isinstance(father,Ivan))
print('father屬於Father類別:',isinstance(father,Father))
print('father屬於Grandfather類別:',isinstance(father,Grandfather))
print('grandfather屬於Ivan類別:',isinstance(grandfather,Ivan))
print('grandfather屬於Father類別:',isinstance(grandfather,Father))
print('grandfather屬於Grandfather類別:',isinstance(grandfather,Grandfather))

