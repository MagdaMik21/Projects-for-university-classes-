def build_adjacency_graph(image):
    """
    Tworzy graf sąsiedztwa dla czarnych pikseli w obrazie rastrowym.

    :param image: Lista list reprezentująca obraz (0 = biały piksel, 1 = czarny piksel)
    :return: Słownik reprezentujący graf sąsiedztwa czarnych pikseli
    """
    n = len(image)
    graph = {}

    # Ruchy: góra, dół, lewo, prawo (można rozszerzyć o ruchy diagonalne)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(n):
            if image[i][j] == 1:  # Czarny piksel
                neighbors = []
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and image[ni][nj] == 1:
                        neighbors.append((ni, nj))
                graph[(i, j)] = neighbors

    return graph

def count_disjoint_black_regions(image):
    """
    Liczy liczbę rozłącznych czarnych plam na obrazie i zwraca ich współrzędne.

    :param image: Lista list reprezentująca obraz (0 = biały piksel, 1 = czarny piksel)
    :return: Liczba rozłącznych czarnych plam oraz lista współrzędnych pikseli dla każdej plamy
    """
    n = len(image)
    visited = [[False for _ in range(n)] for _ in range(n)]

    def dfs(x, y):
        """Przeprowadza przeszukiwanie w głąb, aby znaleźć wszystkie piksele w danej plamie."""
        stack = [(x, y)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        region = [(x, y)]  # Lista współrzędnych tej plamy
        visited[x][y] = True  # Oznaczamy początkowy piksel jako odwiedzony

        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                # Sprawdzamy czy sąsiedni piksel jest czarny i jeszcze nie odwiedzony
                if 0 <= nx < n and 0 <= ny < n and image[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    region.append((nx, ny))  # Dodanie do regionu

        return region

    regions = []
    for i in range(n):
        for j in range(n):
            if image[i][j] == 1 and not visited[i][j]:
                region = dfs(i, j)
                regions.append(region)

    return len(regions), regions

# Przykład użycia
image = [
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 1]
]

number_of_regions, regions = count_disjoint_black_regions(image)
print(f"Liczba rozłącznych czarnych plam: {number_of_regions}")
for idx, region in enumerate(regions, 1):
    print(f"Plama {idx}: {region}")

