import fileinput

from infrastructure.Authorizer import Authorizer

account = {}
auth = Authorizer(account)
bank_account = object

for operation in fileinput.input():
    operation = operation.replace('\n', '')
    if "account" in operation:
        account = operation
        bank_account = auth.create_account(account)
        print(bank_account.json_body())
        continue
    print(auth.authorization_operations(bank_account, operation))

