# Data Structures and Algorithms (DSA) Notes

A comprehensive guide to fundamental sorting, searching, and linked list algorithms.

---

## 1. Sorting Algorithms

### Bubble Sort
In this algorithm, we sort numbers by treating the first element as the maximum and checking if the next number is less than the current number; if so, we swap them. This continues until all numbers are sorted.
* **Optimization:** Include a check to see if a swap happened. If no swap occurs in a pass, break the loop because the array is already sorted.
* **Logic:**
    ```python
    if num[j] > num[j+1]:
        # do swap
        swapped = True
    ```

### Insertion Sort
We take a number and put it in its right place. We assume the first element is sorted (as it is only one element). We define `key = i` where `i` starts from the 2nd element, and `j = i - 1`.
* **Logic:** While `j >= 0` and `num[j] > key`, we shift elements: `num[j+1] = num[j]`, then `j -= 1`. Finally, `num[j+1] = key`.

### Selection Sort
We find either the minimum or maximum from the numbers.
* **Logic:** Take the minimum of `nums[i]` and store the index. A second loop checks if the current number is less than the minimum; if so, update the minimum and swap them.



### Merge Sort
Works on recursive calls and merging elements. We take `l` as the first index and `r` as the last.
* **Logic:** `mergeSort(nums, l, mid, r)` where `mid = (l + r) // 2`.
* **Merging:** After recursive calls, the left and right parts are sorted. We use two empty lists, `a` and `b`, to store elements. We then use pointers `i, j, k` to merge them back into `nums` by comparing `a[i]` and `b[j]`.

### Quick Sort
Similar to Merge Sort but uses a **partition point**. Elements to the left are lesser and elements to the right are greater than the pivot.
* **Partition Logic:** Use a `key` (often the last element). If `nums[i] <= key`, swap `nums[i]` with `nums[start]` and increment `start`.
* **Recursion:** `p = partition(nums, l, r)`, then call `quickSort(nums, l, p-1)` and `quickSort(nums, p+1, r)`.

### Count Sort
First, count the frequency of each element.
* **Logic:** Find the max number (`mx`). Create `freq = [0] * (mx + 1)`. 
* **Process:** For each `i` in `nums`, `freq[i] += 1`. Then, rebuild the array: `for i in range(0, mx + 1): while freq[i] > 0: nums.append(i)`.
* **Note:** Has the best Time Complexity, but is limited by the range of numbers (e.g., if the range is 1 to 100,000, the frequency array becomes very large).

---

## Sorting Classifications

* **Stable vs. Unstable:** In a **Stable** algorithm, if two numbers are the same (e.g., two 5s), their original relative order is preserved after sorting. In **Unstable**, their order might change.
* **Adaptive vs. Non-Adaptive:** An **Adaptive** algorithm takes less time if the array is already almost sorted. A **Non-Adaptive** algorithm follows the same predefined steps regardless of the initial order.
* **In-place Algorithm:** An algorithm that does not require extra space.

---

## 2. Search Algorithms

### Linear Search
We search through the array from start to end. If `nums[i] == target`, return the index. It is simple but not effective for large datasets.

### Binary Search
Highly effective with $O(\log n)$ time complexity. Requires a sorted array.
* **Logic:** Use `l`, `mid`, and `r`. While `l <= r`:
    * If `nums[mid] == target`, return `mid`.
    * If `target > nums[mid]`, search the right part (`l = mid + 1`).
    * If `target < nums[mid]`, search the left part (`r = mid - 1`).



### Lower Bound & Upper Bound
* **Lower Bound:** The first index where the element is $\ge$ target.
    * *Example:* `[0,1,2,5,12,18,60]`, target=12 $\rightarrow$ LB=4. Target=14 $\rightarrow$ LB=5.
* **Upper Bound:** The first index where the element is $>$ target (does not consider equal).
* **Note:** If the number is not present in the array, the Lower Bound and Upper Bound results are the same.

---

## 3. Linked List

A Linked List is a chain of nodes where each node contains data and a pointer to the next node.

### Structure
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creation
a = Node(2)
b = Node(3)
c = Node(54)
a.next = b
b.next = c



## 🔗 Linked List Operations

A **Linked List** is a chain of nodes where each node contains information such as **data** and a **pointer** to the next node in the chain.

### 1. Node Structure & Creation
To create a Linked List, you first define a `Node` class and then connect the objects.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
a = Node(2)
b = Node(3)
c = Node(54)

# Connecting nodes (Creating the chain)
a.next = b
b.next = c
# head = a
```

### 2. Traversal
Traversing means iterating through every node in the list starting from the **head**.

* **Logic:** Use a temporary variable `curr` to move through the list until you reach `None`.
* **Code:**
    ```python
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next 
    ```

---

### 3. Insertion Operations

| Type | Logic |
| :--- | :--- |
| **At Beginning** | `newNode.next = head`, then update `head = newNode`. |
| **At End** | Traverse until `curr.next == None`, then set `curr.next = newNode`. |
| **At Kth Index** | Traverse to the `k-1` index. Connect `newNode.next = curr.next`, then update `curr.next = newNode`. |



---

### 4. Deletion Operations

* **Delete Head (First Node):** Move the head pointer to the second element.
    * `head = head.next`
* **Delete Last Node:** Traverse until you reach the second-to-last node.
    * `while curr.next.next != None: curr = curr.next`
    * `curr.next = None`
* **Delete Kth Node:** Traverse to the `k-1` index.
    * `curr.next = curr.next.next`



---

### 5. Advanced Types & Techniques

#### Doubly & Circular Lists
* **Doubly Linked List:** Each node is connected to the **Next** node and also the **Previous (PREV)** node.
* **Circular List:** The nodes are connected in a circular manner; for example, the last node `C` connects back to the first or second element instead of `None`.

#### Finding the Middle (Slow & Fast Pointer)
There are two main ways to find the middle of a list:
1.  **Length Method:** Find the total length, then run a loop to `length // 2`.
2.  **Slow/Fast Method:** Think of a track where one runner is twice as fast. When the fast runner reaches the end, the slow runner is exactly at the middle.

**Logic:**
```python
slow = head
fast = head 
while fast != None and fast.next != None:
    slow = slow.next      # moves 1 step
    fast = fast.next.next # moves 2 steps
return slow # This is the middle node
```