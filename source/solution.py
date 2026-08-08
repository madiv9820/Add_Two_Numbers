'''
📄 solution.py

Acts as the main entry point for the Add Two Numbers problem, 
exposing the Solution class and coordinating multiple linked-list addition 
strategies—Three-Phase, Single-Pass, and Recursive — while 
using the Single-Pass approach as the selected implementation. 🔗➕🏆
'''

from typing         import Optional
from ListNode       import ListNode
from .approaches    import *

class Solution:
    def addTwoNumbers(
        self                    ,
        l1: Optional[ListNode]  ,
        l2: Optional[ListNode]  ,
    )   ->  Optional[ListNode]  :
        """
        ➕ Adds two numbers represented by reversed linked lists.

        The solution delegates the actual addition logic to one of the
        implementations available in the `approaches` package.

        Args:
            l1: First number represented as a reversed linked list.
            l2: Second number represented as a reversed linked list.

        Returns:
            Optional[ListNode]: The sum represented as a reversed
            linked list.
        """

        # 🔵 Approach 1: Three-Phase Linked List Addition
        #
        # Divides the addition into separate stages:
        #
        #   1️⃣ Process digits while both lists have nodes.
        #   2️⃣ Process remaining digits of the first list.
        #   3️⃣ Process remaining digits of the second list.
        #
        # Any remaining carry is handled after all digits are processed.
        approach_01: Three_Phase_LL_Add = Three_Phase_LL_Add(l1=l1, l2=l2)

        # 🟢 Approach 2: Single-Pass Linked List Addition
        #
        # Processes both operands in one unified traversal.
        #
        # Missing digits are treated as 0, allowing lists of different
        # lengths to be handled without separate processing phases.
        #
        # The carry is also included in the loop condition, allowing
        # a final carry to naturally become the most significant digit.
        approach_02: Single_Pass_LL_Add = Single_Pass_LL_Add(l1=l1, l2=l2)

        # 🟣 Approach 3: Recursive Linked List Addition
        #
        # Processes one digit at a time recursively while maintaining
        # the carry between recursive calls.
        #
        # The recursion terminates once both operands are exhausted
        # and no carry remains.
        approach_03: Recursive_LL_Add = Recursive_LL_Add(l1=l1, l2=l2)

        # 🏆 Selected Approach: Single-Pass Linked List Addition
        #
        # This approach provides the cleanest implementation by
        # handling equal-length lists, different-length lists, and
        # the final carry within a single traversal.
        return approach_02.add()
