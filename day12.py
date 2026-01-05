'''class A():
    __a =100
    __api_key ="12m,21231234"
    b=0
    def __data(self):
        return self.__api_key
    def __datasci(self):
        return self.
class B(A):
    c= 100
    def test(self):
        return self.__a
    
obj = A()'''

class Parent:
    __hospital_name = "BPKISH"
    __patient_count = 0
    def admit_patient(self,n=1):
        self.__patient_count = self.__patient_count+1
        return self.__patient_count
    def discharge_patient(self):
        if self.__patient_count <=0:
            return "Patient count is negative or zero"
        self.__patients_count = self.__patient_count-1
        return self.__patient_count

    def hospital_info(self):
        return f' {self.__hospital_name} and patient count is {self.__patient_count}'
    
class SpecialtyHospital(Parent):
    def bulkAdmit(self):
        return self.admit__patient (n=5)
    
obj = SpecialtyHospital()
for i in range(1):
    obj.admit_patient()
for i in range (5):
    print(obj.discharge_patient())

class BankAccount:
    __acount_number = "2345"
    __balance = 0.0

    def deposit(self):

        self.amount = self.amount+ self.__balance
        return self.amount
    def withdrawl(self):
        self.withd= self.amount - self.__balance
        return self.withdrawl
    def get_balance(self):
        return f' The current balance is { self.amount- self.withd}'

class Saving(BankAccount):
    __interest_rate = 34.5
    def add_interest(self):
        self.get_balance()
        self.interest_increase = self.__balance+ 0.345*self.__balance
        return self.interest_increase
    def get_account_info(self):
        return f'The account number is {self.__acount_number} and balance is {self.__balance}'
    
obj = Saving()
print(obj.deposit(5000))
print(obj.get_account_info())
    


