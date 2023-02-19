from math import gcd

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __str__(self):
        return f'{self.jug1} {self.jug2}'

def minimumSteps(m, n, d):
    if d > max(m, n) or d % gcd(m, n) != 0:
        return -1

    queue = [State(0, 0)]
    visited = set()
    steps_array = []
    steps = 0

    while queue:
        steps += 1
        size = len(queue)

        for _ in range(size):
            state = queue.pop(0)
            if state.jug1 == d or state.jug2 == d:
                print('\nSteps taken to reach the solution:')
                print('\n'.join(steps_array))
                return steps

            if str(state) in visited:
                continue

            visited.add(str(state))
            steps_array.append(f' Fill jug 1 ({m} units) -> {m} {state.jug2}')
            queue.append(State(m, state.jug2))

            steps_array.append(f' Fill jug 2 ({n} units) -> {state.jug1} {n}')
            queue.append(State(state.jug1, n))

            steps_array.append(f'\n Empty jug 1 -> 0 {state.jug2}')
            queue.append(State(0, state.jug2))

            steps_array.append(f' Empty jug 2 -> {state.jug1} 0')
            queue.append(State(state.jug1, 0))

            steps_array.append(
                f'\n Pour jug 2 into jug 1 -> {state.jug1 - min(state.jug1, n - state.jug2)} {state.jug2 + min(state.jug1, n - state.jug2)}')
            queue.append(State(state.jug1 - min(state.jug1, n - state.jug2), state.jug2 + min(state.jug1, n - state.jug2)))

            steps_array.append(
                f' Pour jug 1 into jug 2 -> {state.jug1 + min(state.jug2, m - state.jug1)} {state.jug2 - min(state.jug2, m - state.jug1)}')
            queue.append(State(state.jug1 + min(state.jug2, m - state.jug1), state.jug2 - min(state.jug2, m - state.jug1)))

    return -1

m = int(input('Enter the value for Jug 1 (m): '))
n = int(input('Enter the value for Jug 2 (n): '))
d = int(input('Enter the value for D: '))

print(f'Minimum number of steps required to reach {d} units: {minimumSteps(m, n, d)}')
