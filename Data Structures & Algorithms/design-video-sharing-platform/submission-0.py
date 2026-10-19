class VideoSharingPlatform:
    def __init__(self):
        self.videos = {}
        self.free = []
        self.next_id = 0
    def upload(self, video: str) -> int:
        if self.free:
            i = heapq.heappop(self.free)
        else:
            i = self.next_id
            self.next_id += 1
        self.videos[i] = [video, 0, 0, 0]
        return i
    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
            del self.videos[videoId]
            heapq.heappush(self.free, videoId)
    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.videos:
            return "-1"
        v = self.videos[videoId]
        v[3] += 1
        return v[0][startMinute:endMinute + 1]
    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId][1] += 1
    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId][2] += 1
    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        return self.videos[videoId][1:3] if videoId in self.videos else [-1]
    def getViews(self, videoId: int) -> int:
        return self.videos[videoId][3] if videoId in self.videos else -1
