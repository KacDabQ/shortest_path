inputs = [
    ['A', 'B', 5],
    ['A', 'C', 3],
    ['B', 'C', 2],
    ['B', 'D', 1],
    ['C', 'D', 3],
    ['D', 'E', 2],
    ['A', 'D', 10],
    ['F', 'G', 1],
    ['F', 'H', 3],
    ['G', 'H', 2],
    ['D', 'H', 1],
]


def create_graph(inputs):
    result = {}
    for source, destination, weight in inputs:
        if result.get(source) is None:
            result[source] = {}
        if result.get(destination) is None:
            result[destination] = {}
        result[source][destination] = weight
        result[destination][source] = weight
    print(result)

def main():
    create_graph(inputs)

if __name__ == "__main__":
    main()