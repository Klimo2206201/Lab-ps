#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x,g,y,f;
printf ("Vvedite x: ");
scanf ("%f",&x);
printf ( "Vvedite a");
scanf ("%f" , &a);
g =  5*(-9*a*a + 11*a*x + 14*x*x)/(15*a*a + 49*a*x + 24*x*x)
;
printf ("g=%f\n\n", g);

printf ("Vvedite x ");
scanf ("%f", &a);
printf ("Vvedite a ");
scanf ("%f", &a);
f = tan(18*a*a + 29*a*x + 10*x*x)
;
printf ("f=%f\n\n", f);

printf ("Vvedite x");
scanf ("%f", &x);
printf ("Vvedite a");
scanf ("%f", &a);
y=acos(-7*a*a - 10*a*x + 8*x*x + 1);
printf  ("y=%f\n\n", y);
}
