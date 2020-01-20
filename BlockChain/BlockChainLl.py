import hashlib
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            # out_string += str(cur_head.value) + " -> "
            out_string += str("(Timestamp : " + str(item.timestamp) + ", Data : " + str(item.data) + ", SHA256 Hash : " + str(item.hash) + ", Prev_Hash : " + str(item.previous_hash) + ") <- ")
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Block(time.time(), value, "0")
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Block(time.time(),value, node.hash)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
        
    def __iter__(self):
        current = self.head
    
        while current is not None:
            yield current
            current = current.next


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def calc_hash(self, hash_str):
        sha = hashlib.sha256()

        hash_str = hash_str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()
        
    def __repr__(self):
        return str(self.data)

block_chain = LinkedList()



def add_block(data):
    if not data:
        print("Please enter valid data")
        return None
    else:
        data = str(data)

    block_chain.append(data)


def print_blockchain():
    out_string = ""
    if block_chain:
        for item in block_chain:
            print(item)
    else:
        print("Block Chain is empty!")

#TestCase 1
add_block("1234")
print_blockchain()
# Expected output:
# (Timestamp : 1578072294.6485157, Data : 1234, SHA256 Hash : 03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4, Prev_Hash : 0) <-

#TestCase 2
add_block("")
print_blockchain()
# Expected output:
# Please enter valid data

#TestCase 2
add_block("testing")
add_block("development")
add_block("analysis")
print_blockchain()
# (Timestamp : 1578071931.3984785, Data : testing, SHA256 Hash : cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90, Prev_Hash : 0) <-
# (Timestamp : 1578071931.3984785, Data : development, SHA256 Hash : 875b9380866e9d56e7110b0ee310962c16d9d4ae103f829d62bdffd2cbe7c61d, Prev_Hash : cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90) <-
# (Timestamp : 1578071931.3984785, Data : analysis, SHA256 Hash : f44e85c4b8ea2addc796f8beab6600e801d767ccd26c800dce6d88fdaa5eb4e6, Prev_Hash : 875b9380866e9d56e7110b0ee310962c16d9d4ae103f829d62bdffd2cbe7c61d) <-
