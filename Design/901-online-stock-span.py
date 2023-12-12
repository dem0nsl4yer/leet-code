# Basic solution. 

class StockSpanner:

    def __init__(self):
        self.stockspanner = []

    def next(self, price: int) -> int:
        k = 1
        for i in range(len(self.stockspanner)-1, -1, -1):
            if self.stockspanner[i] <= price:
                k += 1
            else:
                break
        self.stockspanner.append(price)
        #print(self.stockspanner)
        return k
    
# Need faster solution - cache and mempool. 

class StockSpanner:

    def __init__(self):
        self.stockspanner = []
        self.span_cache = []

    def next(self, price: int) -> int:
        span = 1

        while self.stockspanner and price >= self.stockspanner[-1][0]:
            span += self.stockspanner.pop()[1]

        self.stockspanner.append((price, span))
        return span
