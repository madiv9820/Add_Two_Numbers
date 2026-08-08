from typing         import Optional
from ListNode       import ListNode
from .approaches    import *


class Solution:
    def addTwoNumbers(
        self                    ,
        l1: Optional[ListNode]  ,
        l2: Optional[ListNode]  ,
    ) -> Optional[ListNode]:
        """
        ➕ Adds two numbers represented by linked lists.

        The solution delegates the actual addition logic to the
        implementations defined inside the `approaches` package.

        Args:
            l1: First number represented as a reversed linked list.
            l2: Second number represented as a reversed linked list.

        Returns:
            Optional[ListNode]: The sum represented as a reversed
            linked list.
        """

        # 🔵 Approach 1: Three-Phase Linked List Addition
        #
        # Processes the addition in separate phases:
        #   1️⃣ Digits available in both lists.
        #   2️⃣ Remaining digits of the first list.
        #   3️⃣ Remaining digits of the second list.
        #
        # The final carry is handled after all digits are processed.
        approach_01: Three_Phase_LL_Add = Three_Phase_LL_Add(l1=l1, l2=l2)

        # 🟢 Approach 2: Single-Pass Linked List Addition
        #
        # Processes both lists in one unified traversal. Missing digits
        # are treated as 0, allowing different-length lists and the
        # final carry to be handled naturally within the same loop.
        approach_02: Single_Pass_LL_Add = Single_Pass_LL_Add(l1=l1, l2=l2)

        # 🏁 Use the single-pass implementation as the selected solution.
        return approach_02.add()