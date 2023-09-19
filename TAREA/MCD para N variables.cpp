#include<iostream>
using namespace std;
/*EL ALGORITMO DE EUCLIDES se basa en que el MCD de dos números no cambia 
si se reemplaza uno de los números por el residuo de su división por el otro. */

int calcularMCD(int a,int b){
	if(b==0){
		return a;
	}
	return calcularMCD(b,a%b);
}

int main(){	
	int cantidadDeNumeros,numeros[1000],mcd;
	
	cout<<"=======Calculadora de MCD para N numeros========="<<endl;
	cout<<"Ingrese la cantidad de numeros: ";
	cin>>cantidadDeNumeros;
	
	for(int i=0;i<cantidadDeNumeros;i++){
		cout<<i+1<<".Digite un numero: ";
		cin>>numeros[i];
	}
	
	mcd=numeros[0];
	
	for(int i=1;i<cantidadDeNumeros;i++){
		mcd=calcularMCD(mcd,numeros[i]);
	}
	
	cout<<"\nEl MCD de los numeros es: "<<mcd;
	
	return 0;
	system ("PAUSE");
}