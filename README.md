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