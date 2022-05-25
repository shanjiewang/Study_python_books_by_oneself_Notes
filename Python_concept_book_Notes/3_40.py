import new_makefood

# 被當模組import時,有if __name__=='__main__'就不會重複輸出原模組設定值
new_makefood.make_icecream_Fn('可可','咖啡')
new_makefood.make_drink_Fn('small','coke')