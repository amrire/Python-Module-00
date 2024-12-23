#!/usr/bin/python3
import time

class Account:
    """
    A class to represent a bank account with static tracking for all accounts.
    """

    # Static attributes
    _nbAccounts = 0
    _totalAmount = 0
    _totalNbDeposits = 0
    _totalNbWithdrawals = 0

    @staticmethod
    def _displayTimestamp():
        """
        Display the current timestamp in the format [YYYYMMDD_HHMMSS].
        """
        print(f"[{time.strftime('%Y%m%d_%H%M%S')}]", end=" ")

    @staticmethod
    def displayAccountsInfos():
        """
        Display global statistics for all accounts.
        """
        Account._displayTimestamp()
        print(f"accounts:{Account._nbAccounts};total:{Account._totalAmount};"
              f"deposits:{Account._totalNbDeposits};withdrawals:{Account._totalNbWithdrawals}")

    def __init__(self, initial_deposit):
        """
        Initialize an account with an initial deposit and update static statistics.
        """
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be a positive amount.")
        self._accountIndex = Account._nbAccounts
        self._amount = initial_deposit
        self._nbDeposits = 0
        self._nbWithdrawals = 0
        Account._nbAccounts += 1
        Account._totalAmount += initial_deposit
        Account._displayTimestamp()
        print(f"index:{self._accountIndex};amount:{self._amount};created")

    def __del__(self):
        """
        Cleanup method called when an account is deleted. Updates static statistics.
        """
        Account._nbAccounts -= 1
        Account._totalAmount -= self._amount
        Account._displayTimestamp()
        print(f"index:{self._accountIndex};amount:{self._amount};closed")

    def displayStatus(self):
        """
        Display the current status of the account.
        """
        Account._displayTimestamp()
        print(f"index:{self._accountIndex};amount:{self._amount};"
              f"deposits:{self._nbDeposits};withdrawals:{self._nbWithdrawals}")

    def makeDeposit(self, deposit):
        """
        Add funds to the account and update static statistics.
        """
        if deposit < 0:
            raise ValueError("Deposit amount must be positive.")

        self._amount += deposit
        self._nbDeposits += 1
        Account._totalAmount += deposit
        Account._totalNbDeposits += 1

        Account._displayTimestamp()
        print(f"index:{self._accountIndex};p_amount:{self._amount - deposit};"
              f"deposit:{deposit};amount:{self._amount};nb_deposits:{self._nbDeposits}")

    def makeWithdrawal(self, withdrawal):
        """
        Withdraw funds from the account if sufficient balance is available. Update static statistics.
        """
        if withdrawal < 0:
            raise ValueError("Withdrawal amount must be positive.")

        Account._displayTimestamp()
        print(f"index:{self._accountIndex};p_amount:{self._amount}", end="")

        if withdrawal > self._amount:
            print(";withdrawal:refused")
            return False

        self._amount -= withdrawal
        self._nbWithdrawals += 1
        Account._totalAmount -= withdrawal
        Account._totalNbWithdrawals += 1

        print(f";withdrawal:{withdrawal};amount:{self._amount};nb_withdrawals:{self._nbWithdrawals}")
        return True
