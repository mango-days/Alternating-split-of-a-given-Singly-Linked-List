# Alternating split of a given Singly Linked List

# Write a function AlternatingSplit() that takes one list and divides up its nodes to make two smaller lists ‘a’ and ‘b’. The sublists should be made from alternating elements in the original list. So if the original list is 0->1->0->1->0->1 then one sublist should be 0->0->0 and the other should be 1->1->1. 

class Node:
    def __init__ ( self, data, next = None ) :
        self.data = data
        self.next = None
 
class LinkedList :
    def __init__ ( self ) : self.head = None

    def AlternatingSplit ( self , a , b ) :
        first = self.head
        second = first.next
        while ( ( first is not None ) and ( second is not None ) and ( first.next is not None ) ) :
              self.MoveNode(a, first)
              self.MoveNode(b, second)
              first = first.next.next
              if first is None : break
              second = first.next
             
    def MoveNode ( self , dest , node ) :
        new_node = Node ( node.data )
        if dest.head is None : dest.head = new_node
        else :
            new_node.next = dest.head
            dest.head = new_node

    def push ( self , data ) :
        new_node = Node ( data )
        new_node.next = self.head
        self.head = new_node
         
    def printList(self):
        temp = self.head
        while temp:
            print ( temp.data , end = " " )
            temp = temp.next
        print ( "" )
 

llist = LinkedList ()
a = LinkedList ()
b = LinkedList ()

llist.push ( 1 )
llist.push ( 0 )
llist.push ( 1 )
llist.push ( 0 )
llist.push ( 1 )
llist.push ( 0 )
     
llist.AlternatingSplit ( a , b )
llist.printList ()
     
a.printList ()
b.printList ()