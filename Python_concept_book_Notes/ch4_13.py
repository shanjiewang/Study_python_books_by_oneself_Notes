class Banks():
    title='Taipei Bank'
    
    # 初始化
    def __init__(self,uname,money):
        self.name=uname      # 設定提款者名字
        self.balance=money   # 設定所存的錢
    
    # 設計存款方法
    def save_money(self,money):
        assert money>0,'存款必須大於0'
        self.balance+=money   # 將新存款加上原本存款
        print('存款',money,'完成')
    
    # 設計提款方法
    def withdraw_money(self,money):
        assert money>0,'提款必須大於0'
        assert money<=self.balance,'存款金額不足'
        self.balance-=money
        print('提款',money,'完成')
    
    def get_balance(self):
        print(self.name.title(),'目前餘額:',self.balance)  # 首字大寫