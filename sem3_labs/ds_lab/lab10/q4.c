#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct node{
    int coeff;
    int power;
    struct node * next;
};

struct node * initialise(int c,int p){
    struct node * newnode=(struct node * )malloc(sizeof(struct node));
    newnode->coeff=c;
    newnode->power=p;
    newnode->next=NULL;
    return newnode;
}

void create(struct node * head,int power){
    struct node * temp=head;
    for(int i=0;i<power;i++){
        int m;
        printf("\nEnter coeffecient of %d: ",i);
        scanf("%d",&m);
        struct node * newnode=initialise(m,i);
        temp->next=newnode;
        temp=temp->next;
    }
}

void display(struct node * head){
    struct node * temp=head->next;
    printf("\n Display: ");
    while(temp!=NULL){
        printf("%dx^%d + ",temp->coeff,temp->power);
        temp=temp->next;
    }
}

struct node * add(struct node * head1,struct node * head2){
    struct node * head=(struct node *)malloc(sizeof(struct node));
    struct node * temp=head;
    struct node * temp1=head1->next;
    struct node * temp2=head2->next;
    int i=0;
    while(temp1!=NULL && temp2!=NULL){
        if(temp1->power>temp2->power){
           struct node * newnode=initialise(temp2->coeff,temp2->power);
           temp->next=newnode;
           temp=temp->next;
           temp2=temp2->next;
        }
        else if(temp1->power<temp2->power){
            struct node * newnode=initialise(temp1->coeff,temp1->power);
            temp->next=newnode;
            temp=temp->next;
            temp1=temp1->next;
        }
        else{
            struct node * newnode=initialise(temp1->coeff+temp2->coeff,temp1->power);
            temp->next=newnode;
            temp=temp->next;
            temp1=temp1->next;
            temp2=temp2->next;
        }
    }
    while(temp1!=NULL){
        struct node * newnode=initialise(temp1->coeff,temp1->power);
        temp->next=newnode;
        temp=temp->next;
        temp1=temp1->next;
    }

    while(temp2!=NULL){
        struct node * newnode=initialise(temp2->coeff,temp2->power);
        temp->next=newnode;
        temp=temp->next;
        temp2=temp2->next;
    }
   
    
    return head;
}

int main(){
    struct node * head=(struct node *)malloc(sizeof(struct node));
    struct node * head2=(struct node *)malloc(sizeof(struct node));
    struct node * sum=(struct node *)malloc(sizeof(struct node));
    create(head,5);
    display(head);
    create(head2,7);
    display(head2);
    sum=add(head,head2);
    display(sum);
}