#include<iostream>
using namespace std;
int main(){
    cout<<"========BUSQUEDA BINARIA PARA N NUMEROS======="<<endl;
    int i,j,limite;
    int numeros[100];
    int mitad,min,max;
    int target;
    
    cout<<"Cuantos numeros desea ingresar al arreglo: ";
    cin>>limite;
    
    //Llenando el arreglo con #s del usuario
    for(i=0;i<limite;i++){
        cout<<i+1<<".Digite un numero: ";
        cin>>numeros[i];
    }
    
    //Ordenando el arreglo
    for(i=0;i<limite;i++){
        for(j=0;j<limite-1;j++){
            if(numeros[j]>numeros[j+1]){
                int aux;
                aux=numeros[j];
                numeros[j]=numeros[j+1];
                numeros[j+1]=aux;
            }
        }
    }
    

    
    //Aplicando Busqueda Binaria
    cout<<"Digite el numero que desea buscar: ";
    cin>>target;
    min=0;
    max=limite-1;
    while(min<=max){
        mitad = (min+max)/2;
        if(target == numeros[mitad]){
            cout<<"\nEl numero fue encontrado en la posicion: "<<mitad+1<<endl;
            break;
        }
        else if(numeros[mitad]<target){
            min=mitad+1;
        }
        else{
            max=mitad-1;
        }
    }
    
	if (min > max) {
        cout << "\nEl numero no fue ingresado." << endl;
    }
    
    return 0;
}