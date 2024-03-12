# include<stdio.h>
# include<stdlib.h>
# include<string.h>

int opcount = 0;

typedef struct list_{
    struct list_ *next;
    char *data;
} NODE;

int value_of_word(char str[]){
    int val = 0, i = 0;
    char ch;
    while(str[i] != '\0'){
        ch = str[i];
        if (ch >= 'a' && ch <= 'z'){
            val += ch - 'a';
            printf("%d ", ch - 'a');
        }
        else{
            val += ch - 'A';
            printf("%d ", ch = 'A');
        }
        i++;
    }
    printf("%d\t", val);
    return val;
}

NODE *createNode(char ele[]){
    NODE *temp = (NODE*) malloc(sizeof(NODE));
    printf("Length of %s -> %ld", ele, strlen(ele));
    temp->data = (char*) calloc(strlen(ele) + 1, sizeof(char));
    strcpy(temp->data, ele);
    temp->next = NULL;
    return temp;
}

int search(NODE **hash_table, int n, char ele[]){
    NODE *temp = hash_table[value_of_word(ele) % n];
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
    int n, m, k;
    char ele[50];
    NODE *temp;
    printf("Enter the size of hash table and number of entries: ");
    scanf(" %d %d", &n, &m);
    NODE **hash_table = (NODE**) calloc(n, sizeof(NODE*));
    for(int i=0; i<n; i++)
        hash_table[i] = NULL;
    printf("Enter the %d entries:\n", m);
    for(int i=0; i<m; i++){
        printf("\nEnter word: ");
        scanf(" %s", ele);
        printf("hello->%s\t", ele);
        k = (value_of_word(ele)) % n;
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
    printf("Enter word to search: ");
    fgets(ele, 50, stdin); 
    int x = search(hash_table, n, ele);
    if(x){
        printf("\n Word was found!!!\n");
    }
    else{
        printf("\nWord was NOT found!!!\n");
    }
    printf("Opcount = %d\n", opcount);
}