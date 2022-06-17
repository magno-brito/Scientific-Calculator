#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define MAX 1024
int tempo = 0;

struct Cliente{
    int numero;
    int entrada;
    int atendimento;
};
typedef struct Cliente cliente;

struct queue{
    int vef;
	int front;
	int rear;
	cliente data[MAX];
};
typedef struct queue Queue;

void createQueue(Queue *f);  
int isEmpty(Queue *f);      
int isFull(Queue *f);      
void printQueue(Queue *f);   
void enQueue(Queue *f, cliente valor);  
void deQueue(Queue *f);             
int peek(Queue *f, int *valor);    
cliente gerarCliente();

//---------------------------------------------------------------------------
int main(){
	Queue *fila = malloc(sizeof(Queue));
    srand(time(NULL));
	createQueue(fila);
    cliente primeiro_cliente = gerarCliente();
    enQueue(fila,primeiro_cliente);
    printf("Cliente %d -- Chegada (%d) -- Atendimento (%d)\n",
                primeiro_cliente.numero, 
                primeiro_cliente.entrada, 
                primeiro_cliente.atendimento);
    while(tempo <= 20){
        printf("%d\n", tempo);
        if(fila->data[fila->front].entrada == tempo){
            cliente novo_cliente = gerarCliente();
            novo_cliente.numero = tempo;
            printf("Cliente %d -- Chegada (%d) -- Atendimento (%d)\n",
                novo_cliente.numero, 
                novo_cliente.entrada, 
                novo_cliente.atendimento);
            enQueue(fila,novo_cliente);
        }
        if(fila->data[fila->front].entrada == tempo){
            printf(" Cliente %d está sendo atendido\n",fila->data[fila->front].numero);
        }
        
        
        tempo++;
    }
	printQueue(fila);
   
}
//----------------------------------------------------------------------------

cliente gerarCliente(){
    cliente cliente;
    int chegada, atendimento;
     srand(time(NULL));
    chegada = rand()%3;
    atendimento = rand()%4 + 1;
    cliente.entrada = chegada + tempo;
    cliente.atendimento = atendimento + cliente.entrada;
    return cliente;
    
}
void createQueue(Queue *f){
	f->front = 0;
    f->rear = 0;
}
int isEmpty(Queue *f){
    if(f->front == 0 && f->rear == 0) return 1;
    return 0;
}      
int isFull(Queue *f){
    if(f->rear == MAX) return 1;
    return 0;
}
void enQueue(Queue *f, cliente valor){
    if(isEmpty(f) == 1){
        f->data[f->front] = valor;
        f->rear ++;
    }else if(isFull(f) == 1){
        printf("Is Full\n");
    }
    else{
        f->data[f->rear] = valor;
        f->rear++;
    }  
}
void deQueue(Queue *f){
    if(isEmpty(f) == 1 ) {
        printf("Is Empty\n");
        }
    else{
        
        cliente temporario = f->data[f->front];
        for(int i = f->front; i < f->rear-1; i++){
            cliente temp = f->data[i+1];
            f->data[i] = f->data[i+1];
            }
        f->rear--;
            
        }
        //int valor_retirado;
        //valor_retirado = f->front;
        //f->front++;
}
void printQueue(Queue *f){
    for(int i = f->front; i < f->rear; i++){
        if(i == f->rear-1) printf(" Cliente - %d",f->data[i]);
        else printf(" Cliente - %d <- ",f->data[i]);
    }
    printf("\n"); 
}


