# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:01:51 2022

@author: vandenheuvel

Basic Blockchain in Python

inpired by: https://geekflare.com/create-a-blockchain-with-python/

"""


import hashlib


class QuantCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}" #store the previous hash and transaction list, simplification from real blockchain
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() # create the immutable hash in hexadecimal format


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(QuantCoinBlock("0", ['Genesis Block']))
    
    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(QuantCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]
    
    
t1 = "Jane sends 5 QC to Mike"
t2 = "Tim sends 2.5 QC to Jane"
t3 = "Jane sends 11 QC to Kelsey"
t4 = "Kelsey sends 9.5 QC to Charlie"
t5 = "Mike sends 20 QC to Dawn"
t6 = "Dawn sends 1 QC to Charlie"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

myblockchain.display_chain()