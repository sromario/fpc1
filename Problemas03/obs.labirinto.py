def min_turns_to_exit(N, M, heights):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def valid(x, y, prev_height):
        return 0 <= x < N and 0 <= y < M and abs(heights[x][y] - prev_height) <= 1
    
    def bfs():
        queue = [(0, 0, 0)]  # (x, y, turns)
        visited = set()
        
        while queue:
            x, y, turns = queue.pop(0)
            
            if x == N - 1 and y == M - 1:
                return turns
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if valid(new_x, new_y, heights[x][y]) and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, turns + 1))
        
        return -1  # Não é possível alcançar a saída
    
    return bfs()

# Leitura de entrada
N, M = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]

# Encontre a menor quantidade de turnos para sair do labirinto
result = min_turns_to_exit(N, M, heights)

# Imprima o resultado
print(result)
