# Python Module 00: Basics with Object-Oriented Programming

## Overview
This module introduces Python programming with a focus on Object-Oriented Programming (OOP) concepts and command-line tools. Through practical exercises, you will build foundational skills, work with classes and objects, and implement interactive applications. 

## Exercises

### Exercise 00: Megaphone
**Objective:** Create a command-line program that transforms input text into uppercase.

- **Key Concepts:**
  - Command-line arguments (`sys.argv`).
  - String manipulation (`.upper()`).

- **Requirements:**
  - Accept one or more input strings.
  - Convert all input to uppercase.
  - If no input is provided, output: `* LOUD AND UNBEARABLE FEEDBACK NOISE *`.

#### Example Usage:
```bash
$ python megaphone.py "hello world"
HELLO WORLD
$ python megaphone.py
* LOUD AND UNBEARABLE FEEDBACK NOISE *
```

### Exercise 01: My Awesome PhoneBook
**Objective:** Build a basic phonebook application with add, search, and exit functionality.

- **Key Concepts:**
  - Object-Oriented Programming (OOP).
  - User input and output.
  - List-based data storage.

- **Requirements:**
  - Implement two classes:
    - **Contact**: Stores contact information.
    - **PhoneBook**: Manages a list of up to 8 contacts.
  - Support commands:
    - `ADD`: Add a new contact.
    - `SEARCH`: Display a list of contacts and allow detailed view.
    - `EXIT`: Quit the program.

#### Example Usage:
```bash
$ python phonebook.py
Enter command (ADD, SEARCH, EXIT): ADD
First Name: Alice
Last Name: Smith
Nickname: Ali
Phone Number: 123456789
Darkest Secret: Loves pizza
Enter command (ADD, SEARCH, EXIT): SEARCH
Index    |First Name|Last Name |Nickname  
0        |Alice     |Smith     |Ali       
Enter index to view details: 0
First Name: Alice
Last Name: Smith
Nickname: Ali
Phone Number: 123456789
Darkest Secret: Loves pizza
Enter command (ADD, SEARCH, EXIT): EXIT
```

### Exercise 02: The Job of Your Dreams
**Objective:** Implement an `Account` class to simulate basic bank account operations.

- **Key Concepts:**
  - Advanced OOP concepts (static methods and attributes).
  - Logging and timestamps.
  - Exception handling and user interaction.

- **Requirements:**
  - Implement the following in the `Account` class:
    - Static attributes for tracking global account statistics.
    - Instance attributes for account-specific data.
    - Methods for deposits, withdrawals, and account status.
    - Display a formatted log of all transactions and account information.

#### Example Usage:
```python
accounts = [Account(100), Account(200)]
accounts[0].makeDeposit(50)
accounts[1].makeWithdrawal(100)
Account.displayAccountsInfos()
```

## Learning Goals
- Understand and implement Object-Oriented Programming principles in Python.
- Develop command-line tools with Python.
- Work with static and instance attributes/methods.
- Format input and output to enhance user experience.

## Setup and Requirements
1. **Python Version:** Ensure you have Python 3.7+ installed.
2. **Development Tools:** Use your preferred code editor (e.g., VS Code, PyCharm, etc.).
3. **Run Instructions:**
   - Clone the repository containing the module.
   - Navigate to the exercise directory.
   - Run each exercise using the command:
     ```bash
     python <filename>.py
     ```

## Resources
Refer to the following resources to learn the required concepts:
- [Python's Official Documentation](https://docs.python.org/3/)
- [Real Python: Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [GeeksforGeeks: Python String Methods](https://www.geeksforgeeks.org/python-string-methods/)
- [Python argparse for Command-Line Arguments](https://docs.python.org/3/library/argparse.html)

---

## Contribution
Feel free to suggest improvements, report issues, or contribute new exercises by submitting a pull request to the repository.

## Author
- [Yassine AMRIRE](https://github.com/x86skwizer)
