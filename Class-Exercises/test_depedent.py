from bank import BankAccount

def test_deposit_increases_balance():
    account = BankAccount(balance=1000)
    account.deposit(500)
    assert account.balance == 1500

def test_withdraw_decreases_balance():
    account = BankAccount(balance=1000)
    account.withdraw(300)
    assert account.balance == 1200