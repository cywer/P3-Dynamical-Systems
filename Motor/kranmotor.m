Ra = 1.22;
Ke = 0.032;
J = 382*10^-6;
b = 0.09*10^-3;

A = -((Ra*Ke^2)/J + b/J);
B = Ke/(J*Ra);
C = 1;
D = 0;

T = 0:0.1:20;
U = ones(size(T))*5;
X0 = [0];

sys = ss(A,B,C,D)
lsim(sys,U,T,X0)