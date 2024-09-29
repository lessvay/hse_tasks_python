# https://leetcode.com/problems/basic-calculator-ii/description/?envType=problem-list-v2&envId=string&status=SOLVED
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek at empty stack")

    def size(self):
        return len(self.items)


class Solution(object):
    def tokenizer(self, string):
        current_token = ""
        tokens = []
        for i in range(len(string)):
            current_char = string[i]
            if current_char.isdigit():
                current_token += current_char
            else:
                if current_token != "":
                    tokens.append(current_token)
                    current_token = ""
                if current_char != " ":
                    tokens.append(current_char)

        if current_token != "":
            tokens.append(current_token)

        return tokens

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack_for_numbers = Stack()
        stack_for_operation = Stack()
        current_index = 0
        tokens = self.tokenizer(s)
        while current_index < len(tokens):
            current_character = tokens[current_index]

            if current_character.isdigit():
                stack_for_numbers.push(int(current_character))
                current_index += 1
            else:

                priority = 2 if current_character in "/*" else 1

                while (
                    not stack_for_operation.is_empty()
                    and priority <= stack_for_operation.peek()["priority"]
                ):
                    second_number = stack_for_numbers.pop()
                    first_number = stack_for_numbers.pop()
                    operation = stack_for_operation.pop()["current_character"]
                    result = self.math(first_number, second_number, operation)
                    stack_for_numbers.push(result)

                stack_for_operation.push(
                    {"current_character": current_character, "priority": priority}
                )
                current_index += 1

        # Обработка оставшихся операций
        while not stack_for_operation.is_empty():
            second_number = stack_for_numbers.pop()
            first_number = stack_for_numbers.pop()
            operation = stack_for_operation.pop()["current_character"]
            result = self.math(first_number, second_number, operation)
            stack_for_numbers.push(result)

        return stack_for_numbers.peek()

    def math(self, first_number, second_number, operation):
        if operation == "+":
            return first_number + second_number
        if operation == "-":
            return first_number - second_number
        if operation == "*":
            return first_number * second_number
        if operation == "/":
            return first_number / second_number
