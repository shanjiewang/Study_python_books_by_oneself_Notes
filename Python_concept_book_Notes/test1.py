import ch3_41 as c
import ch4_13 as B
import my_first_class as m

print(c.A,c.B,c.C)
c.A=c.B+c.C
print(c.A)

hungBank=B.Banks('hung',300)
hungBank.get_balance()
hungBank.save_money(1000)
hungBank.get_balance()
hungBank.withdraw_money(500)
hungBank.get_balance()
# hungBank.withdraw_money(-300)   # assert拋例外
# hungBank.get_balance()

my_deposit=m.myDeposit('ShanJie',1000)
my_deposit.adds(200)
my_deposit.nows()
my_deposit.reduces(-99)  # assert拋例外
my_deposit.nows()