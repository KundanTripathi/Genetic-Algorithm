# Genetic-Algorithm
Metaheuristic Optimization

Trying to solve Combinatorial optimization which can be solved using solver in Gams in better way using following GAMS code:


set
i /f1*f5/

j /s1*s10/;


integer variable
x(i,j);

binary variable
u(i,j);


variable
z 'objective function';

table c(i,j)

    s1  s2  s3  s4  s5  s6  s7  s8  s9  s10
    
f1  1   .8  1   .6   1  .7  1   1   1   1

f2  .8  .7  .9  .8  1   .8  .9  .6  .7  1

f3  .9  .6  1   .7  .5  .9  1   .7  .9  .6

f4  .7  .4  .7  .9  .8  .8  .9  1   .7  .5 

f5  .9  .8  .6  .5  .7  .8  .9  1   .6  .8
;
parameter phi(i) /f1 100,

                  f2 120,
                  
                  f3 97,
                  
                  f4 150,
                  
                  f5 110/;
                  
parameter d(j)  /s1  30,

                 s2  51,
                 
                 s3  60,
                 
                 s4  59,
                 
                 s5  55,
                 
                 s6  37,
                 
                 s7  25,
                 
                 s8  60,
                 
                 s9  20,
                 
                 s10 10/;
                 

equation 

obj, eq1(j),eq2(i,j),eq(i,j),eq3(i);


obj.. z=e=sum((i,j),x(i,j)*c(i,j));

eq1(j).. sum((i,j),u(i,j))=e=1;

eq2(i,j).. x(i,j)=l=60*u(i,j);

eq(i,j).. x(i,j)=g=d(j)- 60*(1-u(i,j));

eq3(i)..  sum(j,x(i,j))=l=phi(i);



x.lo(i,j)=0;

x.l(i,j)=d(j);

x.up(i,j)=d(j);

model sup /all/;

option mip=cplex;

sup.Optcr = 0.02;


solve sup using mip minimization z;


Metaheuristic takes more time hence reduced the problem to 6 chromosome length and used mutation and didn't use crossover to satisfy the constraints of demand. Instead used tornament selection to seect fittest gene for mutation with mutation probability cutt-off = 0.3.
