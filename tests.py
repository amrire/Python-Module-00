#!/usr/bin/python3
from account import Account


if __name__ == "__main__":
    # Create accounts
    accounts = [Account(42), Account(54), Account(957), Account(432),
                Account(1234), Account(0), Account(754), Account(16576)]

    # Display initial account statuses
    Account.displayAccountsInfos()
    for account in accounts:
        account.displayStatus()

    # Perform deposits
    deposits = [5, 765, 564, 2, 87, 23, 9, 20]
    for account, deposit in zip(accounts, deposits):
        account.makeDeposit(deposit)

    # Display account statuses after deposits
    Account.displayAccountsInfos()
    for account in accounts:
        account.displayStatus()

    # Perform withdrawals
    withdrawals = [321, 34, 657, 4, 76, 275, 657, 7654]
    for account, withdrawal in zip(accounts, withdrawals):
        account.makeWithdrawal(withdrawal)

    # Display final account statuses
    Account.displayAccountsInfos()
    for account in accounts:
        account.displayStatus()
