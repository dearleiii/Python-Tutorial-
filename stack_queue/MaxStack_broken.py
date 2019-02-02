class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.maxstack) == 0 or self.maxstack[-1][0] <= x: 
            self.maxstack.append((x, len(self.maxstack)))
        else: 
            self.maxstack.append((self.maxstack[-1][0], self.maxstack[-1][1]))
            
        #print(self.stack)
        #print(self.maxstack)

    def pop(self):
        """
        :rtype: int
        """
        number = self.stack.pop()
        self.maxstack.pop()
        return number

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxstack[-1][0]

    def popMax(self):
        """
        :rtype: int
        """
        max_num, index = self.maxstack[-1]
        back_stack = []
        while self.stack and self.stack[-1] != max_num:
            self.maxstack.pop()
            back_stack.append(self.stack.pop())
        
        self.stack.pop()
        self.maxstack.pop()
        
        # push back the new values 
        for num in back_stack: 
            self.push(num)
        
        return max_num



class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.maxstack) == 0 or self.maxstack[-1][0] <= x: 
            self.maxstack.append((x, len(self.maxstack)))
        else: 
            self.maxstack.append((self.maxstack[-1][0], len(self.maxstack)))
            
        #print(self.stack)
        #print(self.maxstack)

    def pop(self):
        """
        :rtype: int
        """
        number = self.stack.pop()
        self.maxstack.pop()
        return number

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxstack[-1][0]

    def popMax(self):
        """
        :rtype: int
        """
        max_num, index = self.maxstack[-1]
        self.maxstack.pop()
        self.stack.pop(index)
        return max_num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
