import pytest

from nbt.graph import Graph

@pytest.fixture(scope="function")
def graph():
	return Graph()

def test_graph_add_point(graph):
	graph.add_point("A")
	graph.add_point("B")
	assert graph.get_points() == ["A", "B"]
	graph.add_point("q", "w", "e")
	assert set(graph.get_points()) == set(["A", "B", "q", "w", "e"])
	graph.del_point("A", "B")
	assert set(graph.get_points()) == set(["q", "w", "e"])

def test_graph_edge(graph):
	graph.add_edge("a", "b")
	graph.add_edge("b", "c")
	graph.add_edge("b", "d")
	graph.add_edge("a", "e")
	graph.add_edge("e", "f")
	assert set(graph.get_points()) == set(["a", "b", "c", "d", "e", "f"])
	assert graph._find_edge("a", "b")
	assert not graph._find_edge("a", "d")

def test_graph_bfs(graph):
	graph.add_edge("a", "b")
	graph.add_edge("b", "c")
	graph.add_edge("b", "d")
	graph.add_edge("a", "e")
	graph.add_edge("e", "f")
	assert list(graph.bfs("a")) == ["a", "b", "e", "c", "d", "f"]
