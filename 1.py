import hashlib
import uuid

class Block:
    def _init_(self, product_details, previous_hash):
        self.product_details = product_details
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.product_details).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

blockchain = Blockchain()

# Add product details along with a unique identification code generated by the manufacturer
product_details = "Product Details: iPhone X, Price: $1000, ID: " + str(uuid.uuid1())
blockchain.add_block(Block(product_details, ""))

product_details = "Product Details: MacBook Pro, Price: $1500, ID: " + str(uuid.uuid1())
blockchain.add_block(Block(product_details, ""))

print("Is Blockchain Valid? ", blockchain.is_chain_valid())

for block in blockchain.chain:
    print("Product Details: ", block.product_details)
    print("Previous Hash: ", block.previous_hash)
    print("Current Hash: ", block.hash)
    print("\n")
