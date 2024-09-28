from modstore.rust import DAG

class abc:
    def __init__(self):
        pass

    def do_something(self, a: int, b: int):
        return a+b
        

def test_transactions():
    dag: DAG.TransactionBased = DAG('Transaction-Based').create
    total = []
    total.append(dag.addTransaction("Hehe", [])) # with str

    assert len(total) == 1

    total.append(dag.addTransaction(b"hehe", [])) # with bytes

    assert len(total) == 2

    total.append(dag.addTransaction(abc, [total[0], total[1]])) # with object

    assert len(total) == len(dag.transactions)

    assert dag.transaction(id=total[0]).data(True) == "Hehe" and dag.transaction(id=total[0]).id == total[0]
    assert dag.transaction(id=total[1]).data(True) == b"hehe"
    assert dag.transaction(id=total[2]).data(True) == abc

    obj = abc()
    assert obj.do_something(1, 2) == 3

    assert dag.valid
