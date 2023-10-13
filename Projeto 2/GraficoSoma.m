n = [20000 40000 60000 80000 100000];

% Dados para Exaustão
tExaust = [0.0006046533584594726 0.0013065814971923828 0.002679324150085449 0.0025393486022949217 0.004190278053283691];

c1 = polyfit (n,tExaust,2);
xx = linspace (20000,100000,1000);
p1 = polyval(c1,xx);

hold on
title('Algoritmo de soma')
plot(xx,p1,'green')
hold off
