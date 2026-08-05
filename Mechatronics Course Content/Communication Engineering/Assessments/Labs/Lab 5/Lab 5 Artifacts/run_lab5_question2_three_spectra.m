workspace = '/home/aaron/MATLAB/ENEL700/Lab5';
addpath(workspace);
n = (0:4999).';
bump = sqrt(1250^2 - ((0:2499) - 1250).^2) / 250;
message = [bump bump].';
carrier_frequency = 0.3;
carrier = sin(2*pi*carrier_frequency*n + pi/2);
modulated = message .* carrier;

fig = figure('Visible', 'off', 'Position', [100 100 1100 900]);
subplot(3,1,1);
[f, message_spectrum] = sigspec(message, 1);
title('1. Modulating (Message) Signal Spectrum');
subplot(3,1,2);
[~, carrier_spectrum] = sigspec(carrier, 1);
title('2. Carrier Signal Spectrum');
subplot(3,1,3);
[~, modulated_spectrum] = sigspec(modulated, 1);
title('3. Modulated AM-DSB/SC Signal Spectrum');
sgtitle('ENEL700 Lab 5 Question 2 — Three Signal Spectra');
plot_path = fullfile(workspace, 'lab5_question2_three_stacked_spectra.png');
print(fig, plot_path, '-dpng', '-r170');
close(fig);

message_peak = max(message_spectrum);
positive_sideband = abs(f - carrier_frequency) < 0.02;
negative_sideband = abs(f + carrier_frequency) < 0.02;
positive_peak = max(modulated_spectrum(positive_sideband));
negative_peak = max(modulated_spectrum(negative_sideband));
sideband_peak = mean([positive_peak negative_peak]);
linear_ratio = sideband_peak / message_peak;
db_difference = 10*log10(linear_ratio);
carrier_peak_frequency = abs(f(carrier_spectrum == max(carrier_spectrum)));
carrier_peak_frequency = carrier_peak_frequency(1);

assert(abs(linear_ratio - 0.5) < 0.02, 'Expected modulated sideband to be half the message peak');
assert(abs(db_difference - 10*log10(0.5)) < 0.2, 'Expected approximately -3 dB scaling');
assert(abs(carrier_peak_frequency - carrier_frequency) < 0.001, 'Carrier peak is not near 0.3');

save(fullfile(workspace, 'lab5_question2_spectra.mat'), 'f', 'message_spectrum', ...
    'carrier_spectrum', 'modulated_spectrum', 'linear_ratio', 'db_difference');
fid = fopen(fullfile(workspace, 'lab5_question2_status.txt'), 'w');
fprintf(fid, 'linear_ratio=%.12g\ndb_difference=%.12g\ncarrier_peak_frequency=%.12g\n', ...
    linear_ratio, db_difference, carrier_peak_frequency);
fclose(fid);
fprintf('QUESTION2_OK ratio=%.12g dB=%.12g carrier=%.12g\n', ...
    linear_ratio, db_difference, carrier_peak_frequency);
