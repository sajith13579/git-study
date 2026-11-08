class bank:
    next_account_number=1001
    def __init__(self,name,starting_bal):
        self.name=name
        print(f"{name} started bank account ")

k=bank("Sajit",100)
