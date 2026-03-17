--DSA
    1. SORTING ALGORITHMS:
        --- Bubble Sort: In this algorithm we sort number by going firt element as max and check there next number is lessthan first number then swap them, do this until all number are not sorted.
        - Also additional check if swap not happen then break the loop, because number sorted, 
        >> if num[j] > num[j+1]:
                do swap.
                swap = True
        
        --- Insertion Sort: We took the number and put them at there right place. It's mean we assumed first elemnt is sorted because only one elment, we define key=i where i start from 2nd element of array and j=i-1.
        - we roll loop from first element and check array sorted by considering first and second element, while loop J is greater than 0 and num[j]>key then num[j+1] = num[j] j-=1.
        - num[j+1] = key

        --- Selection Sort: Here we go with first take either min or max from numbers, taking min of nums[i] and took idx=i,second loop start from first index and check current number is less than minimum then make minimum mn=num[j] inx=j and swap them. 

        --- Merge Sort: this worked on revursive call and merging element, like first we took l as first element and r as last element of list, in mergeSort we call the recursive function like mergeSort(nums,l,mid,r) mid is //2 of l and r.

        after recursive call l part is l to mid+1 and r part is mid+1 to r is sorted but now another function call here is merge them, for this we used to empty list likewise a and b, now store element l to mid+1 into a and in b mid+1 to r.
        - here also we decalare i,j,k=0,0,l
        for merging we use the if cases like if j==len(b) then took nums[k]=a[i] i+=1 k+=1
        elif i==len(a) then nums[k]=b[j],j+=1,k+=1
        elif a[i] < b[j]: nums[k] = a[i], i+=1,k+=1
        else nums[k]=b[j],j+=1,k+=1 

        this how sort and merge works.

        --- Quick Sort: this work like merge but here we find the partiction point with help of them there left element is lesser and right elem is greater than it. so by using quickSort recursion call with help of partion function which return partiton point.
        - in function we took start point and key which anything but prefered last elem, then nums[i] <= key: swap nums[i] with nums[start] start+=1 and return start - 1 
        - in quickSort recursive call function p=partion(nums,l,r) and 
        - quickSort(nums,l,p-1) and quickSort(nums,p+1,r)

        --- Count Sort: in this sorting we first count the frequency of each element and also first take max number of arr and freq=[0]*(mx+1) define the array with by default 0 and run the loop for the count the freq. of each number 
        -for i in nums: freq[i]+=1
        -nums = []
        now sort the array  
        -for i in range(0,mx+1): while frq[i]>0: nums.append(i) freq+=1 return nums qith sorted
        -- this has best TM but here number limit because if [1,100000] then freq array created with len of 100001


        ---- Stable and Unstabe algorithm: 
        -- like [5,1,2,4,3,5,6] = here if same number so during the sorting first 5 come first and then second [1,2,3,4,5,5,6] and if second come first and first after then that wes unsatble algorithm.

        --- Adaptive and non-adaptive algorithm: If array is almost sorted only one elem is not in right place then took less time is called adptive algo and if whatever case it goes pre defined steps is non-adaptive algo.

        --- Inplace Algo: Which algo not take extra spaces.



** Search Algorithms:
    --- Linear Search: We search the algorithm from starting to end or target point, if nums[i]==target then return the index or number found, this how linear search algorithms work but if number of elem. is more then this algorithm is not effective as we need.

    --- Binary Search:
        -  This is effective and less TM nlogn, we took l, mid, and right point. what we do is run the loop until l<=r and check condition like if mid is equal to target then return mid, elif target>nums[mid] then l=mid+1 so we consider only right part at this point and if target<nums[mid] then we consider only the left part and r=mid-1 and outof loop return -1 if no found of number in list.

    --- Lower bound: It's give the first index elem that is >= to target, 
        - e.g. [0,1,2,5,12,18,60] target=12 then here LB = 4, if target 14 then LB = 5
        Find the LB, if nums[mid] >= target: ans=mid, r=mid-1 and here default val;ue of 
        ans=len(nums), else l=mid+1

    --- Upper Bound: It's give the first index of elem that > target, here not consider the =.

    ** If Number is not present in arry then lower bound and upper bound are same for both cases **





    ----- Linked List -----:
        -- Linked list is basically chain of node where each node contain informarion such as data and pointer to the next node in each chain.

        -- Now for creating Linked list you have to define the Node class then after create the node objects which you want to consider as List, and connect them.
        class Node:
            def __init__(self,data):
                slef.data = data
                self.next = None

        a = Node(2)
        b = Node(3)
        c = Node(54)

        a.next=b
        b.next=c
        this how linked list created.

        --Linked list Traverse (Traverse means how to iterate throgh node )
            - for doing this we defined head in code, head is starting number of linked list, head=a, 
            - For traverse the list we took the variable curr = head and
                -- while curr!=None:
                    print(curr.data)
                    curr = curr.next 
        
            -- Insertion of Node at beginning: newNode = Node(10), newNode.next = head,head=newNode
            -- Insertion of Node at end: newNode = node(20), while curr.next!=None: 
            curr = curr.next  by doing this your curr at last elem of list
            curr.next  = newNode
            --- Insertion of Node at kth index: 
            - Doing this you have to come k-1 index by using for i in range(k-1): 
            curr=curr.next and then newNode.next = curr.next first connect newnode with next element and then curr.next = newNode.

            -- Deletion of First node or Head: head = head.next, by doing this your head start from second elem and also first node deleted form Linked List.
            -- Deletion of last node: Come at the second last of node, while curr.next.next != None: curr = curr.next and out of loop curr.next = None.
            -- Deletion kth Node: come at the k-1 index and out of loop do curr.next = curr.next.next.


            ---Doubly Linked List: In this list node connected with there next node and also with PREV. node.
            --- Circular List: In this list node connected with circular manner suppose C is last node then it can be connected with first or second elment.


            --- Finding the Middle of Linked List -- There are two ways to find the middle of Linked list: by finding the length of list and then run the loop l//2 you got the middle of list.
            - By using the slow and fast pointer, Suppose one track where fast running is 10km/h and slow 5km/h, so if fast reached the end then slow at middle of track, just like in list: 
                - slow=head, fast=head 
                    while fast.next!=None and fast!=None:
                        slow = slow.next 
                        fast = fast.next.next
                    return slow