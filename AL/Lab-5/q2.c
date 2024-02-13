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

int commonAncestor(NODE *root, int a, int b){
    if(root){
        int p = commonAncestor(root->lchild, a, b), q = commonAncestor(root->rchild, a, b);
        if(p + q == 3){
            printf("\n\nCommon Ancestor: %d\n", root->data);
            return 0;
        }
        if(p + q > 0){
            return p+q;
        }
        if(root->data == a){
            return 1;
        }
        else if(root->data == b){
            return 2;
        }
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
    commonAncestor(root, 1, 2);
}