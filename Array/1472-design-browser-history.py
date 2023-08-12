class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pointer = 0 
        

    def visit(self, url: str) -> None:
        # Move the stack along and delete the old history. 
        self.stack = self.stack[:self.pointer + 1]
        # append the url to it
        self.stack.append(url)
        # move the pointer location
        self.pointer += 1 
        

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer - steps)
        return self.stack[self.pointer]
        

    def forward(self, steps: int) -> str:
            self.pointer = min(len(self.stack)-1, self.pointer + steps)
            return self.stack[self.pointer]    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)