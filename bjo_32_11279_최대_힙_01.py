def heapify_down(A, k, n):
    while 2*k + 1 < n:
        left, right = 2*k + 1, 2*k + 2
        largest = k

        if left < n and A[left] > A[largest]:
            largest = left

        if right < n and A[right] > A[largest]:
            largest = right

        if largest != k:
            A[k], A[largest] = A[largest], A[k]
            k = largest

        else:
            break

def make_heap(A):
    n = len(A)

    for k in range(n//2 - 1, -1, -1):
        heapify_down(A, k, n)

# command_list = [int(sys.stdin.readline()) for _ in range(int(input()))]
# arr = [6, 2, 5, 1, 3, 4]


class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return max_val

    def _heapify_up(self, i):
        parent = self.parent(i)

        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left

        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right

        if i != max_index:
            self.swap(i, max_index)
            self._heapify_down(max_index)

    def build_heap(self, arr):
        self.heap = arr

        for i in range((len(arr) // 2) - 1, -1, -1):
            self._heapify_down(i)

    def get_max(self):
        if not self.heap:
            return None

        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def print_heap(self):
        print(self.heap)


# 사용 예시
heap = MaxHeap()
arr = [4, 10, 3, 5, 1]
heap.build_heap(arr)
print("Initial Max Heap:")
heap.print_heap()

heap.insert(15)
print("After inserting 15:")
heap.print_heap()

max_val = heap.delete_max()
print(f"Deleted max value: {max_val}")
print("After deleting max:")
heap.print_heap()
