class MyHashMap:

    def __init__(self):

        # Create empty dictionary to add/remove from 
        self.my_dict = {}

    def put(self, key: int, value: int) -> None:
        self.my_dict[key] = value
        

    def get(self, key: int) -> int:
        if key in self.my_dict:
            return self.my_dict[key]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.my_dict:
            self.my_dict.pop(key, None)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)