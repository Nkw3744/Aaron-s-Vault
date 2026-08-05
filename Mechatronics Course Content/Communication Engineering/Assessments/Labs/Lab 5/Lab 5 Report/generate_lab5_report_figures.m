workspace = '/home/aaron/MATLAB/ENEL700/Lab5';
report_dir = fullfile(workspace, 'report_figures');
if ~exist(report_dir, 'dir')
    mkdir(report_dir);
end
n = (0:4999).';
bump = sqrt(1250^2 - ((0:2499) - 1250).^2) / 250;
message = [bump bump].';
carrier_frequency = 0.3;
carrier = sin(2*pi*carrier_frequency*n + pi/2);
am = message .* carrier;

% Manual Figure 23 equivalent: message information.
fig23 = figure('Visible','off','Position',[100 100 1100 600]);
plot(n,message,'LineWidth',1.2);
grid on;
xlim([0 5000]); ylim([0 5.2]);
xlabel('Sample'); ylabel('Amplitude');
title('Figure 23 Equivalent — 5000-Sample Message Information');
print(fig23,fullfile(report_dir,'figure23_message_information.png'),'-dpng','-r170');
close(fig23);

% Manual Figure 27 equivalent: full AM-DSB/SC output waveform.
fig27 = figure('Visible','off','Position',[100 100 1100 600]);
plot(n,am,'Color',[0 0.45 0.74],'LineWidth',0.7);
grid on;
xlim([0 5000]); ylim([-5.2 5.2]);
xlabel('Sample'); ylabel('Amplitude');
title('Figure 27 Equivalent — AM-DSB/SC Output Waveform');
print(fig27,fullfile(report_dir,'figure27_am_output_waveform.png'),'-dpng','-r170');
close(fig27);

% Zoomed waveform with message envelope, useful for verification.
fig27z = figure('Visible','off','Position',[100 100 1100 600]);
plot(n(1:300),am(1:300),'Color',[0 0.45 0.74],'LineWidth',1.0);
hold on;
plot(n(1:300),message(1:300),'--','Color',[0.85 0.33 0.10],'LineWidth',1.2);
plot(n(1:300),-message(1:300),'--','Color',[0.85 0.33 0.10],'LineWidth',1.2);
hold off; grid on;
xlabel('Sample'); ylabel('Amplitude');
title('AM-DSB/SC Output — Zoomed Verification of the Message Envelope');
legend('AM signal','+message envelope','-message envelope','Location','best');
print(fig27z,fullfile(report_dir,'figure27_am_output_waveform_zoom.png'),'-dpng','-r170');
close(fig27z);

% Manual Figure 28 equivalent, using its Blackman-window and 20*log10 convention.
NFFT = 2^16;
f = (0:NFFT-1).' / NFFT;
AM = abs(fft(am .* blackman(length(am)),NFFT));
AMdB = 20*log10(max(AM,eps));
half = f <= 0.5;
[~,peak_idx] = max(AM(half));
f_half = f(half);
peak_frequency = f_half(peak_idx);
fig28 = figure('Visible','off','Position',[100 100 1100 600]);
plot(f(half),AMdB(half),'LineWidth',1.1);
grid on;
axis([0 0.5 -20 80]);
xlabel('Normalized frequency'); ylabel('Magnitude (dB)');
title('Figure 28 Equivalent — AM-DSB/SC Output Spectrum');
xline(carrier_frequency,'--r','Carrier 0.3');
print(fig28,fullfile(report_dir,'figure28_output_spectrum.png'),'-dpng','-r170');
close(fig28);

% Manual Figure 29 equivalents already produced with the Question 1 sigspec function.
copyfile(fullfile(workspace,'lab5_question2_three_stacked_spectra_log.png'), ...
    fullfile(report_dir,'figure29_output_spectra_log.png'));
copyfile(fullfile(workspace,'lab5_question2_three_stacked_spectra_linear.png'), ...
    fullfile(report_dir,'figure29_output_spectra_linear.png'));

fid=fopen(fullfile(report_dir,'report_figure_status.txt'),'w');
fprintf(fid,'samples=%d\nmessage_max=%.12g\nam_max_abs=%.12g\nfigure28_peak_frequency=%.12g\n', ...
    numel(message),max(message),max(abs(am)),peak_frequency);
fclose(fid);
fprintf('REPORT_FIGURES_OK samples=%d peak=%.12g\n',numel(message),peak_frequency);
