# class Account:
#     counter = 0
#     accounts = []
#     def __init__(self, holder, number, balance,credit_line=1500):
#         Account.counter += 1
#         self.__Holder = holder
#         self.__Number = number
#         self.__Balance = balance
#         self.__CreditLine = credit_line
#         Account.accounts.append(self)
#     def __str__(self):
#         return f'Account Holder: {self.__Holder}, Account Number: {self.__Number}, Balance: {self.__Balance}, Credit Line: {self.__CreditLine}'
#     def __repr__(self):
#         return f'Account({self.__Holder}, {self.__Number}, {self.__Balance}, {self.__CreditLine})'
#     def __del__(self):
#         Account.counter -= 1
#         Account.accounts.remove(self)
#     def print_type(self):
#         print("This is a bank account.")
#         print(f"Type of self: {type(self)}")
    
#     @classmethod
#     def cprint_type(cls):
#         print("This is a bank account class.")
#         print(f"Type of cls: {type(cls)}")
# account1 = Account("John Doe", "123456789", 5000)
# print(account1)
# print("Total accounts:", Account.counter, Account.accounts)
# account2 = Account("John Doe", "123456789", 5000)
# print(account2)
# print("Total accounts:", Account.counter, Account.accounts)

# account1.print_type()
# # Account.print_type()#TypeError: Account.print_type() missing 1 required positional argument: 'self'
# Account.print_type(account1)
# account1.cprint_type()
# Account.cprint_type()
########################################

class User:

    def __init__(self, sql=None):
        if sql:
            self.sql = sql
    def get_sql_all(self):
        return f"SELECT * FROM users;"
    
    def get_sql_by_id(self, user_id):
        return f"SELECT * FROM users WHERE id = {user_id};"
    def get_by_id(self, pk):
        sql = self.get_sql_by_id(pk)
        user = User(sql)
        return user


    
class Order:
    def __init__(self, sql=None):
        if sql:
            self.sql = sql
    def get_sql_all(self):
        return f"SELECT * FROM orders;"
    
    def get_sql_by_id(self, order_id):
        return f"SELECT * FROM orders WHERE id = {order_id};"
    def get_by_id(self, pk):
        sql = self.get_sql_by_id(pk)
        order = Order(sql)
        return order
    
user = User()
print(user.get_sql_all())
print(user.get_sql_by_id(1))
print(user.get_by_id(1))
print("-----")
order = Order()

print(order.get_sql_all())
print(order.get_sql_by_id(10))
print(order.get_by_id(10))

class BaseModel:

    def get_sql_all(self):
        return f"SELECT * FROM {self.__class__.__name__.lower()}s;"
    
    def get_sql_by_id(self, pk):
        return f"SELECT * FROM {self.__class__.__name__.lower()}s WHERE id = {pk};"
    @classmethod
    def get_by_id(cls, pk):
        sql = cls().get_sql_by_id(pk)
        instance = cls()
        instance.sql = sql
        return instance
    @staticmethod
    def static_method_example():
        return "This is a static method."
    
class User(BaseModel):
    pass
class Order(BaseModel):
    pass

user = User()
print(user.get_sql_all())
print(user.get_sql_by_id(1))
print(user.get_by_id(1))
print("-----")
order = Order()
print(order.get_sql_all())
print(order.get_sql_by_id(10))
print(order.get_by_id(10))

print(User.static_method_example())
print(user.static_method_example())