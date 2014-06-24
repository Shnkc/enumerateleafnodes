fanout = 4
depth = 2

def enumerate_nodes(currentdepth, nodeid,currentbranch, leafnodes):
    if currentdepth==depth:
        leafnodes.append(nodeid)
        return 1
    nodes = 1
    for i in xrange(1,  fanout+1):
        nodes += enumerate_nodes(currentdepth+1, nodeid+nodes, i, leafnodes)
    return nodes


if __name__ == '__main__':
    leafids = []
    #properties for root node
    #root node id   : 1
    #root depth     : 0
    #currentbranch  : 1
    print enumerate_nodes(0,1,1,leafids)
    print leafids
