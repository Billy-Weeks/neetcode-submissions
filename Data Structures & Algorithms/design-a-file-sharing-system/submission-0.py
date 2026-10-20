class FileSharing:
    def __init__(self, m: int):
        self.users = {}
        self.owners = defaultdict(set)
        self.free = []
        self.next_id = 1
    def join(self, ownedChunks: List[int]) -> int:
        if self.free: uid = heapq.heappop(self.free)
        else: uid = self.next_id; self.next_id += 1
        self.users[uid] = set(ownedChunks)
        for chunk in ownedChunks: self.owners[chunk].add(uid)
        return uid
    def leave(self, userID: int) -> None:
        for chunk in self.users.pop(userID): self.owners[chunk].remove(userID)
        heapq.heappush(self.free, userID)
    def request(self, userID: int, chunkID: int) -> List[int]:
        result = sorted(self.owners[chunkID])
        if result:
            self.owners[chunkID].add(userID)
            self.users[userID].add(chunkID)
        return result
