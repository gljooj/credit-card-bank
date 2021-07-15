import json
from infrastructure.ToolsAccount import ToolsAccount


class Account:
    def __init__(self, account: json, violations=None) -> None:
        if violations is None:
            violations = []
        self._account = account
        self._historic = []
        self._active = account.get('active-card', False)
        self._limit = account.get('available-limit', 0)
        self.last_operations = []
        self.actual_operation = {}
        self.status = ''
        self._violations = violations
        self.tools = ToolsAccount()

    @property
    def active(self):
        return self._active

    @property
    def violations(self):
        return self._violations

    @violations.setter
    def violations(self, violation):
        self._violations.append(violation)

    @staticmethod
    def translate_operation(operation):
        json_operation = json.loads(operation)
        return json_operation.get('transaction', '')

    def _set_status_operation(self, has_error):
        status = 'SUCCESS'
        if has_error:
            status = 'FAILED'
        self._historic[-1]['status'] = status

    def json_body(self):
        body = {"account": {"active-card": self._active,
                            "available-limit": self._limit},
                "violations": self._violations}

        self._violations = []
        return body

    def json_body_fail(self):
        body = {"account": {},
                "violations": self._violations}
        self._violations = []
        return body

    def _verify_difference(self, operation):
        has_error = self._verify_has_errors()
        self._set_status_operation(has_error)
        if operation.get('amount') < self._limit:
            self._discount_difference(operation.get('amount')) if not has_error else None
        else:
            self._set_status_operation(has_error=True)
            self._violations.append("insufficient-limit")

    def _discount_difference(self, amount):
        self._limit = self._limit - amount

    def _check_time_operations(self):
        return self.tools.check_if_order_exceeded_time(self.last_operations)

    def _has_high_frequency(self):
        if len(self.last_operations) < 3:
            return False
        return self._check_time_operations()

    def _has_doubled_transaction(self):
        return self.tools.check_order_already_made(self._historic)

    def _verify_has_errors(self):
        has_error = False
        if self._has_high_frequency():
            self._violations.append("high-frequency-small-interval")
            has_error = True

        if self._has_doubled_transaction():
            self._violations.append("doubled-transaction")
            has_error = True

        return has_error

    def _verify_operation(self, operation):
        self.actual_operation = operation
        self.last_operations.append(self.actual_operation)
        self._historic.append(self.actual_operation)
        self._verify_difference(operation)

    def check_operation(self, operation):
        operation = self.translate_operation(operation)
        self._verify_operation(operation)

        return self.json_body()
