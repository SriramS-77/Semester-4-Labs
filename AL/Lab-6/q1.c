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

int countNodes(NODE *root){
    if (root){
        return 1 + countNodes(root->lchild) + countNodes(root->rchild);
    }
    return 0;
}

void preorder(NODE *root){
    if(root){
        preorder(root->lchild);
        printf("%d\t", root->data);
        preorder(root->rchild);
    }
}

int main(){
    NODE *root = CreateTree();
    preorder(root);
    printf("\nCount of nodes: %d", countNodes(root));
    printf("\nOpcount = %d\n", countNodes(root));
}