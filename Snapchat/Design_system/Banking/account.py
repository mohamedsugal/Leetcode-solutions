from customer import Customer

class Account(Customer): 
    def __init__(self, name: str, age: int, gender: str, account_number: int):
        super().__init__(name, age, gender)
        self.__account_number = account_number
        self.__balance = 0 

    def get_account_number(self) -> int: 
        return self.__account_number

    def show_details(self) -> None:
        print('ACCOUNT DETAILS')
        print('------------------')
        print(f'Name: {self.get_name()}\nAge:{self.get_age()}\
        \nGender:{self.get_gender()}\nAccount No: {self.get_account_number()}')
        print('------------------')
    
    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        self.__balance -= amount
    
    def check_balance(self) -> None: 
        print(f'Your account balance is ${self.__balance}')




customer1 = Account("Mohamed", 34, "Male", 76971811)
customer1.show_details()
customer1.check_balance()
customer1.deposit(100)
customer1.withdraw(30)
customer1.check_balance()