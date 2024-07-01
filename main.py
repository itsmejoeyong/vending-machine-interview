from src.balance_handler import balance_handler


def main():
    item = input("Choose between water, soda & juice: ")
    change = input("enter your note: ")
    try:
        change = int(change)
    except Exception:
        raise ValueError("Notes can only be numerical")

    balance_dict = balance_handler(item, change)
    if type(balance_dict) is dict:
        for note, amount in balance_dict.items():
            print(f"returning {amount}x RM{note} note.")
    else:
        print(balance_dict)


if __name__ == "__main__":
    main()
