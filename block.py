import time
import hashlib

# index (master)
# transaction => hash
# previous => hash
# timestamp

class Block(object):

    def __init__(self, index, transaction, previous):
        self.index = index
        self.transaction = transaction
        self.previous = previous
        self.timestamp = time.time()

    @property
    def getHashBlock(self):
        data = "{}{}{}{}".format(self.index, self.transaction, self.previous, self.timestamp)
        return hashlib.sha256(data.encode()).hexdigest()