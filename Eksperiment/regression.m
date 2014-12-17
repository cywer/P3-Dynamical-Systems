m = [0, 1.2, 2, 2.4, 3.2, 4];
Vm = [0.62, 2.60, 3.66, 4.19, 5.44, 7.22];
th = [-30, -20, -10, 0, 10, 20, 30];
Vth = [1.89, 2.15, 2.51, 2.8, 3.09, 3.34, 3.54];
l = [37.5, 49, 98, 78, 68];
Vl = [1.48, 2.13, 4.24, 3.40, 2.95];

t1=linspace(0,7.5,50); 
pm = polyfit(Vm, m, 1); 
fit1 = polyval(pm, t1); 
subplot(2,2,1);
plot(t1, fit1, Vm, m,'.');
title('Kranens position');
xlabel('Spænding [v]');
ylabel('Position fra 0 [m]');

t2=linspace(1.89,3.54, 50); 
pth = polyfit(Vth, th, 1); 
fit2 = polyval(pth, t2); 
subplot(2,2,2);
plot(t2, fit2, Vth, th,'.');
title('Vinklen');
xlabel('Spænding [v]');
ylabel('Vinkel [ ^{\circ} ]');

t3=linspace(1.48,4.24,50); 
pl = polyfit(Vl, l, 1); 
fit3 = polyval(pl, t3); 
subplot(2,2,3);
plot(t3, fit3, Vl, l,'.');
title('Længden');
xlabel('Spænding [v]');
ylabel('Længde [cm]');

