from Structures.Node import Node
def breadthFirstSearch(node, array):
    Q = [node]
    while (len(Q) > 0):
        next = Q.pop(0)
        Q = Q + next.children
        array.append(next.name)
    return array

def main():
    tree = Node("A")
    tree.addChild("B").addChild("C").addChild("D")
    tree.children[0].addChild("E").addChild("F")
    tree.children[2].addChild("G").addChild("H")
    tree.children[0].children[1].addChild("I").addChild("J")
    tree.children[2].children[0].addChild("K")
    print(breadthFirstSearch(tree, []))


if __name__ == '__main__':
    main()