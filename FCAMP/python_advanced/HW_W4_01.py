# Min Heap 자료구조를 이용하면 최대값을 O(logN)의 시간복잡도로 찾을 수 있다. Min Heap을 이용하면 우선순위 값이 낮은 자료를 먼저 출력하는 Priority Queue를 구현할 수 있다. 
# Min Heap을 이용한 Priority Queue는 아래와 같은 특징을 가진다.

# Min Heap을 이용한 Priority Queue의 특징
# 자료를 입력하는 동작과 출력하는 동작 모두 O(logN)으로 이루어진다.
# 우선순위 값이 낮은 자료를 먼저 출력하되, 우선순위 값이 같은 자료끼리는 순서를 고려하지 않는다.
# 다음과 같은 Method들을 구현한다.
# is_empty(): Queue가 비어있으면 True, 비어있지 않으면 False를 출력한다.
# put(): Priority Queue에 자료를 입력한다. 자료는 길이가 2인 Tuple로, (우선순위, 자료) 형태로 입력받는다.
# get(): Priority Queue에서 자료를 출력한다. 출력한 데이터는 Priority Queue에서 삭제한다. 더이상 출력할 데이터가 없는 경우 None을 출력한다.
# peek(): Priority Queue에서 자료를 출력한다. 출력한 데이터는 Priority Queue에 그대로 유지한다. 더이상 출력할 데이터가 없는 경우 None을 출력한다.


class PriorityQueue:
    def __init__(self):
        self.heap_array = list()
 
    def is_empty(self):
        if len(self.heap_array) == 0:
            return True
        else:
            return False
 
    def put(self, data):        
        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1

        while True:
            if inserted_idx == 0:
                return False
            
            parent_idx = (inserted_idx - 1) // 2

            if self.heap_array[inserted_idx][0] > self.heap_array[parent_idx][0]:
                self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
                inserted_idx = parent_idx
                return True

            else:
                return False
        
        
    def get(self):
        if len(self.heap_array) == 0:
            return None

        returned_data = self.heap_array[0]

        self.heap_array[0] = self.heap_array[-1]
        del self.heap_array[-1]

        popped_idx = 0

        while True:
            left_child_idx = (popped_idx * 2) + 1
            right_child_idx = (popped_idx * 2) + 2

            if left_child_idx >= len(self.heap_array):
                return returned_data
            
            elif right_child_idx >= len(self.heap_array):
                if self.heap_array[popped_idx][0] < self.heap_array[left_child_idx][0]:
                    self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_idx
                    return returned_data
                else:
                    return returned_data
            
            else:
                if self.heap_array[left_child_idx][0] > self.heap_array[right_child_idx][0]:
                    if self.heap_array[popped_idx][0] < self.heap_array[left_child_idx][0]:
                        self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_idx
                        return returned_data
                    else:
                        return returned_data
                else:
                    if self.heap_array[popped_idx][0] < self.heap_array[right_child_idx][0]:
                        self.heap_array[popped_idx], self.heap_array[right_child_idx] = self.heap_array[right_child_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_idx
                        return returned_data
                    else:
                        return returned_data
        
 
    def peek(self):
        if len(self.heap_array) == 0:
            return None
        else:
            return self.heap_array[0]

    # Test code
 
pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))

print(pq.heap_array)
 
print(pq.get()) #5
print(pq.get()) #4
print(pq.get()) #3
print(pq.get()) #2
print(pq.get()) #1
print(pq.get()) #0
print(pq.get()) #None