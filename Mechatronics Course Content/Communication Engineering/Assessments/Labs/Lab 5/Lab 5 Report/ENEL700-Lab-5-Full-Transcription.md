# ENEL700 Lab 5 — Full Instructional Transcription

Source: [[ENEL700 Lab Book 2026.pdf#page=30|ENEL700 Lab Book 2026, pages 30–38]]

Transcribed page-by-page from rendered manual images on 22 July 2026. Code, parameters, question wording, and figure captions were visually cross-checked against the page images. This is an accessible instructional transcription rather than a pixel-for-pixel reproduction of every application-window menu label.

# LAB 5 — AMPLITUDE MODULATION USING SIMULINK

## Manual page 30

### 1 Objective

To be familiar with Simulink (Matlab) using amplitude modulation as an example.

### 2 Theory

Amplitude modulation (AM) is a modulation technique used in electronic communication, most commonly for transmitting information via a radio carrier wave. In amplitude modulation, the amplitude (signal strength) of the carrier wave is varied in proportion to the waveform being transmitted. That waveform may, for instance, correspond to the sounds to be reproduced by a loudspeaker, or the light intensity of television pixels. This technique contrasts with frequency modulation, in which the frequency of the carrier signal is varied, and phase modulation, in which its phase is varied.

### 3 Equipment

1. Desktop PC with Matlab installed.
2. Lecture notes related to amplitude modulation.

### 4 Method and Questions

Be familiar with Matlab and Simulink by watching the linked online video or reading the linked Simulink tutorial in the manual.

### 4.1 Start Simulink Programme

Start up Matlab by double-clicking the shortcut on the desktop.

Start up Simulink by typing at the Matlab prompt:

```matlab
Simulink
```

You should see the Simulink Block Library windows as shown below.

**Figure 15. Simulink Block Library**

## Manual page 31

### 4.2 Create Simulink Model for AM-DSB/SC

From the File menu, select **New → Simulink Model**.

**Figure 16. New Simulink Model**

We will start by building and testing an AM-DSB/SC modulator.

Click on the **Sources** block in the Simulink Block Library window. The Sources Block Library should open as shown below.

**Figure 17. Simulink Source Library**

Drag and drop a **Sine Wave** block from the Sources Library to the Model window.

Click on **DSP System Toolbox**, then **Sources**.

## Manual page 32

The DSP System Toolbox/Sources library contains the **Signal From Workspace** block.

**Figure 18. DSP Source Library**

Drag and drop the **Signal From Workspace** block into the Model window.

Click on the Simulink Block Library, then **Math Operations**.

**Figure 19. Simulink Math Operations Library**

Drag and drop the **Product** block onto the Model window.

Click on the **Sinks** block in the Simulink Block Library window. The Sinks Block Library window should open as shown below.

## Manual page 33

**Figure 20. Simulink Sink Library**

The relevant Sinks shown are **Scope** and **To Workspace**.

Connect the blocks with signal flow lines. The Model window should now contain:

- Signal From Workspace → Product input
- Sine Wave → Product input
- Product output branched to Scope
- Product output branched to To Workspace

**Figure 21. Built Simulink Model**

### 4.3 Setting up the Simulation

Open the **Sine Wave** block by double-clicking on it. Set the parameters as follows.

## Manual page 34

### Sine Wave parameters

The block describes its output as:

```text
O(t) = Amp*Sin(Freq*t+Phase) + Bias
```

Set:

- Sine type: **Time based**
- Time (t): **Use simulation time**
- Amplitude: `1`
- Bias: `0`
- Frequency (rad/sec): `2*pi*0.3`
- Phase (rad): `pi/2`
- Sample time: `1`
- Interpret vector parameters as 1-D: checked

**Figure 22. Sinusoidal Source Property Window**

Click **OK** when you are done to set the parameters of the Sine Wave block.

In the Matlab Command Window define the signal `bumps` by typing:

```matlab
bump = sqrt(1250^2-([0:2499]-1250).^2) / 250;
bumps = [bump bump];
plot(bumps)
```

The resulting plot should look something like the displayed two arches. The manual asks: “Do you recognize the McDonald's ‘Golden Arches’?”

**Figure 23. Message Information**

## Manual page 35

This signal is 5000 samples long and will be used as the modulating signal for the AM-DSB/SC modulator. To let Simulink know that we want this for our source signal, double-click the From Workspace block in the Model window and set the parameters as shown below.

### Signal From Workspace parameters

- Signal: `bumps'`
- Sample time: `1`
- Samples per frame: `1`
- Form output after final data value by: **Setting to zero**

**Figure 24. Signal from Workspace Property Window**

Double-click the To Workspace block in the Model window and set the parameters as shown below.

### To Workspace parameters

- Variable name: `am`
- Limit data points to last: `inf`
- Decimation: `1`
- Save format: **Array**
- Save 2-D signals as: **3-D array (concatenate along third dimension)**
- Log fixed-point data as a fi object: checked
- Sample time (-1 for inherited): `-1`

**Figure 25. Output to Workspace Property Window**

Click **OK** to set the values.

### 4.4 Save Simulink Model and Configure Simulation Parameters

Save your model by selecting **Save as…** in the File menu in the Model window.

Call this model **`lab5.slx`**.

Bring up the simulation parameters dialog from the Simulation menu in the Model window; select **Model Configuration Parameter** (`Ctrl+E`).

Under Simulation time, change the **Stop time** to `5000`.

Under Solver options, change the **Type** to **Fixed-step**.

## Manual page 36

The Configuration Parameters window should look something like Figure 26.

### Configuration values shown

- Start time: `0.0`
- Stop time: `5000`
- Type: **Fixed-step**
- Solver: `ode3 (Bogacki-Shampine)`
- Fixed-step size (fundamental sample time): `auto`

**Figure 26. Simulation Configuration Parameters Window**

Set the values by clicking **OK**. Next select **Run** (`Ctrl+T`) from the Simulation menu in the Model window.

### 4.5 Simulation Results

Open the Scope display by double-clicking on the Scope. You should see an AM-DSB/SC output waveform whose envelope corresponds to the two-arch message.

**Figure 27. AM-DSB/SC Output Waveform**

You can zoom in to verify that this is an amplitude-modulated wave corresponding to the modulating signal given above. By entering the following in the Matlab Command Window, you can see that the original modulating signal has been moved from baseband to a carrier frequency at `0.3`.

## Manual page 37

### Output-spectrum commands

```matlab
NFFT=2^16;
f=[0:NFFT-1]/NFFT;
AM=abs(fft(out.am(1,:).*blackman(length(out.am)).',NFFT));
plot(f,20*log10(AM));
axis([0 0.5 -20 80]);
```

**Figure 28. Output Spectrum**

## 5 Questions

### Question 1

Write a Matlab function that will display the spectrum of a signal. Here is some code that you may want to try:

```matlab
function sigspec(sigin,flag)
if(nargin==0)
    disp('USAGE: sigspec(sigin,flag)');
    disp('   The input signals should be in the columns of sigin.');
    disp('   flag=0 produces a linear magnitude plot (default)');
    disp('   flag=1 produces a log magnitude plot (dB)');
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
```

The function continues on manual page 38.

## Manual page 38

### Question 1 starter code continued

```matlab
fftsize = 2^(ceil(log2(len))+2); % Zero-padded FFT size
f=[0:fftsize-1].'/fftsize - 0.5; % Normalized frequency
sigin = repmat(hamming(len),1,numsigs).*sigin; % Window to reduce spec. leakage
siginspec = abs(fftshift(fft(sigin,fftsize),1)); % Compute spectrum
if(flag)
    plot(f,10*log10(siginspec));
else
    plot(f,siginspec);
end
xlabel('Normalized Frequency');
ylabel('Magnitude (dB)');
```

### Question 2

In the Simulink model created above, there are three signals:

1. the modulating signal;
2. the carrier signal;
3. the modulated signal.

The modulating signal and the modulated signal should already exist in the Matlab workspace. Add another **To Workspace** block to the model and connect it to the carrier signal. Run the simulation. Then all three signals should exist in the Matlab workspace.

Use the `sigspec.m` function that you wrote previously to plot the spectra of the three signals. Plot all three signals in the same figure window but in different axes. Use the `subplot` function in Matlab to accomplish this. If you have never used `subplot`, at the Matlab prompt type:

```matlab
help subplot
```

Write an explanation of the three plots. Comment on the scaling of the modulated signal relative to the modulating signal. The scaling should be one half in the linear scale and `-3 dB` on the log scale. To get an accurate measurement, you may need to zoom in to read off the correct value of the peak. A log plot would look something like Figure 29.

**Figure 29. Output Spectra**

The example figure contains three vertically stacked log-magnitude spectra:

1. Modulating signal: baseband spectrum centred at normalized frequency `0`.
2. Carrier signal: narrow peaks at normalized frequencies approximately `-0.3` and `+0.3`.
3. Modulated signal: shifted message spectra centred around approximately `-0.3` and `+0.3`, each approximately half the linear magnitude of the baseband message spectrum, or `-3 dB` relative under the manual's `10*log10` convention.

## Dependency summary

Question 2 is explicitly a continuation of the setup and Question 1:

- The initial setup defines `bumps`, the time-based carrier, and the `am` workspace output.
- Question 1 defines the required graph function and its processing choices: orientation into columns, Hamming window, zero-padding by two powers of two, `fftshift`, normalized frequency `[-0.5,0.5)`, linear magnitude for `flag=0`, and `10*log10` magnitude for `flag=1`.
- Question 2 adds the carrier workspace output and must reuse `sigspec.m` within three separate subplot axes.
