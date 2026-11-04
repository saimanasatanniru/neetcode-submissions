class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build an adjacency list.
        # graph[prereq] contains the courses that depend on prereq.
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # visiting tracks courses on the current DFS path.
        # If we reach one again, we have found a cycle.
        visiting = set()

        # visited tracks courses whose neighbors have all been explored.
        visited = set()

        # Courses are appended after their neighbors are explored.
        # This creates the order in reverse, so we reverse it at the end.
        order = []

        def dfs(course):
            # A course on the current DFS path means there is a cycle.
            if course in visiting:
                return False

            # This course was already fully explored without finding a cycle.
            if course in visited:
                return True

            # Mark this course as part of the current DFS path.
            visiting.add(course)

            # Explore every course that depends on this course.
            for neighbor in graph[course]:
                # If any path contains a cycle, no valid order exists.
                if not dfs(neighbor):
                    return False

            # All neighbors were explored successfully.
            # Remove this course from the active path and mark it complete.
            visiting.remove(course)
            visited.add(course)

            # Add it after its dependent courses have been explored.
            order.append(course)
            return True

        # Start DFS from every course, including disconnected courses.
        for course in range(numCourses):
            # If a cycle is found anywhere, return an empty list.
            if not dfs(course):
                return []

        # Reverse the postorder so prerequisites come before their courses.
        return order[::-1]