from typing import Optional
from __future__ import annotations


class ListNode:
    def __init__(
        self,
        val: int = -1,
        prev: Optional[ListNode] = None,
        next: Optional[ListNode] = None,
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_keys = 0
        self.key_list_head = ListNode()
        self.key_list_tail = ListNode(prev=self.key_list_head)
        self.key_list_head.next = self.key_list_tail
        self.key_to_node = {}
        self.key_to_value = {}

    def get(self, key: int) -> int:
        if key in self.key_to_value:
            self._move_key_to_most_recently_used(key)
            return self.key_to_value[key]
        return -1

    def _move_key_to_most_recently_used(self, key: int):
        node = self.key_to_node[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self._insert_into_last(node)

    def _insert_into_last(self, node: ListNode):
        node.prev, node.next = self.key_list_tail.prev, self.key_list_tail
        self.key_list_tail.prev.next = node
        self.key_list_tail.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_value:
            self._move_key_to_most_recently_used(key)
        else:
            self._append_new_key(key)
            self._evict_least_recently_used_if_exceeds()

        self.key_to_value[key] = value

    def _append_new_key(self, key: int):
        key_node = ListNode(key)
        self._insert_into_last(key_node)
        self.key_to_node[key] = key_node
        self.num_keys += 1

    def _evict_least_recently_used_if_exceeds(self):
        if self.num_keys > self.capacity:
            lru_key = self.key_list_head.next.val
            lru_node = self.key_to_node[lru_key]
            lru_node.prev.next = lru_node.next
            lru_node.next.prev = lru_node.prev
            del self.key_to_node[lru_key]
            del self.key_to_value[lru_key]
            self.num_keys -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
