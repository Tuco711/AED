x = [20000 40000 60000 80000 100000];
y = [0.0006046533584594726 0.0013065814971923828 0.002679324150085449 0.0025393486022949217 0.004190278053283691];

p = polyfit(x,y,1);
yfit = polyval(p,x);

hold on
plot(x,yfit)
scatter(x,y)

title('Solução por Soma')
legend('Regressão Linear', 'Pontos Reais')
hold off 