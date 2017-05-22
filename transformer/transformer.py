class Transform:
    def __init__(self, number):
        self.number = number

    def transform(self, number):
        self.number = number
        new_number = self.number + 1
        return new_number
