"""
Для реалізації однозв'язного списку (приклад реалізації можна взяти
з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку,
змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад,
сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки
в один відсортований список.
"""


from queue import Queue


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        cur = self.head
        q = Queue()
        q.put(self.head)
        cur = cur.next
        while cur:
            q.put(cur)
            cur = cur.next
        cur = self.head
        next_noda = cur.next
        cur.next = None
        cur = next_noda
        while cur.next:
            next_noda = cur.next
            cur.next = q.get()
            cur = next_noda
        cur.next = q.get()
        self.head = q.get()

    def sort_list(self):
        length = 0
        cur = self.head
        
        while cur:
            length += 1
            cur = cur.next
        
        cur = self.head
        for i in range(1, length):
            # key = lst[i]
            # j = i-1
            k = cur.next
            k_data = k.data
            j = cur
            j_data = j.data
            while j and k_data < j_data:
                link_1 = j
                link_2 = k
                link_3 = k.next
                cur = link_2
                cur.next = link_1
                cur.next.next = link_3
                k = cur.next
                k_data = k.data
                j = cur
                j_data = j.data

# insert_after(self, prev_node: Node, data):

                # j_data = j.data
            # j.next.data = k.data
            cur = cur.next
            i += 1


        
    #     while j >=0 and key < lst[j] :
    #             lst[j+1] = lst[j]
    #             j -= 1
    #     lst[j+1] = key 
    # return lst

    def merge_list(list_1, list_2):
        pass


if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()

    # Вставляємо вузли в початок
    llist1.insert_at_beginning(1)
    llist1.insert_at_beginning(2)
    llist1.insert_at_beginning(3)
    llist1.insert_at_beginning(4)
    llist1.insert_at_beginning(5)

    # Створимо другий список
    llist2.insert_at_beginning(23)
    llist2.insert_at_beginning(25)
    llist2.insert_at_beginning(43)
    llist2.insert_at_beginning(38)
    llist2.insert_at_beginning(0)
    llist2.insert_at_beginning(18)
    llist2.insert_at_beginning(2)

    # Зобимо реверс списку і роздрукуємо результати до та після
    print("Зв'язний список 1:")
    llist1.print_list()
    # llist1.reverse_list()
    # print("Зв'язний список 1 після реверсу:")
    # llist1.print_list()
    # print("Зв'язний список 2:")
    # llist2.print_list()
    # llist2.reverse_list()
    # print("Зв'язний список 2 після реверсу:")
    # llist2.print_list()
    print("Відсортований зв'язний список 1:")
    llist1.sort_list()
    llist1.print_list()
