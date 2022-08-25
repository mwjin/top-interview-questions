class ListNode:
    def __init__(self, key: int = -1, value: int = -1) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.list_head = ListNode()
        self.list_tail = ListNode()
        self.list_head.next = self.list_tail
        self.list_tail.prev = self.list_head

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self._move_key_to_most_recently_used(key)
            return self.key_to_node[key].value
        return -1

    def _move_key_to_most_recently_used(self, key: int):
        node = self.key_to_node[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self._insert_into_last(node)

    def _insert_into_last(self, node: ListNode):
        node.prev, node.next = self.list_tail.prev, self.list_tail
        self.list_tail.prev.next = node
        self.list_tail.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._move_key_to_most_recently_used(key)
            self.key_to_node[key].value = value
        else:
            self._append_new_node(key, value)
            self._evict_lru_if_exceeds()

    def _append_new_node(self, key: int, value: int):
        new_node = ListNode(key, value)
        self._insert_into_last(new_node)
        self.key_to_node[key] = new_node

    def _evict_lru_if_exceeds(self):
        if len(self.key_to_node) > self.capacity:
            lru_node = self.list_head.next
            lru_node.prev.next = lru_node.next
            lru_node.next.prev = lru_node.prev
            del self.key_to_node[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
