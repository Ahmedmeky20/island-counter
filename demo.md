ISLAND COUNTER 

0:00–0:40 — Problem
1 means land and 0 means water. An island is a group of land cells connected up, down, left, or right. Diagonal contact does not connect islands.

0:40–1:30 — Graph model
Treat each cell as a vertex. The four neighboring cells are possible edges. Each island is a connected component.

1:30–3:00 — Code
Open island_counter.py. Show the row-by-row scan, the visited matrix, the island counter, and the DFS stack. Each new unvisited land cell starts one DFS.

3:00–4:00 — Run the example
Run: python island_counter.py
Expected output: Number of islands: 3

4:00–4:40 — Tests
Run: python -m unittest -v
Mention the tests for diagonal contact, all-water, all-land, and invalid input.

4:40–5:00 — Complexity and reflection
Time complexity: O(R × C). Auxiliary space: O(R × C).
The key detail is that diagonal cells are not connected. A next step would be comparing DFS and BFS.
