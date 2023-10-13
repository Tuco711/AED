
n = [20000 40000 60000 80000 100000];

% Dados para Exaustão
tExaust = [4.530172657966614 21.221055650711058 43.0513578414917 105.66545600891114 125.95995230674744];

c1 = polyfit (n,tExaust,2);
xx = linspace (20000,100000,1000);
p1 = polyval(c1,xx);

hold on
title('Algoritmo de exaustão')
plot(xx,p1,'red')
hold off
