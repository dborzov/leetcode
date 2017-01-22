# example = [(7,0),(9,0),(20,2),(2,3)]

inner=[(9,1),(2,4),(7,0),(20,0),(10,0)]

def find_order(els):
    els = sorted(els,key=lambda x: (x[0],-x[1]))
    ordered = []
    while len(els)>0:
        cur, rank  = els.pop()
        print 'placing: ', (cur,rank)
        ordered.insert(rank, (cur,rank))
    return ordered

print find_order(inner)
