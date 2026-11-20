def create_account(money):
    current_money = money

    # 存款
    def deposit(add_money):
        nonlocal current_money
        current_money += add_money
        return current_money

    # 取款
    def withdraw(take_money):
        nonlocal current_money
        if take_money > current_money:
            return "余额不足"

        current_money -= take_money
        return current_money

    return deposit, withdraw


deposit, withdraw = create_account(100)
print(deposit(50))  # 150
print(withdraw(30))  # 120
print(withdraw(200))  # 余额不足
