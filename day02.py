from datetime import datetime

class account(object):
    def __init__(self,accountname,accountamount):
        self.__accountname = accountname
        self.__accountamount = float(accountamount)

    def getName(self):
        #print(self.__accountname)
        return(self.__accountname)
    def getAmount(self):
        print("%s : %s " %(self.__accountname,self.__accountamount))
        print("----------" + datetime.now().strftime('%Y-%m-%d %a %H:%M.%S'))
        return(self.__accountamount)
    def save(self,saveamount):
        try :
            self.__accountamount += float(saveamount)            
            print("%s : %s " %(self.__accountname,self.__accountamount))
            print("----------" + datetime.now().strftime('%Y-%m-%d %a %H:%M.%S'))
        except:
            print("THE SAVEAMOUNT MUST BE INT OR FLOAT")
        return self.__accountamount
        
    def withdrawal(self,withdrawalamount):
        try:
            self.__accountamount -= float(withdrawalamount)
            print("%s : %s " %(self.__accountname,self.__accountamount))
        except:
            print("THE WITHDRADAL MUST BE INT OR FLOAT")
        print("----------" + datetime.now().strftime('%Y-%m-%d %a %H:%M.%S'))
        return self.__accountamount
    
    def transfer(self,ToAccount,transferMoney):
        ToAccountName = ToAccount.getName()
        print('%s tranfer %s to %s' %(self.__accountname,transferMoney,ToAccountName))
        self.withdrawal(transferMoney)
        ToAccount.save(transferMoney)
        

Tanya=account("Tanya Chen",0)

Tanya.save("apple")
Tanya.save(1000)
Tanya.save(50.05)
Tanya.withdrawal(200)

Philip=account("Philip Han",3000)
Philip.getAmount()

Philip.transfer(Tanya,13000)

