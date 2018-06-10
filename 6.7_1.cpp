#include<iostream>
#include<math.h>
using namespace std;
#define Pi 3.14

class Point {
public:
	void initPoint(double x=0, double y=0){this->x=x; this->y=y;};
	virtual double CalArea() const=0;
private:
	double x,y;

};

class Rect:public Point{
public:
	Rect(double x, double y, double w, double h){
		initPoint(x,y);
		this->w=w;
		this->h=h;
	}
	double CalArea() const;
private:
	double w,h;

};

double Rect::CalArea() const {
	cout<<"the Area of Rect is "<<w*h<<endl;

}


class Circle:public Point {
public:
	Circle(double x, double y, double r){
		initPoint(x,y);
		this->r=r;
	}
	double CalArea() const;
private:
	double r;
};

double Circle::CalArea() const {
	cout<<"the Area of Circle is "<<Pi*r*r<<endl;

}

class Triangle:public Point {
public:
	Triangle(double x, double y, double a, double b, double c){
		initPoint(x,y);
		this->a=a;
		this->b=b;
		this->c=c;
	}
	double CalArea() const;
private:
	double a,b,c;
};

double Triangle::CalArea() const {
	double p = (a+b+c)/2;
	cout<<"the Area of Triangle is "<<sqrt(p*(p-a)*(p-b)*(p-c))<<endl;

}

int main()
{
	Rect object_1(2,3,20,10);
	Circle object_2(2,3,2);
	Triangle object_3(2,3,3,4,5);
	Point *p[3]={&object_1, &object_2, &object_3};
	for(int i=0;i<3;i++)
		p[i]->CalArea();
	return 0;

}

