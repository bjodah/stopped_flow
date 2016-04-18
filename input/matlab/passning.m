% Antag, en funktion f(x) med två parametrar a och b:
%
%               x^b + 1
% f(x) =  a * -----------
%             x^(b+1) + 1
%
% I matlab kan den skrivas enligt:

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

% Låt se om kurvanpassning kan ge alpha och beta från
% våra brusiga data i y. Syntax för fit:
% http://se.mathworks.com/help/curvefit/fit.html
% Vi behöver anropa fittype med vår funktion, och sedan
% använda det objektet i anrop på fit:
ftyp = fittype(f);

% [1, 1] är gissning för a och b, gissningen kan behöva uppdateras
[fitobj, gof, nfo] = fit(t', y', ftyp, 'StartPoint', [1, 1]);
fitobj

% Standardavvikelsen för resp. parameter fås genom:
standard_deviation = diff(confint(fitobj, 0.6827))/2
% 0.6827 är konfidensintervallet för 1 sigma (68–95–99.7 rule)

% Root-mean-square-error (användbar för kvalitetsjämförelse)
root_mean_square_error = gof.rmse

% visualisering av "goodness of fit"
hold on;
handle = plot(t, f(fitobj.a, fitobj.b, t));
legend('Data', 'Passning');
saveas(handle, 'passning.png', 'png'); % sparar vår plot
