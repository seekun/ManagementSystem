#include<iostream>
#include<string.h>
using namespace std;

void parse_str(char *str){
    char flag = '\0';
    int asc[256]={0};
    for(int i=0; i<strlen(str); i++)
        asc[str[i]]++;
    for(int i=0; i<strlen(str); i++)
    {
        if(asc[str[i]]==1)
        {
            flag = char(str[i]);
            break;
        }
    }
    cout<<flag<<endl;
}

int main()
{
    char str[100];
    while(true){
        cout<<"ÇëÊäÈë×Ö·û´®:"<<endl;
        cin>>str;
        parse_str(str);
    }
}

