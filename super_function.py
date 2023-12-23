class Computer(object):
    def __init__(self, ram, storage) -> None:
        self.ram = ram
        self.storage = storage
        print("Computer class constructor called")

    def display(self):
        print(f"The computer ram is {self.ram}, and storage {self.storage}")

class Mobile(Computer):
    def __init__(self, ram, storage, model) -> None:
        super().__init__(ram, storage)
        # super().display()
        self.model = model

    def display(self):
        return super().display()


apple = Mobile("8GB", "512GB","IphoneX")
print(apple.__dict__)
print(apple.display())