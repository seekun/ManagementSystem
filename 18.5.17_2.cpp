#include<iostream>
using namespace std;

void parse(int dio){
    if(dio%3 == 0){
        cout<<dio<<"是3的倍数"<<endl;
    }
    else{
        cout<<dio<<"不是3的倍数"<<endl;
    }
    if(dio%5 == 0){
        cout<<dio<<"是5的倍数"<<endl;
    }
    else{
        cout<<dio<<"不是5的倍数"<<endl;
    }
    if(dio%7 == 0){
        cout<<dio<<"是7的倍数"<<endl;
    }
    else{
        cout<<dio<<"不是7的倍数"<<endl;
    }
}

int main()
{
    int dio;
    while(true){
        cout<<"请输入:";
        cin>>dio;
        parse(dio);
    }
}
