from bank import BankAccount
def test_deposit_increases_balance():
    account = BankAccount(balance=1000)
    new_balance = account.deposit(500)
    assert new_balance == 1500

def test_withdraw_decreases_balance():
    account = BankAccount(balance=1000)
    new_balance = account.withdraw(300)
    assert new_balance == 700

def test_everything_at_once():
    account = BankAccount(balance=1000)
    account.deposit(200)
    account.withdraw(300)
    account.deposit(100)
    assert account.balance == 1300
