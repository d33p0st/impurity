from modstore.rust import DAG

def test_basic():
    dag: DAG.BasicDag = DAG('Basic').create

    dag.addNode('A')
    dag.addNode('B')

    assert 'A' in dag.nodes
    assert 'B' in dag.nodes

    assert dag.addEdge('B', 'C', True) == True

    assert 'C' in dag.nodes
    assert ('B', 'C') in dag.edges

    assert dag.addEdge('A', 'B') == True

    assert ('A', 'B') in dag.edges

    assert dag.addEdge('C', 'A') == False # cyclic edge

    try:
        test = dag.addEdge('C', 'D') # not added node, not forced
    except NotImplementedError:
        assert True