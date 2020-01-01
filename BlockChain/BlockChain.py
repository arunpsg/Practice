import hashlib
import time


def calc_hash(self, hash_str):
    sha = hashlib.sha256()

    hash_str = hash_str.encode('utf-8')
    # hash_str = "We are going to encode this string of data!".encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)


block_chain = []


def add_block(self, data):
    if not block_chain:
        block_chain.append(Block(time.time(), data, "0"))
        return block_chain
    else:
        timestamp = time.time()
        previous_hash = block_chain[-1].hash
        block_chain.append(Block(timestamp, data, previous_hash))


def print_blockchain():
    out_string = ""
    for item in block_chain:
        out_string += "(Timestamp : " + item.timestamp + ", Data : " + item.data + ", SHA256 Hash : " + item.hash + ", Prev_Hash : " + item.previous_hash + ") <- "
    print(out_string)
