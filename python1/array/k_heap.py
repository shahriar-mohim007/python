def special_tree( values, k ) :
    ####### DO NOT MODIFY THE CODE BELOW #######
    myTree = MySpecialTree(values)
    soln = []
    for val in range(k):
        soln.append(myTree.pop_max_value())

    return soln
    ####### DO NOT MODIFY THE CODE ABOVE #######

class MySpecialTree():
    def __init__(self, values=None):
        self.data = values or []
        for x in range(len(values)//2, -1, -1):
            self.__max_treeify__(x)

    def parent(self, x):
        return x >> 1

    def left_child(self, x):
        return (x << 1) + 1

    def right_child(self, x):
        return (x << 1) + 2

    def __max_treeify__(self, x):
        largest = x
        left = self.left_child(x)
        right = self.right_child(x)

        if left < len(self.data) and self.data[left] > self.data[largest]:
            largest = left
        if right < len(self.data) and self.data[right] > self.data[largest]:
            largest = right

        if largest != x:
            self.data[x], self.data[largest] = self.data[largest], self.data[x]
            self.__max_treeify__(largest)

    def pop_max_value(self):
        if not self.data:
            return None

        max_value = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.__max_treeify__(0)
        return max_value
    









# def special_tree( values, k ) :
# 	####### DO NOT MODIFY THE CODE BELOW #######
#         myTree = MySpecialTree(values)
#         soln = []
#         for val in range(k):
#             soln.append(myTree.pop_max_value())

#         return soln
# 	####### DO NOT MODIFY THE CODE ABOVE #######

# class MySpecialTree():
# 		def __init__(self, values=None):
# 			self.data = values or []
# 			for x in range(len(values)//2, -1, -1):
# 				self.__max_treeify__(x)

# 		def parent(self, x):
# 			return x >> 1

# 		def left_child(self, x):
# 			return (x << 1) + 1

# 		def right_child(self, x):
# 			return (x << 1) + 2

# 		def __max_treeify__(self, x):
# 			pass

# 		def pop_max_value(self):
# 			pass