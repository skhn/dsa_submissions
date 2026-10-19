class LinkedList:
    
    def __init__(self):
        self.dq = deque()
    
    def get(self, index: int) -> int:
        if 0 <= index < len(self.dq):
            return self.dq[index]
        return -1
        
    def insertHead(self, val: int) -> None:
        self.dq.appendleft(val)

    def insertTail(self, val: int) -> None:
        self.dq.append(val)

    def remove(self, index: int) -> bool:
        if 0 <= index < len(self.dq):
            del self.dq[index]
            return True
        return False

    def getValues(self) -> List[int]:
        return list(self.dq)
        
