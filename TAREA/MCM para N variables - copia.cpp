#include<iostream>
using namespace std;

int calcularMCD(int a,int b){
	if(b==0){
		return a;
	}
	return calcularMCD(b,a%b);
}

int calcularMCM(int a,int b){
	return (a*b)/calcularMCD(a,b);
}

int main(){	
	int cantidadDeNumeros,numeros[1000];
	int mcm;
	
	cout<<"=======Calculadora de MCM para N numeros========="<<endl;
	cout<<"Ingrese la cantidad de numeros: ";
	cin>>cantidadDeNumeros;
	
	for(int i=0;i<cantidadDeNumeros;i++){
		cout<<i+1<<".Digite un numero: ";
		cin>>numeros[i];
	}
	
	mcm=numeros[0];
	
	for(int i=0;i<cantidadDeNumeros;i++){
		mcm=calcularMCM(mcm,numeros[i]);
	}
	
	cout<<"\nEl MCM es : "<<mcm;

	return 0;
	system ("PAUSE");
}