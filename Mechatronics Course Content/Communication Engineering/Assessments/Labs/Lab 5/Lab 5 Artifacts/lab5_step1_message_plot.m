workspace = '/home/aaron/MATLAB/ENEL700/Lab5';
if ~exist(workspace, 'dir')
    mkdir(workspace);
end
bump = sqrt(1250^2 - ((0:2499) - 1250).^2) / 250;
bumps = [bump bump];
assert(numel(bumps) == 5000, 'Expected 5000 samples');
assert(all(isreal(bumps)) && all(isfinite(bumps)), 'Message signal must be finite and real');
fig = figure('Visible', 'off');
plot(0:numel(bumps)-1, bumps, 'LineWidth', 1.2);
grid on;
xlabel('Sample');
ylabel('Amplitude');
title('Lab 5 Message Signal: Two-Arch Waveform');
plot_path = fullfile(workspace, 'lab5_message_signal.png');
print(fig, plot_path, '-dpng', '-r150');
close(fig);
save(fullfile(workspace, 'lab5_message_signal.mat'), 'bumps');
fid = fopen(fullfile(workspace, 'step1_status.txt'), 'w');
fprintf(fid, 'samples=%d\nmin=%.12g\nmax=%.12g\n', numel(bumps), min(bumps), max(bumps));
fclose(fid);
fprintf('STEP1_OK samples=%d min=%.12g max=%.12g\n', numel(bumps), min(bumps), max(bumps));
