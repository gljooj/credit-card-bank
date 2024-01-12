import fileinput

from infrastructure.Authorizer import Authorizer

account = {}
auth = Authorizer(account)
bank_account = object

for operation in fileinput.input():
    operation = operation.replace('\n', '')
    if "account" in operation:
        account = operation
        bank_account = auth.start_account(account)
        print(f"bank account: {bank_account.json_body()} \n")
        continue

    print(f"operation: {operation} \n"
          f'operation_response: {auth.authorization_operations(bank_account, operation)} \n'
          )
