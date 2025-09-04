from pathlib import Path
import json
import getpass
from eth_account import Account

KEY = Path(".keystore.json")

def main():
    pk = getpass.getpass("your pk: ") #input like without showing in terminal
    acc = Account.from_key(pk)

    password = getpass.getpass("password: ")
    encryptPass = acc.encrypt(password)

    print(f"saving to {KEY}")
    with KEY.open("w") as fp:
        json.dump(encryptPass, fp)

if __name__ == "__main__":
    main()