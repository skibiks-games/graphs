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

    def topological_sort_dfs_successors(self):
        visited = [False] * self.vertices
        stack = []

        def topological_sort_util(v):
            visited[v] = True
            for i in self.successors(v):
                if not visited[i]:
                    topological_sort_util(i)
            stack.append(v)

        for i in range(self.vertices):
            if not visited[i]:
                topological_sort_util(i)

        print("Sortowanie Topologiczne (DFS lista nastepnikow):")
        while stack:
            print(stack.pop(), end=' ')

    def topological_sort_bfs_successors(self):
        in_degree = [0] * self.vertices
        for i in range(self.vertices):
            for j in self.successors(i):
                in_degree[j] += 1

        queue = deque([i for i in range(self.vertices) if in_degree[i] == 0])
        result = []

        while queue:
            v = queue.popleft()
            result.append(v)
            for i in self.successors(v):
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

        print("Sortowanie Topologiczne (BFS lista nastepnikow):")
        print(' '.join(map(str, result)))

    def topological_sort_dfs_matrix(self):
        visited = [False] * self.vertices
        stack = []

        def topological_sort_util(v):
            visited[v] = True
            for i in range(self.vertices):
                if self.matrix[v][i] == 1 and not visited[i]:
                    topological_sort_util(i)
            stack.append(v)

        for i in range(self.vertices):
            if not visited[i]:
                topological_sort_util(i)

        print("Sortowanie Topologiczne (DFS macierz sasiedztwa):")
        while stack:
            print(stack.pop(), end=' ')
        print()

    def topological_sort_bfs_matrix(self):
        in_degree = [0] * self.vertices
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.matrix[i][j] == 1:
                    in_degree[j] += 1

        queue = deque([i for i in range(self.vertices) if in_degree[i] == 0])
        order = []

        while queue:
            v = queue.popleft()
            order.append(v)
            for i in range(self.vertices):
                if self.matrix[v][i] == 1:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)

        print("Sortowanie Topologiczne (BFS macierz sasiedztwa):")
        print(' '.join(map(str, order)))

    def topological_sort_dfs_edges(self):
        adj_list = {i: [] for i in range(self.vertices)}
        for u, v in self.edges:
            adj_list[u].append(v)

        visited = [False] * self.vertices
        stack = []

        def topological_sort_util(v):
            visited[v] = True
            for i in adj_list[v]:
                if not visited[i]:
                    topological_sort_util(i)
            stack.append(v)

        for i in range(self.vertices):
            if not visited[i]:
                topological_sort_util(i)

        print("Sortowanie Topologiczne (DFS tabela krawedzi):")
        while stack:
            print(stack.pop(), end=' ')
        print()

    def topological_sort_bfs_edges(self):
        adj_list = {i: [] for i in range(self.vertices)}
        in_degree = [0] * self.vertices
        for u, v in self.edges:
            adj_list[u].append(v)
            in_degree[v] += 1

        queue = deque([i for i in range(self.vertices) if in_degree[i] == 0])
        order = []

        while queue:
            v = queue.popleft()
            order.append(v)
            for i in adj_list[v]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

        print("Sortowanie Topologiczne (BFS tabela krawedzi):")
        print(' '.join(map(str, order)))

def create_graph():
    n = int(input('Podaj liczbe wierzcholkow: '))
    graph = Graph(n)
    print('Podaj macierz sasiedztwa: \n')
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if row[j] == 1:
                graph.add_edge(i, j)
    return graph

def generate_graph(saturation):  # generowanie grafu acyklicznego
    n = int(input('Podaj liczbe wierzcholkow: '))
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




option = 1
while option != 0:
    print('Wybierz opcję z Menu:\n'
          '1 Wygeneruj spójny skierowany graf acykliczny\n'
          '2 Utwórz graf na podstawie macierzy sąsiedztwa\n'
          '3 Wyświetl macierz sąsiedztwa, listę następników, tabelę krawędzi\n'
          '4 BFS\n'
          '5 DFS\n'
          '6 Sortowanie topologiczne\n'
          '0 Zakończ program')
    option = int(input())
    if option == 1:
        graph = generate_graph(0.5)
    elif option == 2:
        graph = create_graph()
    elif option == 3:
        graph.show_matrix()
        graph.show_edges()
        graph.show_successors()
    elif option == 4:
        timer = time()
        graph.bfs_matrix()
        timer = time() - timer
        print(f"Czas BFS dla macierzy sąsiedztwa: {timer}")
        print()

        timer = time()
        graph.bfs_edges()
        timer = time() - timer
        print(f"Czas BFS dla listy krawędzi: {timer}")
        print()

        timer = time()
        graph.bfs_successors()
        timer = time() - timer
        print(f"Czas BFS dla listy następników: {timer}")
        print()
    elif option == 5:
        timer = time()
        graph.dfs_matrix()
        timer = time() - timer
        print(f"Czas DFS dla macierzy sąsiedztwa: {timer}")
        print()

        timer = time()
        graph.dfs_edges()
        timer = time() - timer
        print(f"Czas DFS dla listy krawędzi: {timer}")
        print()

        timer = time()
        graph.dfs_successors()
        timer = time() - timer
        print(f"Czas DFS dla listy następników: {timer}")
        print()
    elif option == 6:
        timer = time()
        graph.topological_sort_dfs_matrix()
        timer = time() - timer
        print(f"Czas sortowania topologicznego DFS dla macierzy sąsiedztwa: {timer}")
        print()

        timer = time()
        graph.topological_sort_bfs_matrix()
        timer = time() - timer
        print(f"Czas sortowania topologicznego BFS dla macierzy sąsiedztwa: {timer}")
        print()

        timer = time()
        graph.topological_sort_dfs_edges()
        timer = time() - timer
        print(f"Czas sortowania topologicznego DFS dla listy krawędzi: {timer}")
        print()

        timer = time()
        graph.topological_sort_bfs_edges()
        timer = time() - timer
        print(f"Czas sortowania topologicznego BFS dla listy krawędzi: {timer}")
        print()

        timer = time()
        graph.topological_sort_dfs_successors()
        timer = time() - timer
        print(f"Czas sortowania topologicznego DFS dla listy następników: {timer}")
        print()

        timer = time()
        graph.topological_sort_bfs_successors()
        timer = time() - timer
        print(f"Czas sortowania topologicznego BFS dla listy następników: {timer}")
        print()
    elif option == 0:
        print('Zakończono program')
    else:
        print('Nie rozpoznano opcji')