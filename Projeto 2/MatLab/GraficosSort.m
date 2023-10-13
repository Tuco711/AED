x = [20000 40000 60000 80000 100000];
y = [0.0028690338134765626 0.005833101272583008 0.009419965744018554  0.014128947257995605  0.016724252700805665];

p = polyfit(x,y,1);
yfit = polyval(p,x);

hold on
plot(x,yfit)
scatter(x,y)

title('Solução por Sort')
legend('Regressão Linear', 'Pontos Reais')
hold off 