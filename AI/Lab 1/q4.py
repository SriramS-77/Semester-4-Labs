class BST:
    def __init__(self, val):
        self.lchild = None
        self.rchild = None
        self.data = val

    def preorder(self, root):
        if root != None:
            print(root.data, end = " ")
            self.preorder(root.lchild)
            self.preorder(root.rchild)
    def inorder(self, root):
        if root != None:
            self.inorder(root.lchild)
            print(root.data, end = " ")
            self.inorder(root.rchild)
    def postorder(self, root):
        if root != None:
            self.postorder(root.lchild)
            self.postorder(root.rchild)
            print(root.data, end = " ")

    def addElement(self, root, val):
        if root == None:
            return BST(val)
        if val < root.data:
            root.lchild = self.addElement(root.lchild, val)
        elif val > root.data:
            root.rchild = self.addElement(root.rchild, val)
        else:
            print("No Duplicate Elements Allowed!")
        return root

    
def main():
    bst = BST(25)
    bst.addElement(bst, 15)
    bst.addElement(bst, 50)
    bst.addElement(bst, 10)
    bst.addElement(bst, 22)
    bst.addElement(bst, 4)
    bst.addElement(bst, 12)
    bst.addElement(bst, 24)
    bst.addElement(bst, 18)
    bst.addElement(bst, 35)
    bst.addElement(bst, 70)
    bst.addElement(bst, 31)
    bst.addElement(bst, 44)
    bst.addElement(bst, 66)
    bst.addElement(bst, 90)
    bst.inorder(bst)
    print()
    bst.preorder(bst)
    print()
    bst.postorder(bst)
    print()

if __name__ == "__main__":
    main()


'''
    def InitializeBST(self):
        val = int(input("Enter value: "))
        if val == -1:
            return
        self.data = val
        self.lchild.InitializeBST()
        self.rchild.InitializeBST()
'''