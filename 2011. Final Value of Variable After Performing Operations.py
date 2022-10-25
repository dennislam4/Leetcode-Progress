class Solution(object):
    def finalValueAfterOperations(self, operations):
        value = 0
        for index in range(len(operations)):
            curr = operations[index]
            if curr == "++X" or curr == "X++":
                value += 1
            else:
                value -= 1
        return value

