x = [20000 40000 60000 80000 100000];

y2 = [0.0006046533584594726 0.0013065814971923828 0.002679324150085449 0.0025393486022949217 0.004190278053283691]; % Sort
y3 = [0.0028690338134765626 0.005833101272583008 0.009419965744018554  0.014128947257995605  0.016724252700805665]; % Soma

p2 = polyfit(x,y2,1);
yfit2 = polyval(p2,x);

p3 = polyfit(x,y3,1);
yfit3 = polyval(p3,x);

hold on
% Sort
plot(x,yfit2, 'red');

% Soma
plot(x,yfit3, 'blue');


scatter(x,y2,'red')
scatter(x,y3,'blue')

title('Sort x Soma')
legend('Sort', 'Soma')
hold off
