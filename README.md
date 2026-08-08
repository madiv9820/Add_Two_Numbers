# [🧮 The Linked List Calculator — Add Two Numbers! 🔗➕](https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150)

### 📖 Short Story

Two numbers arrive at your doorstep, but there’s a catch! 😈 Instead of being written normally, their digits are packed inside linked lists, backwards one node at a time. Your job is to play the role of the calculator 🧮, add these mysterious numbers together, and return their ***final sum as another linked list***. Can you bring the digits together and uncover the answer? 🔢✨

### 📝 Problem Explanation

You are given two **non-empty linked lists**, where each node stores a single digit of a non-negative integer. The digits are stored in **reverse order**, meaning the first node represents the units digit, followed by the tens, hundreds, and so on.

*Add the two numbers represented by these linked lists and return their sum in the same reversed linked-list format. ➕🔗*

- #### 🌟 Example 1 — The First Mission

    ```
    l1      = [2,4,3]
    l2      = [5,6,4]
    Output  = [8,0,7]
    ```
    
    **Explanation:** **`342 + 465 = 807`**

- #### 🟢 Example 2 — The Zero Case
    ```
    l1      = [0]
    l2      = [0]
    Output  = [0]
    ```
    
    **Explanation:** **`0 + 0 = 0`**

- #### 🔥 Example 3 — The Carry Chain
    ```
    l1      = [9,9,9,9,9,9,9]
    l2      = [9,9,9,9]
    Output  = [8,9,9,9,0,0,0,1]
    ```
    **Explanation:** Here, the many 9s create a chain reaction of carries, making the final number longer than either input. 💥➕9️⃣

#### 📌 Constraints
- Each list contains **1–100 nodes**.
- Each node contains a digit from **0–9**.
- The numbers contain no leading zeros, except for the number **`0`**.
- Both numbers are non-negative.
---

### 🧠 Approaches

The key challenge is to simulate **normal column-wise addition** while working with linked lists whose digits are already stored in reverse order. Each approach processes the digits from least significant to most significant while keeping track of a possible **carry**. The first approach separates the work into distinct phases, while the second simplifies everything into a **single unified traversal**. 🔗➕

#### 🔵 Approach 1: Three-Phase Linked List Addition

- **💡 Intuition**

    Process the addition in three stages: first add digits while **both lists have nodes**, then process whichever list has remaining digits, and finally handle any leftover carry. This mirrors manual addition while explicitly separating the different list-length scenarios. 🧮

- **🪜 Steps**

    1. 🔄 Add corresponding digits while both lists contain nodes.
    2. 🎒 Include the carry from the previous digit in every addition.
    3. 📏 If **`l1`** has remaining nodes, process them with the carry.
    4. 📐 If **`l2`** has remaining nodes, process them with the carry.
    5. ➕ If a carry remains after both lists are exhausted, append it.
    6. 🏁 Return the head of the resulting linked list.

- **📝 Pseudocode**
    
    ```
    Initialize result list and carry = 0

    WHILE both lists have nodes:
        sum = l1 digit + l2 digit + carry
        create node with sum % 10
        carry = sum // 10
        move both lists forward

    WHILE l1 has nodes:
        sum = l1 digit + carry
        create result node
        update carry
        move l1 forward

    WHILE l2 has nodes:
        sum = l2 digit + carry
        create result node
        update carry
        move l2 forward

    IF carry exists:
        append carry

    RETURN result
    ```

- **⏱️ Complexity**

    - **Time: `O(max(m, n))`** — every digit is processed once.
    - **Space: `O(max(m, n))`** — the result contains up to **`max(m, n) + 1`** nodes.

#### 🟢 Approach 2: Single-Pass Linked List Addition

- **💡 Intuition**

    Instead of separating the different-length cases into multiple loops, process **both lists together in one loop**. Whenever one list runs out of digits, simply treat its missing digit as **`0`**. The carry is also included in the loop condition, allowing everything to be handled uniformly. 🚀

- **🪜 Steps**

    1. 🔄 Continue while either list has nodes **or a carry remains**.
    2. 🔢 Read the current digit from each list; use **`0`** if a list is exhausted.
    3. ➕ Add both digits and the current carry.
    4. 🎯 Store **`sum % 10`** as the current result digit.
    5. 🎒 Store **`sum // 10`** as the carry for the next position.
    6. 👉 Move each list forward if it still contains a node.
    7. 🏁 Return the resulting linked list.

- **📝 Pseudocode**

    ```
    Initialize result list and carry = 0

    WHILE l1 exists OR l2 exists OR carry exists:
        digit1 = l1 digit if l1 exists, otherwise 0
        digit2 = l2 digit if l2 exists, otherwise 0

        sum = digit1 + digit2 + carry

        create node with sum % 10
        carry = sum // 10

        move l1 forward if it exists
        move l2 forward if it exists

    RETURN result
    ```

- **⏱️ Complexity**

    - **Time: `O(max(m, n))`** — each input node is visited once.
    - **Space: `O(max(m, n))`** — required for the resulting linked list.

#### 🟣 Approach 3: Recursive Linked List Addition
- **💡 Intuition**

Think of each recursive call as handling **one column of the addition**. At every step, we add the current digits and the carry from the previous step, create the corresponding result node, move both pointers forward, and let the next recursive call handle the remaining digits. 🔄➕

If one list runs out of digits, its value is treated as **`0`**. The recursion continues until **both lists are exhausted and no carry remains**.

- **🪜 Steps**

    1. 🔢 Read the current digit from each list, using **`0`** when a list is exhausted.
    2. ➕ Add both digits along with the current **`carry`**.
    3. 🎯 Store **`sum % 10`** as the current result digit.
    4. 🎒 Store **`sum // 10`** as the carry for the next recursive call.
    5. 👉 Move each available linked-list pointer forward.
    6. 🔄 Recursively process the next pair of digits.
    7. 🛑 Stop when both lists are exhausted and there is no remaining carry.
    8. 🏁 Return the head of the constructed result list.

- **📝 Pseudocode**

    ```
    FUNCTION add():

        IF l1 is empty AND l2 is empty AND carry is 0:
            RETURN

        digit1 = l1 digit if l1 exists, otherwise 0
        digit2 = l2 digit if l2 exists, otherwise 0

        sum = digit1 + digit2 + carry

        create node with sum % 10

        carry = sum // 10

        append node to result

        move l1 forward if it exists
        move l2 forward if it exists

        recursively call add()

        RETURN result
    ```
    
-  **⏱️ Complexity**

    Let **`n = max(m, n)`** be the length of the longer linked list.
    - **Time: `O(n)` ⏱️** — each digit is processed exactly once.
    - **Auxiliary Space: `O(n)` 🧠** — recursive calls consume stack space.
    - **Output Space: `O(n)` 🔗** — the resulting linked list requires up to **`n + 1`** nodes.

### 🏆 Quick Comparison

| Approach           | 💡 Core Idea                                                      | ⏱️ Time | 🧠 Auxiliary Space | 🔗 Output Space |
| ------------------ | ----------------------------------------------------------------- | ------: | -----------------: | --------------: |
| 🔵 **Three-Phase** | Process common digits, then remaining digits separately           |  **`O(n)`** |             **`O(1)`** |          **`O(n)`** |
| 🟢 **Single-Pass** | Process both lists and missing digits uniformly in one loop       |  **`O(n)`** |             **`O(1)`** |          **`O(n)`** |
| 🟣 **Recursive**   | Process one digit per recursive call while carrying state forward |  **`O(n)`** |             **`O(n)`** |          **`O(n)`** |

### 🥇 Final Verdict

**🟢 Single-Pass** remains the best overall choice for your **`Solution`** class.

- **🔵 Three-Phase** — straightforward and explicit, but has duplicated processing logic.
- **🟢 Single-Pass** — clean, iterative, handles unequal lengths naturally, and uses **`O(1)`** auxiliary space -> **🏆 Best practical approach**.
- **🟣 Recursive** — elegant and demonstrates recursion nicely, but uses **O(n)** call-stack space.
---