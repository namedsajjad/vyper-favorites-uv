import os

from vyper import compile_code
from web3 import Web3, EthereumTesterProvider

# from dotenv import load_dotenv
# load_dotenv()

ADDRESS = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
# PRIVATE = os.getenv("MY_PRIVATE")

def main():
    print("\n------------------> DEPLOYING...")
    # print(f"Address: {ADDRESS},\nPrivate Key: {PRIVATE}\n")
    with open("favorites.vy", "r") as f_file:
        f_code = f_file.read()
        f_compiled = compile_code(f_code, output_formats=["bytecode", "abi"])

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    f_contract = w3.eth.contract(
        bytecode=f_compiled["bytecode"], 
        abi=f_compiled["abi"]
    )

    nonce = w3.eth.get_transaction_count(ADDRESS)
    tx = f_contract.constructor().build_transaction(
        {
            "from": ADDRESS,
            "nonce": nonce
        }
    )
    # print(tx)

    pk = decryptKey()
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=pk)
    print(signed_tx)
    print("\n------------------> Sending TX:")

    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f'hash: {tx_hash}')
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"\n------------------> DONE!\nTX ADDRESS: {tx_receipt.contractAddress}\n")

def decryptKey() -> str:
    from encrypt_key import KEY
    from getpass import getpass
    from eth_account import Account

    with open(KEY,"r") as fp:
        encrypted = fp.read()
        password = getpass("password? ")
        key = Account.decrypt(encrypted, password)
        print(key)
        return key

if __name__ == "__main__":
    main()
