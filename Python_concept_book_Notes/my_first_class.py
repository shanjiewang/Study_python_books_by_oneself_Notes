class myDeposit():
    def __init__(self,name,money):
        self.name=name
        self.money=money
    
    def adds(self,money):
        assert money>=100,'每次儲值需大於100元'
        self.money+=money   # 將新存款加上原本存款
        print(self.money) 
        
    def reduces(self,money):
        assert money>0,'每次付款需大於0'
        self.money-=money
        print(self.money)
    
    def nows(self):
        print(self.name,':',self.money)