###################################
#########  Anas Zughayyar  ########
###################################
##### Users with Bank Account #####
###################################

from user import User

anas = User("Anas Zughayyar", "anas@axsos.academy")
omar = User("Omar Rayyan", "omar@axsos.academy")

anas.display_account_info()
omar.display_account_info()

anas.account.deposit(1000 , "usd")
anas.account.deposit(500 , "ils")

omar.account.deposit(300,"usd").deposit(500,"ils")

anas.display_account_info()
omar.display_account_info()

anas.account.withdraw(2000,'ils')
anas.display_account_info()

anas.account.withdraw(200,'ils')
anas.display_account_info()