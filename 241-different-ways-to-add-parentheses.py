from itertools import permutations

class Node:
    def __init__(self, val, left):
        self.val = val
        self.left, self.right = left, None
        if not(left is None): left.right = self
    def calc(self):
        if self.val=='*': return self.left.calc()* self.right.calc()
        if self.val=='+': return self.left.calc()+ self.right.calc()
        if self.val=='-': return self.left.calc()- self.right.calc()
        return self.val

    def reduce(self):
        self.val = self.calc()
        ll = self.left.left
        if ll: ll.right = self; self.left = ll
        rr = self.right.right
        if rr: rr.left = self; self.right = rr


def get_all_combinations(expression):
    def build_ll(expression):
        operators = []
        numstr = ''
        cur_node = None
        for el in expression:
            if el in '0123456789':
                numstr += el
                continue
            if len(numstr)!=0:
                cur_node = Node(int(numstr), cur_node)
                numstr = ""
            cur_node = Node(el, cur_node)
            operators.append(cur_node)
        cur_node = Node(int(numstr), cur_node)
        return operators

    operators = build_ll(expression)
    results = set()
    for order in permutations(range(len(operators))):
        operators = build_ll(expression)
        for n in order:
            operators[n].reduce()
        results.add(operators[order[-1]].calc())
    return sorted(list(results))


print get_all_combinations("2*3-4*5")
