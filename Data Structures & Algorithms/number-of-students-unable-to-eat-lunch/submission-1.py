from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_q, sandwiches_q, counter = deque(students), deque(sandwiches), 0
        while sandwiches_q:
            max = len(sandwiches_q)
            if students_q[0] == sandwiches_q[0]:
                students_q.popleft()
                sandwiches_q.popleft()
                counter = 0
            else:
                students_q.append(students_q.popleft())
                counter += 1
            if counter > max:
                return max
        return 0

        