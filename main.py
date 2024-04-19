import random
from collections import deque
import sys
from time import time

sys.setrecursionlimit(10000)


class Graph:
    def __init__(self, n):
        self.matrix = [[0] * n for i in range(n)]
        self.vertices = n
        self.edges = []

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.edges.append((u, v))

    def successors(self, vertex):
        return [i for i in range(self.vertices) if self.matrix[vertex][i] == 1]

    def show_matrix(self):
        print('Macierz sąsiedzstwa: ')
        for row in self.matrix:
            print(*row)

    def show_edges(self):
        print('Lista krawedzi: ')
        for u, v in self.edges:
            print(u + 1, '->', v + 1)

    def show_successors(self):
        print('Lista następników: ')
        for i in range(self.vertices):
            print(f'Wierzchołek: {i}: {self.successors(i)}')

    def dfs_matrix(self):  # przeszukiwanie w glab
        visited = [False] * self.vertices
        print('Przeszukiwanie DFS na macierzy sasiedztwa:', end=' ')
        def def_recursion(vertex):
            visited[vertex] = True
            print(vertex, end=' ')

            for neighbor in range(self.vertices):
                if self.matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                    def_recursion(neighbor)

        print('Przeszukiwanie w głąb: ', end='')
        for i in range(self.vertices):  # Rozpocznij DFS od każdego wierzchołka, który jeszcze nie został odwiedzony
            if not visited[i]:
                def_recursion(i)
        print()

    def bfs_matrix(self):  # przeszukiwanie wszerz
        visited = [False] * self.vertices
        print('Przeszukiwanie BFS na macierzy sasiedztwa:', end=' ')
        for start in range(self.vertices):
            if not visited[start]:
                queue = deque([start])
                visited[start] = True
                while queue:
                    vertex = queue.popleft()
                    print(vertex, end=' ')
                    for neighbor in range(self.vertices):
                        if self.matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True
        print()

    def dfs_edges(self):  # Przeszukiwanie w głąb
        visited = [False] * self.vertices
        print('Przeszukiwanie DFS na lisicie krawedzi:', end=' ')
        def dfs_recursion(vertex):
            visited[vertex] = True
            print(vertex, end=' ')

            for u, v in self.edges:
                if u == vertex and not visited[v]:
                    dfs_recursion(v)

        print('Przeszukiwanie w głąb:', end=' ')
        for i in range(self.vertices):
            if not visited[i]:
                dfs_recursion(i)
        print()

    def bfs_edges(self):  # Przeszukiwanie wszerz
        visited = [False] * self.vertices
        print('Przeszukiwanie BFS na lisicie krawedzi:', end=' ')
        for start in range(self.vertices):
            if not visited[start]:
                queue = deque([start])
                visited[start] = True
                while queue:
                    vertex = queue.popleft()
                    print(vertex, end=' ')
                    for u, v in self.edges:
                        if u == vertex and not visited[v]:
                            queue.append(v)
                            visited[v] = True
        print()

    def bfs_successors(self):
        print('Przeszukanie grafu BFS na liscie nastepnikow: ')
        visited = [False] * self.vertices

        for start in range(self.vertices):
            if not visited[start]:
                queue = deque([start])
                visited[start] = True

                while queue:
                    vertex = queue.popleft()
                    print(vertex, end=' ')
                    for neighbour in self.successors(vertex):
                        if not visited[neighbour]:
                            queue.append(neighbour)
                            visited[neighbour] = True
        print()

    def dfs_successors(self):
        print('Przeglądanie grafu DFS na liscie następników: ')
        visited = [False] * self.vertices
        def dfs_recursion(vertex, visited):
            visited[vertex] = True
            print(vertex, end=' ')

            for neighbour in self.successors(vertex):
                if not visited[neighbour]:
                    dfs_recursion(neighbour, visited)

        for start in range(self.vertices):
            if not visited[start]:
                dfs_recursion(start, visited)
        print()


def create_graph():
    n = int(input('Podaj liczbę wierzchołków: '))
    graph = Graph(n)
    print('Podaj macierz sasiedztwa: \n')
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if row[j] == 1:
                graph.add_edge(i, j)
    return graph


def generate_graph(saturation, n):  # generowanie grafu acyklicznego
    list_len = int(n * (n - 1) / 2)
    num_ones = int(list_len * saturation)
    num_zeros = list_len - num_ones
    random_ones = [1] * num_ones + [0] * num_zeros
    random.shuffle(random_ones)

    index = 0
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] = random_ones[index]
            index += 1
    g = Graph(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                g.add_edge(i, j)
    return g


# graph = create_graph()
# graph.show_matrix()
# graph.print_successors()
# graph.dfs()

graph = generate_graph(0.5, 10)

graph.show_matrix()
graph.show_edges()
graph.show_successors()
# PRZESZUKIWANIE BFS
timer = time()
graph.bfs_matrix()
timer = time() - timer
print(f"Czas BFS dla macierzy sasiedztwa {timer}")
print()

timer = time()
graph.bfs_edges()
timer = time() - timer
print(f"Czas BFS dla listy krawedzi {timer}")
print()

timer = time()
graph.bfs_successors()
timer = time() - timer
print(f"Czas BFS dla listy nastepnikow {timer}")
print()

# PRZESZUKIWANIE DFS
timer = time()
graph.dfs_matrix()
timer = time() - timer
print(f"Czas DFS dla macierzy sasiedztwa {timer}")
print()

timer = time()
graph.dfs_edges()
timer = time() - timer
print(f"Czas DFS dla listy krawedzi {timer}")
print()

timer = time()
graph.dfs_successors()
timer = time() - timer
print(f"Czas DFS dla listy nastepnikow {timer}")
print()
