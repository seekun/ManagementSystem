    #include<iostream>
    #include"math.h"
    using namespace std;

    const float PI = 3.141593;
    class Gragh {
    public:
        Gragh(float r);
        Gragh(float l, float w);
        Gragh(float e1, float e2, float e3);
        float Calculate_perimeter_1();
        float Calculate_perimeter_2();
        float Calculate_perimeter_3();
    private:
        float radius;
        float length;
        float width;
        float edge_1;
        float edge_2;
        float edge_3;
    };

    Gragh::Gragh(float r){
        radius = r;
    }

    float Gragh::Calculate_perimeter_1(){
        return PI*radius*radius;
    }

    Gragh::Gragh(float l, float w){
        length = l;
        width = w;
    }

    float Gragh::Calculate_perimeter_2(){
        return length*width;
    }

    Gragh::Gragh(float e1, float e2, float e3){
        edge_1 = e1;
        edge_2 = e2;
        edge_3 = e3;
    }

    float Gragh::Calculate_perimeter_3(){
        float P;
        P = (edge_1+edge_2+edge_3)/2;
        return sqrt(P*(P-edge_1)*(P-edge_2)*(P-edge_3));
    }

    int main(){
        float a=-1, b=-1, c=-1,S;
        cout<<"Enter the data_1(NuLL == 0):";
        cin>>a;
        cout<<"Enter the data_2(NuLL == 0):";
        cin>>b;
        cout<<"Enter the data_3(NuLL == 0):";
        cin>>c;
        if(a==0&&b==0&&c==0)
        {
            cout<<"Error"<<endl;
        }
        else if(a!=0&&b==0&&c==0)
        {
            Gragh G(a);
            S = G.Calculate_perimeter_1();
            cout<<S<<endl;
        }
        else if(a!=0&&b!=0&&c==0)
        {
            Gragh G(a,b);
            S = G.Calculate_perimeter_2();
            cout<<S<<endl;
        }
        else if(a!=0&&b!=0&&c!=0)
        {
            Gragh G(a,b,c);
            S = G.Calculate_perimeter_3();
            cout<<S<<endl;
        }
    }



