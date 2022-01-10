import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = [] # empty list to add blocks to
        self.pending_transactions = [] # transactions stay here until they have been approved and added

        self.new_block(previous_hash="MY first hash xoxo", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1, # add to the chain, first block has idx of 1
            'timestamp': time(), # current time
            'transactions': self.pending_transactions, #points to where we store pending transactions
            'proof': proof, # comes from miner who thinks they have the valid nonce
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

#Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction) # pushes transaction to our pending_transactions queue where it sits until a new block is mined
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True) # turns block to json formatted string
        block_string = string_object.encode() # encodes string

        raw_hash = hashlib.sha256(block_string) # converts block_string to encrypted sha256 version
        hex_hash = raw_hash.hexdigest() #turn it into hex string

        return hex_hash


blockchain = Blockchain()
blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
blockchain.new_block(12345)

blockchain.new_transaction("Mike", "Alice", '1 BTC')
blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
blockchain.new_block(6789)

# print("Blockchain: ", blockchain.chain)
for block in blockchain.chain:
    print(block)