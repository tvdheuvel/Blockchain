# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:01:51 2022
@author: vandenheuvel
Basic Blockchain in Python
inpired by: Will Assad https://www.youtube.com/channel/UCX4QtKIp00r3ILeGuiYRxqw
"""

# imports 
from hashlib import sha256

# create a hash function
def hashfunction(*args):
    hash = ""
    h = sha256()

    # hash each argument passed to the function and create string
    for arg in args:
        hash += str(arg)

    h.update(hash.encode('utf-8'))
    return h.hexdigest()

# Create the block class
class Block():

    def __init__(self, blocknumber=0, previous_hash="0"*64, data=None, nonce=0): # set tge default nonce to 0
        self.data = data
        self.blocknumber = blocknumber
        self.previous_hash = previous_hash
        self.nonce = nonce

    def hash(self):
        return hashfunction(
            self.blocknumber,
            self.previous_hash,
            self.data,
            self.nonce
        )

    # allows to print the block
    def __str__(self):
        return str(f"Block#: {self.blocknumber}\nHash: {self.hash()}\nPrevious: {self.previous_hash}\nData: {self.data}\nNonce: {self.nonce}\n" 
        )


# Create the chain of the blocks
class Blockchain():
    
    difficulty = 4

    def __init__(self):
        self.chain = []

    def add(self, block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    # This is the mining function
    def mine(self, block):
        try: 
            block.previous_hash = self.chain[-1].hash()
        except IndexError: 
            pass

        # find the hash with the right difficulty
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                block.nonce += 1

    def validation(self):
        
        for i in range(1,len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            
            if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
                return False

        return True


# test section
def main():
    blockchain = Blockchain()
    database = ["hello", "world", "tesla", "rocket"]

    num = 0

    for data in database:
        num += 1
        blockchain.mine(Block(num, data=data))

    for block in blockchain.chain:
        print(block)

    # print(blockchain.validation())

    # blockchain.chain[2].data = "NEW DATA"
    # blockchain.mine(blockchain.chain[2])
    # print(blockchain.validation())


if __name__ == '__main__':
    main()