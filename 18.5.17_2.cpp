#include<iostream>
using namespace std;

void parse(int dio){
    if(dio%3 == 0){
        cout<<dio<<"��3�ı���"<<endl;
    }
    else{
        cout<<dio<<"����3�ı���"<<endl;
    }
    if(dio%5 == 0){
        cout<<dio<<"��5�ı���"<<endl;
    }
    else{
        cout<<dio<<"����5�ı���"<<endl;
    }
    if(dio%7 == 0){
        cout<<dio<<"��7�ı���"<<endl;
    }
    else{
        cout<<dio<<"����7�ı���"<<endl;
    }
}

int main()
{
    int dio;
    while(true){
        cout<<"������:";
        cin>>dio;
        parse(dio);
    }
}
