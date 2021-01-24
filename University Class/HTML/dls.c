int main(){

    struct node *root = NULL;
    int choose;
    int n=0, i=0, insertNode, limit;

    printf("Enter Your choice : \n 1 For insert a node \n 2 For BFS \n 3 for DFS\n 4 for DLS\n 0 for exit the program");
    printf("\n---------------------------------");



printf("Enter the depth limit for DLS: ");
            scanf("%d", &limit);
            dls(root, 0, limit);








void dls(struct node *root, int i, int limit){
    for(i = 0; i < limit; i++){
        if(root != NULL){
            if(limit > 0){
                dls(root->left, i, limit-1 );
                dls(root->right, i, limit-1 );
                printf("%d ", root->data);
            }

        }
        //printf("\n");
    }
