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
    printf("\nRoot: %d\n", root->data);
}