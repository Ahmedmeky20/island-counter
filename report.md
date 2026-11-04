ISLAND COUNTER — PROJECT REPORT

1. PROBLEM STATEMENT
The goal is to count separate islands in a grid containing land (1) and water (0). Land cells are connected when they share an edge: up, down, left, or right. Diagonal neighbors are not considered connected.

2. GRAPH MODEL
Treat every grid cell as a vertex. A land cell can connect to land neighbors in the four allowed directions. An island is a connected component of land vertices. Water cells are ignored during traversal.

3. ALGORITHM
The solution uses iterative Depth-First Search (DFS).
1. Create a visited matrix with the same dimensions as the grid.
2. Scan each cell row by row.
3. When an unvisited land cell is found, increment the island count.
4. Start a DFS stack from that cell and mark it visited.
5. Pop a cell and inspect its four neighbors. Add each in-bounds, unvisited land neighbor to the stack and mark it visited.
6. Continue until every cell has been checked. Return the count.

Cells are marked visited when added to the stack to prevent duplicate processing. An explicit stack avoids Python recursion-depth problems on large grids.

4. COMPLEXITY ANALYSIS
Let R be the number of rows and C the number of columns.
Time: O(R × C), because every cell is checked and each land cell is visited at most once.
Auxiliary space: O(R × C) for the visited matrix; the DFS stack can also use O(R × C) space in the worst case.

5. EXPERIMENTS AND TESTS
Run tests with: python -m unittest -v
The tests cover the lecture example, an empty grid, all-water and all-land grids, diagonal-only contact, single-cell grids, a non-rectangular grid, and invalid cell values.
Expected counts for several patterns:
- Lecture example (4 × 5): 3 islands
- All-water 10 × 10: 0 islands
- All-land 10 × 10: 1 island
- Main diagonal land cells in a 10 × 10 grid: 10 islands
Measure actual running times on the computer used for the final demonstration.

6. CONCLUSION
DFS is a direct way to identify connected components in the grid. The implementation avoids external dependencies and validates its input. The same connected-component idea can be used in maze and network problems.

7. REFLECTION
What surprised me? Diagonal land cells do not form one island under the four-directional rule; connectivity depends on the graph model.
What would I do next? I would time larger grids and compare DFS with BFS using the same connectivity rule and test cases.
