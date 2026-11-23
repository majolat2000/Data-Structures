## Week 3 Assignment: Recursion, Dynamic Arrays, Linked Lists & Amortized Analysis

### 1. Code Examples Included
In this folder, I wrote and ran three beginner Python programs to understand how different data structures and functions work:

* **`week3_recursion.py` (Recursion):** A function that calls itself to solve a smaller part of a problem until it reaches a stopping point (the base case). I tested this using a simple countdown and by adding numbers from `1` to `n`.
* **`week3_dynamic_array.py` (Dynamic Arrays):** Unlike fixed arrays where you have to set a size limit first, a dynamic array grows automatically when you add new items. In Python, a normal `list` works as a dynamic array using `.append()` and `.remove()`.
* **`week3_linked_list.py` (Linked Lists):** Instead of storing items side-by-side in one block like an array, a linked list connects separate **Nodes** together like coaches on a train, where each node holds its `data` and a `next` link pointing to the next node.

---

### 2. What is Amortized Analysis and What Does It Do?

**Simple Definition:**
Amortized analysis is a way of calculating the **average time** an operation takes over many runs, rather than judging an algorithm by one single slow moment.

**Everyday Example:**
Imagine buying a **₦2,000 notebook** at the start of the semester and using it for **20 lectures**:
* On **Day 1**, you spend **₦2,000** (expensive).
* On **Days 2 to 20**, you spend **₦0** because you already have the notebook.
* Spreading that ₦2,000 across all 20 classes (`₦2,000 ÷ 20`) means it really only cost **₦100 per lecture** on average.

**What It Does in Data Structures:**
It helps us prove whether a data structure is fast overall in real-world use. For example, in a **Dynamic Array**:
1. Most times when you `.append()` an item, there is already extra empty space waiting, so it happens instantly.
2. Occasionally, the array gets completely full, so the computer has to create a bigger array behind the scenes and copy all the old items over—which takes extra time.
3. **Amortized analysis** averages that one slow copying step across all the fast `.append()` steps before it, showing that adding items to a dynamic array is still very fast on average.
