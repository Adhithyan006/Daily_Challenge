# Leetcode Qn no: 23
# Qn Name: Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []
 

# Constraints:
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


#My SOLUTION:
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next