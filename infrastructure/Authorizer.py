import json
from infrastructure.Account import Account


class Authorizer:
    def __init__(self, last_bank_account):
        self.last_bank_account = last_bank_account

    def create_account(self, account_bank):
        json_account = json.loads(account_bank)
        new_account = json_account.get('account', '')
        if self.last_bank_account:
            return Account(self.last_bank_account, violations=["account-already-initialized"])

        self.last_bank_account = Account(new_account)
        return self.last_bank_account

    def verify_possibles_errors(self):
        if self.last_bank_account == {}:
            return {"has_error": True, "type": "not_initialized", "violation": "account-not-initialized"}

        if not self.last_bank_account.active:
            return {"has_error": True, "type": "account_deactivated", "violation": "card-not-active"}
        return {"has_error": False}

    def error(self, type_error):
        if type_error.get('type') == 'not_initialized':
            temporary_account = Account(account={}, violations=[type_error.get('violation')])
            return temporary_account.json_body_fail()
        self.last_bank_account.violations.append(type_error.get('violation'))
        return self.last_bank_account.json_body()

    def authorization_operations(self, bank_account_client, operation):
        has_error = self.verify_possibles_errors()
        if has_error.get("has_error"):
            return self.error(has_error)

        return bank_account_client.check_operation(operation)

