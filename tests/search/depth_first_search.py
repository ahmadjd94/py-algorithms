from data_structures import Graph
from search.depth_first_search import dfs


def test_dfs():
    a = Graph(["0", "1", "2", "3", "5", "6"], [
        ("0", "1"), ("1", "2"), ("1", "6"), ("2", "5"), ("2", "3")])

    assert dfs(a, "0", "7", set()) is False
    assert dfs(a, "0", "6", set()) is True
    assert dfs(a, "0", "3", set()) is True
    assert dfs(a, "0", "2", set()) is True
