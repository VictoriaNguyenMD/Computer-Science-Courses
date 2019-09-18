class GetCalled():
    def __init__(self):
        self.v1 = -459
        self.v2 = 585
        self.v3 = 10101
        
    def call(self):
        self.v1 += self.v2
        self.v3 += self.v2 * 2
        self.v2 = self.v2 // 2 + self.v1
