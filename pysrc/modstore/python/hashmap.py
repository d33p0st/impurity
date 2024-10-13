
class HashMap(dict):
    def __init__(self, createfrom: dict) -> None:
        for k, v in createfrom.items():
            self[k] = v
    
    @property
    def invert(self) -> 'HashMap':
        inverted = {}
        for k, v in self.items():
            if v in inverted:
                if isinstance(inverted[v], list):
                    inverted[v].append(k)
                else:
                    inverted[v] = [inverted[v], k]
            else:
                inverted[v] = k
        return inverted
    
    