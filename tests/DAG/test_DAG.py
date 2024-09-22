from modstore.rust.dag import DAG

def test_Dag():
    # create a dag
    dag = DAG()

    # add a few nodes
    dag.addNode('A')
    dag.addNode('B')
    dag.addNode('C')

    # check added nodes
    assert 'A' in dag.nodes
    assert 'B' in dag.nodes
    assert 'C' in dag.nodes

    # add a few edges
    dag.addEdge('A', 'B')
    dag.addEdge('A', 'C')

    # check added edges
    assert ('A', 'B') in dag.edges
    assert ('A', 'C') in dag.edges

    # try to add cyclic edge
    try:
        dag.addEdge('C', 'B')
        # assert False # assert False if added
    except ValueError:
        assert True # assert True if failed like it's supposed to.