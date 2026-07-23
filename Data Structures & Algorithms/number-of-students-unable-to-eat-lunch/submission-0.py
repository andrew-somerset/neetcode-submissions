from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_q = deque(students)
        sandwiches_q = deque(sandwiches)
        counter = 0
        while sandwiches_q:
            if counter >= len(students_q):
                return len(students_q)
            if sandwiches_q[0] == students_q[0]:
                sandwiches_q.popleft()
                students_q.popleft()
                counter = 0
            else:
                students_q.append(students_q.popleft())
                counter += 1
        return 0