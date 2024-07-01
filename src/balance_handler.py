def balance_handler(item: str, amount_given: int):
    items = {"water": 1, "soda": 2, "juice": 5}
    bills = [100, 50, 20, 10, 5, 1]
    change: dict = {}

    if item not in items:
        raise ValueError("Please choose between water, soda & juice")
    if amount_given < items.get(item, 0):
        raise ValueError("insuficient funds")

    balance = amount_given - items.get(item, 0)
    if balance == 0:
        return "No Change"

    for bill in bills:
        if bill > balance:
            continue
        n_change = balance // bill
        change[bill] = n_change
        balance = balance - (n_change * bill)

    return change
