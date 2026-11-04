class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list with one empty list for each course.
        # graph[i] will contain the courses that can be taken after course i.
        graph = [[] for _ in range(numCourses)]

        # Each pair is [course, prereq]: prereq must be taken before course.
        # So add an edge from prereq to course.
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # visiting: courses currently on the active DFS path.
        # Reaching one again means we found a cycle.
        # visited: courses whose neighbors have all been explored.
        # These are safe to skip if we encounter them again.
        visiting, visited = set(), set()

        def dfs(course):
            # This course is already on the current path:
            # following the edges brought us back to it, so there is a cycle.
            if course in visiting:
                return False

            # This course was fully explored before, with no cycle found.
            if course in visited:
                return True

            # Mark this course as part of the current DFS path.
            visiting.add(course)

            # Explore every course that depends on this course.
            for neighbor in graph[course]:
                # If any path contains a cycle, the whole schedule is impossible.
                if not dfs(neighbor):
                    return False

            # All neighbors were explored without finding a cycle.
            # Remove this course from the active path and mark it fully explored.
            visiting.remove(course)
            visited.add(course)
            return True

        # Check every course, including courses with no prerequisites
        # and courses in separate, disconnected parts of the graph.
        for course in range(numCourses):
            if not dfs(course):
                return False  # A cycle means not all courses can be completed.

        # No cycle was found, so all courses can be completed.
        return True