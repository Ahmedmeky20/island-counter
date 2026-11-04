from collections.abc import Sequence
import argparse
from pathlib import Path


Grid = Sequence[Sequence[int]]


def count_islands(grid: Grid) -> int:
    """Return the number of 4-directionally connected land components.

    Args:
        grid: A rectangular grid containing only 0s and 1s.

    Raises:
        ValueError: If rows have different lengths or a cell is not 0 or 1.
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    for row in grid:
        if len(row) != cols:
            raise ValueError("Grid must be rectangular.")
        if any(cell not in (0, 1) for cell in row):
            raise ValueError("Grid cells must be 0 or 1.")

    visited = [[False] * cols for _ in range(rows)]
    islands = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                islands += 1
                stack = [(r, c)]
                visited[r][c] = True

                while stack:
                    current_r, current_c = stack.pop()

                    for dr, dc in directions:
                        nr = current_r + dr
                        nc = current_c + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                            and not visited[nr][nc]
                        ):
                            visited[nr][nc] = True
                            stack.append((nr, nc))

    return islands


def read_grid(file_path: str) -> list[list[int]]:
    """Read a grid from a text file; values may be separated by spaces or commas."""
    grid: list[list[int]] = []
    for line_number, line in enumerate(Path(file_path).read_text(encoding="utf-8").splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        normalized = line.replace(",", " ")
        try:
            row = [int(value) for value in normalized.split()]
        except ValueError as exc:
            raise ValueError(f"Invalid integer on line {line_number}.") from exc
        grid.append(row)
    return grid


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count islands in a grid of 0s (water) and 1s (land)."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="sample_grid.txt",
        help="Path to a text file containing the grid (default: sample_grid.txt)",
    )
    args = parser.parse_args()

    try:
        grid = read_grid(args.file)
        print(f"Number of islands: {count_islands(grid)}")
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
