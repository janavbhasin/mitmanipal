#include <stdio.h>
#include <stdlib.h>
typedef struct complex
{
    float r,i;
}complex;
complex add(complex c1,complex c2)
{
    complex temp;
    temp.r=c1.r+c2.r;
    temp.i=c1.i+c2.i;
    return temp;
}
complex sub(complex c1,complex c2)
{
    complex temp;
    temp.r=c1.r-c2.r;
    temp.i=c1.i-c2.i;
    return temp;
}
complex mul(complex c1,complex c2)
{
    complex temp;
    temp.r=(c1.r*c2.r)+(c1.i*c2.i);
    temp.i=(c1.i*c2.r)+(c1.r*c2.i);
    return temp;
}
int main()
{
    complex c1,c2;
    printf("enter the 1st complex number:\n");
    scanf("%f%f",&c1.r,&c1.i);
    printf("enter the 2nd complex number:\n");
    scanf("%f%f",&c2.r,&c2.i);
    complex sum=add(c1,c2);
    complex difference=sub(c1,c2);
    complex product=mul(c1,c2);
    printf("the sum is : %.2f+%.2fi\n",sum.r,sum.i);
    printf("the difference is : %.2f+%.2fi\n",difference.r,difference.i);
    printf("the product is : %.2f+%.2fi\n",product.r,product.i);
}