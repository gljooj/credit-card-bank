# Welcome to Authorizer 

This Project was created with the objective to carry out banking transactions following the rules proposed by the bank instituition.
🏦
## How to Run 🎡

### Preparing the environment 💻
How is nothing too complex the environment is more prepared for perform tests

Execute:
(os & Linux)

#### 1 - `virtualenv .venv` 
#### 2 - `source .venv/bin/activate` 

(Windows)

#### 1 - `python -m venv .venv` 
#### 2 - `source .venv/Scripts/activate` 

#### 3 - `pip install -r requirements.txt` 

### To execute the project you must execute on the root project the follow command:
`python3 authorizator.py < operations` 

## To verify all the tests proposed you must: 
access the **tests/test.py** and execute the run(pytest) with command:
`python3 -m unittest tests/test.py` 
 or use a framework (preference pycharm)
 here you you will have others scenarios

# Explaining the project

## infrastructure/Authorizer.py
This file is the first authorization layer, where the establishment/credit card machine have the freedom to know 
the status of client's credit card or know if is a valid credit card.

# infrastructure/Account.py
## Here is the core
This file is the account layer, here the app execute the process of captures from credit card errors for example:
**Limit to purchase, time for a request to another, duplicated purchase.**
# Businness rules:
**All the Scenarios is on tests/tmp_operations/operations_to_test.py**

```
first_operation = """{"account": {"active-card": true, "available-limit": 100}}
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:00.000Z"}}"""
```
### account-not-initialized
```
second_operation = """{"transaction": {"merchant": "Uber Eats", "amount": 25, "time": "2020-12-01T11:07:00.000Z"}}
{"account": {"active-card": true, "available-limit": 225}}
{"transaction": {"merchant": "Uber Eats", "amount": 25, "time": "2020-12-01T11:07:00.000Z"}}"""
```
### card-not-active
```
third_operation = """{"account": {"active-card": false, "available-limit": 100}}
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:00.000Z"}}
{"transaction": {"merchant": "Habbib's", "amount": 15, "time": "2019-02-13T11:15:00.000Z"}}"""
```
### insufficient-limit
```
fourth_operation = """{"account": {"active-card": true, "available-limit": 1000}}
{"transaction": {"merchant": "Vivara", "amount": 1250, "time": "2019-02-13T11:00:00.000Z"}}
{"transaction": {"merchant": "Samsung", "amount": 2500, "time": "2019-02-13T11:00:01.000Z"}}
{"transaction": {"merchant": "Nike", "amount": 800, "time": "2019-02-13T11:01:01.000Z"}}"""
```
### high-frequency-small-interval
```
fifth_operation = """{"account": {"active-card": true, "available-limit": 100}}
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:00.000Z"}}
{"transaction": {"merchant": "Habbib's", "amount": 20, "time": "2019-02-13T11:00:01.000Z"}}
{"transaction": {"merchant": "McDonald's", "amount": 20, "time": "2019-02-13T11:01:01.000Z"}}
{"transaction": {"merchant": "Subway", "amount": 20, "time": "2019-02-13T11:01:31.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 10, "time": "2019-02-13T12:00:00.000Z"}}"""
```
### doubled-transaction
```
sixth_operation = """{"account": {"active-card": true, "available-limit": 100}}
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:00.000Z"}}
{"transaction": {"merchant": "McDonald's", "amount": 10, "time": "2019-02-13T11:00:01.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:02.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 15, "time": "2019-02-13T11:00:03.000Z"}}"""
```
### Multiple errors
```
seventh_operation = """{"account": {"active-card": true, "available-limit": 100}}
{"transaction": {"merchant": "McDonald's", "amount": 10, "time": "2019-02-13T11:00:01.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:02.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 5, "time": "2019-02-13T11:00:07.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 5, "time": "2019-02-13T11:00:08.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 150, "time": "2019-02-13T11:00:18.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 190, "time": "2019-02-13T11:00:22.000Z"}}
{"transaction": {"merchant": "Burger King", "amount": 15, "time": "2019-02-13T12:00:27.000Z"}}"""
```

#### 1. No transaction should be accepted unless the account has been initialized: `account-not-initialized`.
#### 2. No transaction should be accepted when the card is not active: `card-not-active`.
#### 3. The transaction amount should not exceed the available limit: `insufficient-limit`.
#### 4. There should be no more than 3 transactions from any merchant within a 2-minute interval: `high-frequency-small-interval`.
#### 5. There should be no more than 1 similar transaction (same amount and merchant) within a 2-minute interval: `double-transaction`.

# infrastructure/ToolsAccount.py
This file it's like a helper for the Account, here has some tools and checkers for help the Account.
