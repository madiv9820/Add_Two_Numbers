'''
Three_Phase_Linked_List_Addition.py implements linked-list addition using a three-phase strategy, 
processing common digits first, followed by any remaining digits from either operand, 
while propagating carries and constructing the resulting sum as a new linked list. 🔗➕
'''

from typing     import Optional
from ListNode   import ListNode

class Three_Phase_LL_Add:
    """
    🔗 Implements linked-list addition using a three-phase strategy.

    The addition is divided into three phases:
        1️⃣ Process digits while both operands have nodes.
        2️⃣ Process remaining digits of the first operand.
        3️⃣ Process remaining digits of the second operand.

    A final carry, if present, is appended as an additional node.
    """

    def __init__(
        self                    ,
        l1: Optional[ListNode]  ,
        l2: Optional[ListNode]  ,
    ) -> None:

        # 📥 Store references to both input linked lists.
        self.operand1: Optional[ListNode] = l1
        self.operand2: Optional[ListNode] = l2

        # 🎒 Stores the carry generated during digit addition.
        self.carry: int = 0

        # 🏗️ Pointers used to construct the resulting linked list.
        self.sum_head: Optional[ListNode] = None
        self.sum_tail: Optional[ListNode] = None

    def add(self) -> Optional[ListNode]:
        """
        ➕ Adds the two linked-list numbers and returns their sum.

        Returns:
            Optional[ListNode]: Head of the resulting sum linked list.
        """

        # 🚪 If either operand is empty, return the other operand directly.
        if not self.operand1: return self.operand2
        if not self.operand2: return self.operand1

        # 🔄 Reset result state so the object can safely perform
        #    the addition with its current operands.
        self.sum_head   = None
        self.sum_tail   = None
        self.carry      = 0

        # ==========================================================
        # 🔵 PHASE 1: Process digits from both linked lists
        # ==========================================================
        #
        # Both numbers still have digits available, so we add the
        # corresponding digits along with any carry from the previous
        # position.
        while self.operand1 and self.operand2:

            # 🧮 Add the current digits and the carry.
            node_sum: int = (
                    self.operand1.val
                +   self.operand2.val
                +   self.carry
            )

            # 🔢 Store only the current digit in the result node.
            new_node: Optional[ListNode] = ListNode(node_sum % 10)

            # 🎒 Preserve the carry for the next digit.
            self.carry = node_sum // 10

            # 🌱 Initialize the result list with its first node.
            if not self.sum_head:
                self.sum_head = new_node
                self.sum_tail = new_node

            # 🔗 Append subsequent nodes to the result list.
            else:
                self.sum_tail.next  = new_node
                self.sum_tail       = self.sum_tail.next

            # 👉 Move both operands to their next digits.
            self.operand1 = self.operand1.next
            self.operand2 = self.operand2.next

        # ==========================================================
        # 🟢 PHASE 2: Process remaining digits of operand 1
        # ==========================================================
        #
        # If operand 1 is longer, its remaining digits still need to
        # be added along with any carry from Phase 1.
        while self.operand1:

            # 🧮 Add the remaining digit and the carry.
            node_sum = self.operand1.val + self.carry

            # 🎒 Calculate the carry for the next position.
            self.carry = node_sum // 10

            # 🔢 Create a node containing the current result digit.
            new_node = ListNode(node_sum % 10)

            # 🔗 Append the digit to the result list.
            self.sum_tail.next  = new_node
            self.sum_tail       = new_node

            # 👉 Move to the next remaining digit.
            self.operand1 = self.operand1.next

        # ==========================================================
        # 🟡 PHASE 3: Process remaining digits of operand 2
        # ==========================================================
        #
        # If operand 2 is longer, process its remaining digits in
        # exactly the same way as the remaining digits of operand 1.
        while self.operand2:

            # 🧮 Add the remaining digit and the carry.
            node_sum = self.operand2.val + self.carry

            # 🎒 Calculate the carry for the next position.
            self.carry = node_sum // 10

            # 🔢 Create a node containing the current result digit.
            new_node = ListNode(node_sum % 10)

            # 🔗 Append the digit to the result list.
            self.sum_tail.next  = new_node
            self.sum_tail       = new_node

            # 👉 Move to the next remaining digit.
            self.operand2 = self.operand2.next

        # ==========================================================
        # 🔴 FINAL STEP: Handle leftover carry
        # ==========================================================
        #
        # A carry can remain even after both lists have been fully
        # processed.
        #
        # Example:
        #     9 + 1 = 10
        #
        # The 0 is already stored, but the final 1 requires a
        # separate node in the result list.
        if self.carry:

            # 🆕 Create a node for the remaining carry.
            new_node = ListNode(self.carry)

            # 🔗 Append it as the most significant digit.
            self.sum_tail.next  = new_node
            self.sum_tail       = new_node

        # 🏁 Return the beginning of the newly constructed sum list.
        return self.sum_head
