class Customer: 
    def __init__(self, name: str, age: int, gender: str): 
        self.__name = name 
        self.__age = age 
        self.__gender = gender 
    
    def get_name(self) -> str: 
        return self.__name
    
    def get_age(self) -> int: 
        return self.__age
    
    def get_gender(self) -> str: 
        return self.__gender
    
    def __str__(self): 
        return f'{self.__name}, {self.__age}, {self.__gender}'

customer = Customer("Mohamed", 34, "Male")
