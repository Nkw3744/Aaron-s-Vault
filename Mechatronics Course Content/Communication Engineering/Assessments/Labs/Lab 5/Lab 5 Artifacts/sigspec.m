function [f, siginspec] = sigspec(sigin, flag)
%SIGSPEC Plot the centered spectrum of one or more column signals.
%   SIGSPEC(SIGIN,0) plots linear magnitude.
%   SIGSPEC(SIGIN,1) plots 10*log10 magnitude, matching ENEL700 Lab 5.
if nargin < 2
    flag = 0;
end
if isvector(sigin)
    sigin = sigin(:);
end
[len, numsigs] = size(sigin);
fftsize = 2^(ceil(log2(len)) + 2);
f = (0:fftsize-1).' / fftsize - 0.5;
windowed = repmat(hamming(len), 1, numsigs) .* sigin;
siginspec = abs(fftshift(fft(windowed, fftsize, 1), 1));
if flag
    plot(f, 10*log10(max(siginspec, eps)));
    ylabel('Magnitude (dB)');
else
    plot(f, siginspec);
    ylabel('Linear magnitude');
end
xlabel('Normalized frequency');
grid on;
xlim([-0.5 0.5]);
end
