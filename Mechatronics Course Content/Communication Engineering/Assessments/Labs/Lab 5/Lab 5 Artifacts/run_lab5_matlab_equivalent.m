workspace = '/home/aaron/MATLAB/ENEL700/Lab5';
n = 0:4999;
bump = sqrt(1250^2 - ((0:2499) - 1250).^2) / 250;
message = [bump bump];
carrier_frequency = 0.3;
carrier = sin(2*pi*carrier_frequency*n + pi/2);
am = message .* carrier;

assert(numel(message) == 5000 && numel(am) == 5000, 'Expected 5000 samples');
assert(all(isfinite(am)) && all(isreal(am)), 'AM signal must be finite and real');
assert(max(abs(am)) <= max(message) + 1e-12, 'AM signal exceeds its message envelope');

waveform_fig = figure('Visible', 'off');
plot(n(1:300), am(1:300), 'Color', [0 0.45 0.74], 'LineWidth', 1.0);
hold on;
plot(n(1:300), message(1:300), '--', 'Color', [0.85 0.33 0.10], 'LineWidth', 1.2);
plot(n(1:300), -message(1:300), '--', 'Color', [0.85 0.33 0.10], 'LineWidth', 1.2);
hold off;
grid on;
xlabel('Sample');
ylabel('Amplitude');
title('Lab 5 AM-DSB/SC Waveform and Message Envelope');
legend('AM signal', '+message envelope', '-message envelope', 'Location', 'best');
print(waveform_fig, fullfile(workspace, 'lab5_am_waveform.png'), '-dpng', '-r150');
close(waveform_fig);

NFFT = 2^16;
f = (0:NFFT-1) / NFFT;
windowed_am = am .* blackman(length(am)).';
AM = abs(fft(windowed_am, NFFT));
AM_dB = 20*log10(max(AM, eps));
half = 1:(NFFT/2 + 1);
[~, peak_index] = max(AM(half));
peak_frequency = f(peak_index);
assert(abs(peak_frequency - carrier_frequency) < 0.01, 'Spectrum peak is not near the 0.3 carrier');

spectrum_fig = figure('Visible', 'off');
plot(f(half), AM_dB(half), 'LineWidth', 1.0);
grid on;
xlim([0 0.5]);
xlabel('Normalized frequency');
ylabel('Magnitude (dB)');
title('Lab 5 AM-DSB/SC Spectrum');
xline(carrier_frequency, '--r', 'Carrier 0.3');
print(spectrum_fig, fullfile(workspace, 'lab5_am_spectrum.png'), '-dpng', '-r150');
close(spectrum_fig);

save(fullfile(workspace, 'lab5_matlab_results.mat'), 'n', 'message', 'carrier', 'am', 'f', 'AM', 'peak_frequency');
fid = fopen(fullfile(workspace, 'lab5_matlab_status.txt'), 'w');
fprintf(fid, 'samples=%d\nmessage_max=%.12g\nam_max_abs=%.12g\nspectrum_peak=%.12g\ncarrier_frequency=%.12g\n', ...
    numel(am), max(message), max(abs(am)), peak_frequency, carrier_frequency);
fclose(fid);
fprintf('LAB5_MATLAB_OK samples=%d peak_frequency=%.12g\n', numel(am), peak_frequency);
