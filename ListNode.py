'''
📄 ListNode.py — File Description

Defines the reusable ListNode class used to represent nodes in a singly linked list, 
storing an integer value and a reference to the next node. 🔗
'''

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val    : int                   = val
        self.next   : Optional[ListNode]    = next
