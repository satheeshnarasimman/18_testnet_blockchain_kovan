import os
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account
from pathlib import Path
from getpass import getpass

load_dotenv()

w3= Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer= 0)

private_key = os.getenv("NODE3_PRIVATE_KEY")
my_account= Account.from_key(private_key)

with open (Path ('./UTC--2021-01-31T13-44-10.965Z--88cadcb70941224984a44c8cbdbbe4341702ba85')) as keyfile:
    encrypted_key= keyfile.read()
    private_key= w3.eth.account.decrypt(encrypted_key, getpass ("Enter keystore password:"))
    my_account2= Account.from_key(private_key)
    
print (my_account2.address)

def create_raw_txn(account, address_to, amount):
    gas_estimate= w3.eth.estimateGas ({'from': account.address, 
                                      'to': address_to,
                                      'value': amount})
    return {
        'from': account.address,
        'to': address_to,
        'value': amount,
        'gasPrice': w3.eth.gasPrice,
        'gas': gas_estimate,
        'nonce': w3.eth.getTransactionCount(account.address)
    }

def send_txn (account, address_to, amount):
    txn= create_raw_txn(account, address_to, amount)
    signed_txn= account.sign_transaction(txn)
    result= w3.eth.sendRawTransaction (signed_txn.rawTransaction)
    
    print (result.hex())
    return result.hex()

transaction_id= send_txn (my_account2, my_account, 10)

# print (w3.eth.getTransactionReceipt(""))