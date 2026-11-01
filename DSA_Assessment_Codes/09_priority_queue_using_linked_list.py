# Priority Queue Using Singly Linked List
class Node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        return True if self.front is None else False

    def enqueue(self, new_node):
        if self.isEmpty():
            self.front = new_node
            return
        else:
            if self.front.priority > new_node.priority:
                new_node.next = self.front
                self.front = new_node
                return
            else:
                temp = self.front
                while temp.next:
                    if new_node.priority <= temp.next.priority:
                        break
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
                return

    def dequeue(self):
        if self.isEmpty():
            return
        else:
            self.front = self.front.next
            return

    def printdata(self):
        if self.isEmpty():
            return "Queue is Empty!"
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(Node(4, 1))
    pq.enqueue(Node(5, 2))
    pq.enqueue(Node(6, 3))
    pq.enqueue(Node(7, 0))
    pq.printdata()
    pq.dequeue()
    pq.printdata()
    pq.dequeue()
    pq.printdata()
    pq.dequeue()
    pq.printdata()
    pq.dequeue()
    pq.printdata()
