#include <stdio.h>
#include <locale.h>

void main(){

    setlocale(LC_ALL,"Portuguese_Brazil");

    char nome [50];
    float janeiro;
    float fevereiro;
    float marco;
    float valorTotal;

    printf("Digite seu nome: \n");
    scanf("%s", &nome);
    printf("Digite seu quanto você guardou em janeiro, fevereiro e março: \n");
    scanf("%f %f %f", &janeiro, &fevereiro, &marco);
    valorTotal = (janeiro+fevereiro+marco);

    if(valorTotal > 1000) {
        printf("Parabéns! Você bateu a sua meta");
    }
    else
    {
    printf("Você precisa guardar mais dinheiro...");
    }
    return(0);
}
