#include <stdio.h>
#include <stdlib.h>

typedef struct tr{
    int data;
    struct tr *lchild, *rchild;
} NODE;

NODE *getNode(int data){
    NODE *root = (NODE*) malloc(sizeof(NODE));
    root->lchild = root->rchild = NULL;
    root->data = data;
    return root;
}

NODE *CreateTree(){
    printf("Enter data in node: ");
    int n;
    scanf(" %d", &n);
    if(n==-1) return NULL;
    NODE *root = getNode(n);
    root->lchild = CreateTree();
    root->rchild = CreateTree();
    return root;
}

void inorder(NODE *root){
    if(root){
        inorder(root->lchild);
        printf("%d\t", root->data);
        inorder(root->rchild);
    }
}

void s_inorder(NODE *root, int key, int *suc){
    static int x = 0;
    if(root){
        s_inorder(root->lchild, key, suc);
        if(x){
            *suc = root->data;
            x = 0;
        }
        printf("%d\t", root->data);
        if(root->data == key){
            x = 1;
        }
        s_inorder(root->rchild, key, suc);
    }
}

void p_inorder(NODE *root, int key, int *pre){
    static int x = -1;
    if(root){
        p_inorder(root->lchild, key, pre);
        printf("%d\t", root->data);
        if(root->data == key){
            *pre = x;
        }
        x = root->data;
        p_inorder(root->rchild, key, pre);
    }
}

int max(int a, int b){
    if (a > b)
        return a;
    return b;
}

int depth(NODE *root){
    if(root){
        return 1 + max(depth(root->lchild), depth(root->rchild));
    }
    return 0;
}

NODE* insertBST(NODE *root, int key){
    if(!root){
        printf("Inserted %d\n", key);
        return getNode(key);
    }
    else if(root->data < key){
        root->rchild = insertBST(root->rchild, key);
    }
    else if(root->data > key){
        root->lchild = insertBST(root->lchild, key);
    }
    else{
        printf("\nDuplicates Not Allowed!!!\n");
        return root;
    }

    int bal = depth(root->lchild) - depth(root->rchild);
    printf("Bal is %d\n", bal);
    NODE *temp;
    if(bal < -1){
        if(key > root->rchild->data){
            temp = root->rchild;
            temp->lchild = root;
            root->rchild = NULL;
            root = temp;
        }
        else{
            temp = root->rchild;
            root->rchild = temp->lchild;
            temp->lchild = NULL;
            root->rchild->rchild = temp;
            temp = root->rchild;
            temp->lchild = root;
            root->rchild = NULL;
            root = temp;
        }
    }
    else if(bal > 1){
        if(key < root->lchild->data){
            temp = root->lchild;
            temp->rchild = root;
            root->lchild = NULL;
            root = temp;
        }
        else{
            temp = root->lchild;
            root->lchild = temp->rchild;
            temp->rchild = NULL;
            root->lchild->lchild = temp;
            temp = root->lchild;
            temp->rchild = root;
            root->lchild = NULL;
            root = temp;
        }
    }
    return root;
}

int *getPredecessor(NODE *root, int key){
    if(root){
        int *n;
        if(root->data < key){
            n = getPredecessor(root->rchild, key);
        }
        else if(root->data > key){
            n = getPredecessor(root->lchild, key);
        }
        else{
            NODE *temp;
            if(root->lchild){
                temp = root->lchild;
                while(temp->rchild)
                    temp = temp->rchild;
                return &(temp->data);
            }
            else{
                return NULL;
            }
        }
        if (n){
            return n;
        }
        else{
            return &(root->data);
        }
    }
    else{
        printf("\nError! Key not found!\n");
        return NULL;
    }
}

int *getSuccessor(NODE *root, int key){
    if(root){
        int *n;
        if(root->data < key){
            n = getSuccessor(root->rchild, key);
        }
        else if(root->data > key){
            n = getSuccessor(root->lchild, key);
        }
        else{
            NODE *temp;
            if(root->rchild){
                temp = root->rchild;
                while(temp->lchild)
                    temp = temp->lchild;
                return &(temp->data);
            }
            else{
                return NULL;
            }
        }
        if (n){
            return n;
        }
        else{
            return &(root->data);
        }
    }
    else{
        printf("\nError! Key not found!\n");
        return NULL;
    }
}

int main(){
    NODE *root = NULL;
    int n;
    while(1){
        printf("Enter node: ");
        scanf(" %d", &n);
        if (n == -1)
            break;
        root = insertBST(root, n);
    }
    inorder(root);
    printf("\nEnter the key to find successor and predecessor of: ");
    scanf(" %d", &n);
    int pre, suc;
    p_inorder(root, n, &pre);
    s_inorder(root, n, &suc);
    printf("\nPredecessor = %d", pre);
    printf("\nSuccessor = %d\n", suc);
}