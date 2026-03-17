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