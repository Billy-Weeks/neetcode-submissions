class MyHashSet:

    def __init__(self):
        # Instatiate empty set
        self.emptySet = set()

    def add(self, key: int) -> None:
        self.emptySet.add(key)

    def remove(self, key: int) -> None:
        if key in self.emptySet:
            self.emptySet.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.emptySet:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)