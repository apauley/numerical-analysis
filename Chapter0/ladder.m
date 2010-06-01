# The ladder example on page 7
# Language: Octave/Matlab

a = 123*2*pi/360;
L = inline('9/sin(pi-(123*2*pi/360)-c)+7/sin(c)');
fplot(L, [0.4, 0.5]); grid on
minPoint = fminbnd(L, 0.4, 0.5)
L(minPoint)
