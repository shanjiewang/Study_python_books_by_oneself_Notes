def make_icecream_Fn(*toppings):
    print('冰淇淋的配料如下:')
    for t in toppings:
        print(t)
    print()
        
#title()返回字符串的標題大小寫版本
def make_drink_Fn(size,drink):
    print('輸入飲料尺寸及種類:')
    print(size.title())
    print(drink.title())

make_icecream_Fn('巧克力')
make_icecream_Fn('草莓','香草')
make_drink_Fn('large','teamilk')