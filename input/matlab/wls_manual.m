% Detta skript visar hur man passar en rät linje
%      y(x) = k*x + m
% till en dataserie med varianser (s2)

x = [1.3 2.7 3.5 7.8 9.2]';
y = [6.5 11.7 13.6 23.2 33.2]';
s2 = [1.3 0.9 0.6 13.4 2.2]';

% Vi kan plotta punkterna med osäkerheten utritad
% errorbar(x, y, s2.^0.5, 'o');

% Låt oss först göra en oviktad minsta-kvadrat-anpassning:
% A'A c = A'y
A = [ones(size(x)), x];
c_ols = A\y  % (Matlab löser med hjälp SVD eller QR)
r_ols = A*c_ols - y;

% Formeln för WLS: (se Weighted least squares på wikipedia):
Aw = A./[s2 s2].^0.5;
yw = (y./s2.^0.5);
c_wls = Aw \ yw

r_wls = Aw*c_wls - yw;

% varians-kovarians matriser för parametrarna:
size_x = size(x);
nx = size_x(1);
vcv_ols = r_ols'*r_ols ./ (nx - 2) .* inv(A'*A);
vcv_wls = r_wls'*r_wls ./ (nx - 2) .* inv(Aw'*Aw);

stderr_ols = sqrt(diag(vcv_ols))
stderr_wls = sqrt(diag(vcv_wls))
