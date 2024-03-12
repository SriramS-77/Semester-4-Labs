# include<stdio.h>
# include<stdlib.h>

int opcount = 0;

typedef struct list_{
    struct list_ *next;
    int data;
} NODE;

NODE *createNode(int ele){
    NODE *temp = (NODE*) malloc(sizeof(NODE));
    temp->data = ele;
    temp->next = NULL;
    return temp;
}

int search(NODE **hash_table, int m, int ele){
    NODE *temp = hash_table[ele % m];
    while(temp){
        opcount++;
        if(temp->data == ele)
            return 1;
        temp = temp->next;
    }
    return 0;
}

int main()
{
    int n, m, k, ele;
    NODE *temp;
    printf("Enter the size of hash table and number of entries: ");
    scanf(" %d %d", &n, &m);
    NODE **hash_table = (NODE**) calloc(n, sizeof(NODE*));
    for(int i=0; i<n; i++)
        hash_table[i] = NULL;
    printf("Enter the %d entries: ", m);
    for(int i=0; i<m; i++){
        scanf(" %d", &ele); 
        k = ele % n;
        temp = hash_table[k];
        if(!temp){
            hash_table[k] = createNode(ele);
            continue;
        }
        while(temp->next){
            temp = temp->next;
        }
        temp->next = createNode(ele);
    }
    printf("Enter element to search: ");
    scanf(" %d", &ele);
    int x = search(hash_table, n, ele);
    if(x){
        printf("\nElement was found!!!\n");
    }
    else{
        printf("\nElement was NOT found!!!\n");
    }
    printf("Opcount = %d\n", opcount);
}