#include<iostream>
#include<csdlib>
#include<ctime>
#include<time.h>

#define max 100
srand((unsigned)time(NULL));

Class Card{
private:
	int top;
	char date[max][11];
	int money[max];
	int rest[max];
	static int sum;
Public:
	Card();
	~Card();
	void Cardin(char d[], int m);
	void Cardout(char d[], int m);
	void disp();
}
int Card::sum=0;

Card::Card(){
	top = rand();
	const time_t t = time(NULL);
	struct tm* current_time = localtime(&t);
	date[current_time->tm_mday][current_time->tm_mon] = string(t);
}


void Card::Cardin(char d[], int m){

}
