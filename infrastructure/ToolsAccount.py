from datetime import datetime


class ToolsAccount:
    @staticmethod
    def time_exceeded(times):
        last_time = 'undefined'
        difference = 0
        for time in times:
            if last_time == 'undefined':
                last_time = time
                continue
            if difference == 0:
                difference = (time - last_time)
            else:
                difference = difference + (time - last_time)
        if (difference.seconds / 60) < 2:
            return True
        return False

    @staticmethod
    def append_time_operations(operations):
        times = []
        for operation in operations:
            time_string = operation.get('time')
            time_datetime_format = datetime.strptime(time_string.split(".")[0], '%Y-%m-%dT%H:%M:%S')
            times.append(time_datetime_format)
        return times

    @staticmethod
    def has_equals_operations(actual_operation, operations):
        list_equal = []

        for operation in operations:
            if operation.get('status') == 'SUCCESS' \
                    and actual_operation.get("merchant") == operation.get("merchant") \
                    and actual_operation.get("amount") == operation.get("amount"):
                list_equal.append(operation)
                list_equal.append(actual_operation)
                return list_equal
        return list_equal

    @staticmethod
    def without_keys(body, keys):
        return {x: body[x] for x in body if x not in keys}

    def append_equal_orders(self, operations):
        actual_operation = operations[-1]
        return self.has_equals_operations(actual_operation, operations[:-1])

    @staticmethod
    def last_three_success_operations(operations):
        success_operations = []
        for operation in operations:
            if operation.get('status') == 'SUCCESS' or operation.get('status') is None:
                success_operations.append(operation)
        return success_operations

    def verify_time(self, times):
        difference = times[-1] - times[-2]
        if difference.seconds / 60 > 2:
            return False
        if len(times) > 2:
            return self.time_exceeded(times[-4:-1])
        else:
            return False

    def check_if_order_exceeded_time(self, operations):
        last_three_success_operations = self.last_three_success_operations(operations)
        if len(last_three_success_operations) <= 3:
            return False
        times = self.append_time_operations(last_three_success_operations)
        return self.verify_time(times)

    def check_order_already_made(self, last_operations):
        equal_orders = self.append_equal_orders(last_operations)
        if len(equal_orders) == 0:
            return False
        time_operations = self.append_time_operations(equal_orders)
        return self.time_exceeded(time_operations) if len(time_operations) > 0 else False
