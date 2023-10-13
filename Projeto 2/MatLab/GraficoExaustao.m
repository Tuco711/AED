x = [20000 40000 60000 80000 100000];
y = [4.530172657966614 21.221055650711058 43.0513578414917 105.66545600891114 125.95995230674744];

p = polyfit(x,y,2);
yfit = polyval(p,x);

% yfitt =  p(1) * x*x + p(2) * x + p(3);

hold on
plot(x,yfit)
scatter(x,y)

title('Solução por Exaustão')
legend('Regressão Quadrática', 'Pontos Reais')
hold off 