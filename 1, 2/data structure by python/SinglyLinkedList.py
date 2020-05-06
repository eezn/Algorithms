# Node 클래스 선언
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly linked list 클래스 선언
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    # Add new node at the end of the linked list.
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None: # 마지막 노드까지 순환
                cur = cur.next # head의 포인터 부터 존재하는 마지막 포인터까지 추적
            cur.next = node # 마지막 노드의 포인터에 삽입하는 노드를 삽입

    # return first index of data in the linked list.
    def getdataIndex(self, data):
        curn = self.head
        idx = 0
        while curn: # 마지막 노드까지 순환
            if curn.data == data: # 현재 노드와 찾는 데이터가 일치 하는지 판단
                return idx
            curn = curn.next # 일치하지 않을 시 다음 노드로 옮겨감
            idx += 1 # 인덱스 갱신
        return -1

    # Add new node at the given index.
    def insertNodeAtIndex(self, idx, node):
        """
        A node can be added in three ways
        1) At the front of the linked list.
        2) At a given index.
        3) At the end of the linked list.
        """
        curn = self.head
        prevn = None
        cur_i = 0

        # (1) Add 0 index
        if idx == 0:
            if self.head:
                nextn = self.head # headn(!)를 다음 노드로
                self.head = node # 추가되는 노드를 headn(*)로
                self.head.next = nextn # 새로운 headn(*)에 연결되는 노드에 최초 headn(!, nextn)였던 노드에 연결
            else:
                self.head = node # 빈 linked list 에는 그냥 headn로 추가
        else:
            # (2) Add at given index &
            # (3) At the end of the linked list
            while cur_i < idx: # 주어진 idx 위치 노드까지 순환 ~
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1 
            if cur_i == idx: 
                node.next = curn # 새로운 노드의 next에 curn
                prevn.next = node # 바로앞 노드의 next에 새로운 노드
            else:
                return -1

    # Add new node before the given data.
    def insertNodeAtData(self, data, node):
        index = self.getdataIndex(data)
        if 0 <= index:
            self.insertNodeAtIndex(index, node)
        else:
            return -1

    # Delete data at given index.
    def deleteAtIndex(self, idx):
        curn_i = 0
        curn = self.head # 기준(0번)노드로 설정
        prevn = None # -1번 노드로 설정
        nextn = self.head.next # 1번 노드로 설정
        if idx == 0: # 삭제하고자 하는 노드가 0번 노드일 경우
            self.head = nextn 
        else:
            while curn_i < idx:
                if curn.next: # 기준노드의 다음 노드가 존재할때
                    prevn = curn
                    crun = nextn
                    nextn = nextn.next # 1, 2, 3 -> 2, 3, 4 한 칸씩 뒤로
                else:
                    break
                curn_i += 1
            if curn_i == idx:
                prevn.next = nextn # -1번 노드와 1번 노드를 연결 (가운데 노드 삭제)
            else:
                return -1

    # Empty linked list
    def clear(self):
        self.head = None

    # print
    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)


if __name__=="__main__":
    sl = SinglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(5))
    sl.insertNodeAtIndex(3, Node(4))
    sl.print()
    print(sl.getdataIndex(1))
    print(sl.getdataIndex(2))
    print(sl.getdataIndex(3))
    print(sl.getdataIndex(4))
    print(sl.getdataIndex(5))
    sl.insertNodeAtData(1, Node(0))
    sl.print()