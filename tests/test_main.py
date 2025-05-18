from shortest_path.main import create_graph, inputs


def test_create_graph_should_return_proper_graph_as_dictionary():
    graph = create_graph(inputs)
    assert isinstance(graph, dict)
    assert graph['A']['B'] == 5
    assert graph['B']['A'] == 5
    assert len(graph) == 8