# Lab 5 — Amplitude Modulation Using Simulink

Return to [[Communication Engineering Assessment Index]] · Open the source manual: [[ENEL700 Lab Book 2026.pdf#page=30|ENEL700 Lab Book 2026, Lab 5 (manual page 30)]]

> [!success] Completed report
> [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Report/Lab 5 - MATLAB Replication Report|Open the certified Lab 5 MATLAB Replication Report]], including the full source reconstruction, manual-equivalent figures, Questions 1–2, numerical validation, and the Aaron-assisted plan for completing the GUI procedure exactly in Simulink.

## What this lab is

Lab 5 uses an amplitude-modulation example to introduce MATLAB and Simulink. The model is an AM double-sideband suppressed-carrier (AM-DSB/SC) modulator: a 5,000-sample message signal is multiplied by a sinusoidal carrier, viewed on a Scope, and exported to the MATLAB workspace for spectral analysis.

## Model blocks and connections

Use these blocks:

- **Signal From Workspace** (DSP System Toolbox → Sources)
- **Sine Wave** (Simulink → Sources)
- **Product** (Simulink → Math Operations)
- **Scope** (Simulink → Sinks)
- **To Workspace** (Simulink → Sinks)

Connect both sources to the two Product inputs. Branch the Product output to both Scope and To Workspace.

## Exact setup from the manual

### MATLAB message signal

```matlab
bump = sqrt(1250^2-([0:2499]-1250).^2) / 250;
bumps = [bump bump];
plot(bumps)
```

This produces a 5,000-sample, two-arch message waveform.

### Sine Wave carrier

| Parameter | Value |
| --- | --- |
| Sine type | Time based |
| Time | Use simulation time |
| Amplitude | `1` |
| Bias | `0` |
| Frequency (rad/sec) | `2*pi*0.3` |
| Phase (rad) | `pi/2` |
| Sample time | `1` |

### Signal From Workspace

| Parameter | Value |
| --- | --- |
| Signal | `bumps'` |
| Sample time | `1` |
| Samples per frame | `1` |
| Form output after final data value by | Setting to zero |

### To Workspace

| Parameter | Value |
| --- | --- |
| Variable name | `am` |
| Limit data points to last | `inf` |
| Decimation | `1` |
| Save format | Array |
| Sample time | `-1` |

Save the model as **`lab5.slx`**. In Model Configuration Parameters set:

- Start time: `0.0`
- Stop time: `5000`
- Solver type: **Fixed-step**
- Fixed-step size: `auto`

Run the model and inspect the Scope. The AM-DSB/SC waveform should have the message waveform as its envelope.

## Spectrum commands from the manual

```matlab
NFFT = 2^16;
f = [0:NFFT-1]/NFFT;
AM = abs(fft(out.am(1,:).*blackman(length(out.am)).',NFFT));
plot(f,20*log10(AM));
axis([0 0.5 -20 80]);
```

The output spectrum should be shifted from baseband to the normalized carrier frequency of `0.3`.

## Questions to complete

1. Write a `sigspec(sigin,flag)` MATLAB function that plots a signal spectrum in linear magnitude (`flag=0`) or dB (`flag=1`). The manual supplies starter code on pages 37–38.
2. Add another **To Workspace** block to capture the carrier. Use `sigspec.m` and `subplot` to display the message, carrier, and modulated-signal spectra in one figure. Explain the three plots and check that the modulated signal is scaled by one half in linear magnitude, equivalent to **−3 dB** under the manual's `10*log10` convention.

### Question 2 verified result

Question 2 was reproduced without Simulink by generating the same three signals directly in MATLAB and passing each through a completed `sigspec.m` implementation. The figure uses three vertically stacked axes as required by manual page 38:

1. **Modulating/message spectrum:** a baseband spectrum centred at normalized frequency 0.
2. **Carrier spectrum:** narrow symmetric peaks at approximately ±0.3.
3. **Modulated AM-DSB/SC spectrum:** the message spectrum shifted to symmetric sidebands around ±0.3, with the carrier itself suppressed.

The measured modulated-sideband/message peak ratio was `0.498366330964`, effectively the expected `0.5`. Using the manual's `10*log10` magnitude convention, the measured difference was `−3.02451305776 dB`, matching the expected `−3 dB`. The measured carrier peak was `0.299987792969`, matching the configured normalized frequency of `0.3`.

- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/sigspec.m|Completed sigspec.m function]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/run_lab5_question2_three_spectra.m|Question 2 MATLAB script]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_question2_three_stacked_spectra.png|Three stacked spectra figure]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_question2_spectra.mat|Question 2 spectrum data]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_question2_status.txt|Question 2 verification values]]

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_question2_three_stacked_spectra.png]]

> [!note] Source status
> The laboratory manual is already stored in this vault. Lab 5 spans manual pages 30–38 and includes the full model-building procedure, parameter screenshots, expected waveform/spectrum, and questions.

## Verified MATLAB attempt — 22 July 2026

The Lab 5 calculations were exercised in small, time-limited stages while Aaron was away from Tornado:

1. **MATLAB runtime and licence check passed.** MATLAB R2026a Update 3 completed a batch calculation successfully, and `license('test','Simulink')` returned `1`.
2. **Message-signal generation passed.** The manual's two-arch expression produced 5,000 finite real samples with amplitude from 0 to 5. The saved plot was visually checked and showed the expected two clean arches.
3. **Simulink was stopped safely.** A minimal Constant → Gain smoke model reached its 60-second hard timeout before creating a model. A still simpler `load_system('simulink')` check also reached its 30-second limit. Both processes were terminated automatically, no partial `.slx` file was produced, and no further Simulink attempt was made.
4. **MATLAB-only AM equivalent passed.** A carrier at normalized frequency 0.3 was multiplied directly by the message signal. The result contained 5,000 samples, remained inside the ±message envelope, and had a measured dominant spectral peak at `0.300003051758`, matching the required `0.3` carrier.

### Verified artifacts

- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_step1_message_plot.m|Message-signal MATLAB script]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/run_lab5_matlab_equivalent.m|MATLAB-only AM experiment script]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_message_signal.png|Message-signal plot]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_am_waveform.png|AM waveform and envelope plot]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_am_spectrum.png|AM spectrum plot]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_message_signal.mat|Message-signal data]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_matlab_results.mat|Complete MATLAB result data]]
- [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_matlab_status.txt|Machine-readable verification summary]]

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_am_waveform.png]]

![[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Artifacts/lab5_am_spectrum.png]]

> [!warning] Simulink follow-up
> MATLAB itself is working, but headless Simulink initialization currently stalls. Any later Simulink retry should begin at the `load_system('simulink')` step with a hard timeout rather than immediately rebuilding the full lab model.

> [!note]- Original Lab 5 class files
> - [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/lab5part2.slx|Simulink model]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/lab5final.mat|MATLAB data]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/finalgragh.fig|MATLAB figure]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/image.png|exported image]]
> - [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184310.png|Screenshot 1]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184343.png|Screenshot 2]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184421.png|Screenshot 3]] · [[Mechatronics Course Content/Communication Engineering/Assessments/Labs/Lab 5/Lab 5 Class Documents/Screenshot 2026-07-23 184430.png|Screenshot 4]]
