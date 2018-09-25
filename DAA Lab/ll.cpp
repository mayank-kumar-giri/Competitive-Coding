#include<iostream>
#include<stdlib.h>
using namespace std;
typedef struct ll
{
int data;
struct ll *next;
}node;

node* create()
{
char r;
int count=0;
node *cn;
node *start=NULL;
do
{
count++;
node *a=(node *)malloc(sizeof(node));
cout<<"\nEnter data for your node- "<<count<<" ";
cin>>a->data;
a->next=NULL;
if(start==NULL)
{
start=a;
cn=start;
}
else
{
cn->next=a;
cn=a;
}
cout<<"\nDo you want to continue?(y/n)";
cin>>r;
}while(r != 'n');
return start;
}


void insB(node *start)
{
int valb;
cout<<"\nEnter the value before which you want node";
cin>>valb;
node *ptr,*pptr;
ptr=start;
node *a=(node *)malloc(sizeof(node));
cout<<"\nEnter data for your new node";
cin>>a->data;
a->next=NULL;
if(ptr->data==valb)
{
a->next=start;
start=a;
}
else
{
while(ptr->data != valb)
{
pptr=ptr;
ptr=ptr->next;
}
pptr->next=a;
a->next=ptr;
}
}


void display(node *start)
{
node *cn;
cn=start;
while(cn!=NULL)
{
cout<<"\n"<<cn->data<<"\n";
cn=cn->next;
}
}


void insA(node *start)
{
int vala;
cout<<"\nEnter the value after which you want node";
cin>>vala;
node *ptr;
ptr=start;
node *a=(node *)malloc(sizeof(node));
cout<<"\nEnter data for your new node";
cin>>a->data;
a->next=NULL;
while(ptr->data != vala)
{
ptr=ptr->next;
}
a->next=ptr->next;
ptr->next=a;
}


void insE(node *start)
{
node *ptr;
ptr=start;
node *a=(node *)malloc(sizeof(node));
cout<<"\nEnter data for your new node";
cin>>a->data;
a->next=NULL;
while(ptr != NULL)
{
ptr=ptr->next;
}
ptr->next=a;
}


void del(node *start)
{
int val;
cout<<"\nEnter the value of node which you want to delete";
cin>>val;
node *ptr,*pptr;
ptr=start;
while(ptr->data != val)
{
pptr=ptr;
ptr=ptr->next;
}
pptr->next=ptr->next;
free(ptr);
}


void delALL(node *start)
{
node *ptr,*pptr;
ptr=start;
while(ptr != NULL)
{
pptr=ptr;
ptr=ptr->next;
free(pptr);
node *pptr;
}
free(ptr);
free(pptr);
}
