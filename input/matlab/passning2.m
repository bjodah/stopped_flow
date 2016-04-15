% Antag att vi har en ickelinjär funktion f(x) med två
% parametrar a och b:
%
%               x^b + 1
% f(x) =  a * -----------
%             x^(b+1) + 1
%
% Funktionen f(x) är enkel och kan beskrivas i matlab som:
%
%    f = @(a, b, x) (a*(x.^b + 1)./(x.^(b+1) + 1));
%
% men låt oss låtsas att den är lång och att vi vill uttrycka
% den i termer av en hjälpfunktion g(p, x) (detta är något ni
% kan vilja använda er av):
g = @(p, x) (x.^p + 1);
f = @(a, b, x) (a*g(b, x)./g(b+1, x));

% Antag att f(t) är en observabel med mätosäkerhet
% vi kan simulera detta med normalfördelat brus
% (ni kommer istället att läsa in data från en textfil,
% exempelvis mha. funktionen ``load``):
N = 1000; t = linspace(0, 4, N);
alpha = 2.0; beta = 3.0;
rng('default'); % ger reproducerbara stokastiska värden
y = f(alpha, beta, t) + random('Normal', 0, 0.1, 1, N);


% Låt oss plotta mätdata:
plot(t, y);

% Låt oss nu se ifall vi kan genom kurvanpassning
% bestämma alpha och beta från våra brusiga data i y.
resfcn = @(params) f(params(1), params(2), t) - y;
result = fsolve(resfcn, [1.0, 1.0])
% [1.0, 1.0] är gissning för a och b, gissningen kan behöva uppdateras

% vi kan rita in passningen över våra brusiga data för att
% få en visualisering av "goodness of fit"
hold on;
handle = plot(t, f(result(1), result(2), t));
legend('Data', 'Passning');
saveas(handle, 'passning.png', 'png'); % sparar vår plot
