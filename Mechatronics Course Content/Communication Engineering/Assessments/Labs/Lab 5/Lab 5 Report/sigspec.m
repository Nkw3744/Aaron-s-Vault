function [f, siginspec] = sigspec(sigin, flag)
%SIGSPEC Display a signal spectrum using the ENEL700 Lab 5 method.
% Optional outputs are retained only for numerical verification.
if(nargin==0)
    disp('USAGE: sigspec(sigin,flag)');
    disp('   The input signals should be in the columns of sigin.');
    disp('   flag=0 produces a linear magnitude plot (default)');
    disp('   flag=1 produces a log magnitude plot (dB)');
    f = [];
    siginspec = [];
    return;
end

if(nargin==1)
    flag = 0;
end
[len,numsigs]=size(sigin);
if(len<numsigs)
    sigin = sigin.'; % Force the signals into the columns of sigin
    tmp = len;
    len = numsigs;
    numsigs = tmp;
end
fftsize = 2^(ceil(log2(len))+2); % Zero-padded FFT size
f=[0:fftsize-1].'/fftsize - 0.5; % Normalized frequency
sigin = repmat(hamming(len),1,numsigs).*sigin; % Window to reduce spec. leakage
siginspec = abs(fftshift(fft(sigin,fftsize),1)); % Compute spectrum
if(flag)
    plot(f,10*log10(siginspec));
    ylabel('Magnitude (dB)');
else
    plot(f,siginspec);
    ylabel('Linear magnitude');
end
xlabel('Normalized Frequency');
end
