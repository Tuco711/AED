x = [20000 40000 60000 80000 100000];

y1 =  [4.530172657966614 21.221055650711058 43.0513578414917 105.66545600891114 125.95995230674744]; % Exaustão
y2 = [0.0006046533584594726 0.0013065814971923828 0.002679324150085449 0.0025393486022949217 0.004190278053283691]; % Sort
y3 = [0.0028690338134765626 0.005833101272583008 0.009419965744018554  0.014128947257995605  0.016724252700805665]; % Soma


p1 = polyfit(x,y1,2);
yfit1 = polyval(p1,x);

p2 = polyfit(x,y2,1);
yfit2 = polyval(p2,x);

p3 = polyfit(x,y3,1);
yfit3 = polyval(p3,x);

hold on
% Exaustão
plot(x,yfit1,'green');


% Sort
plot(x,yfit2, 'red');

% Soma
plot(x,yfit3, 'blue', LineStyle='--');

scatter(x,y3,'blue')
scatter(x,y1, 'green')
scatter(x,y3,'red')


title('Comparação dos Resultados')
legend('Exaustão', 'Sort', 'Soma')
hold off



