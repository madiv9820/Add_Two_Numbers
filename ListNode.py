from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val    : int                   = val
        self.next   : Optional[ListNode]    = next