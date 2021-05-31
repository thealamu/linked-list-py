from linkedlist import LinkedList, Node


def test_all():
    l = LinkedList()
    # insert 3 items
    n1 = Node(0, None)
    n2 = Node(1, n1)
    n3 = Node(2, n2)

    l.push_front(n1)
    l.push_front(n2)
    l.push_front(n3)

    gotSize = l.size()
    assert gotSize == 3, f"expected size ${3}, got ${gotSize}"
