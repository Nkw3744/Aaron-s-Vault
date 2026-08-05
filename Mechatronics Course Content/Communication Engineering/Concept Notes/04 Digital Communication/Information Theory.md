---
aliases:
  - ENEL700 Week 9
  - L9 Information Theory
lecture: 9
source: L9 Information Theory.pdf
---

# Information Theory

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Transmitters Receivers and Noise]] - Next: [[Coding and Multiplexing]]
>
> [[L9 Information Theory.pdf|Lecture slides]] - [[ENEL700 T9.pdf|Tutorial 9]] - [[ENEL700 T9A.pdf|Tutorial 9 answers]]

## Core idea

Information theory quantifies uncertainty, determines the minimum average description length of a source, and places an upper bound on reliable communication through a channel. Source coding removes unnecessary redundancy; channel coding deliberately adds structured redundancy to combat errors.

## Sources and redundancy

A discrete source produces symbols from a finite alphabet $\{x_1,x_2,\ldots,x_m\}$. A **discrete memoryless source (DMS)** produces each symbol independently according to fixed probabilities $p(x_i)$.

Natural language contains redundancy, which lets a reader infer missing or corrupted letters. A maximally compressed random-looking string contains little such redundancy, so an error may be impossible to recognise. Efficient communication therefore balances compression against the structured redundancy needed for reliability.

## Self-information

The information conveyed by observing symbol $x_i$ is:

$$
I(x_i)=-\log_2p(x_i)=\log_2\left(\frac{1}{p(x_i)}\right)\quad\text{bits}
$$

- A certain event, $p=1$, conveys $0$ bits.
- A less probable event conveys more information.
- Independent-event information adds because probabilities multiply and logarithms convert multiplication to addition.

### Example

If $p(x)=0.1$:

$$
I(x)=-\log_2(0.1)\approx3.32\ \text{bits}
$$

If $p(x)=0.4$:

$$
I(x)\approx1.32\ \text{bits}
$$

## Entropy

Source entropy is the expected self-information per symbol:

$$
H(X)=\sum_{i=1}^{m}p(x_i)I(x_i)
$$

$$
H(X)=-\sum_{i=1}^{m}p(x_i)\log_2p(x_i)\quad\text{bits/symbol}
$$

For $m$ equally likely symbols:

$$
H_{max}=\log_2m
$$

Entropy is low when outcomes are predictable and high when uncertainty is large. It is the theoretical lower bound on the average number of bits per source symbol for lossless coding over long sequences.

## Code length and efficiency

If symbol $x_i$ has a binary code word of length $n_i$, average code length is:

$$
\bar L=\sum_{i=1}^{m}p(x_i)n_i
$$

Code efficiency is:

$$
\eta=\frac{H(X)}{\bar L}
$$

and redundancy can be written as:

$$
r=1-\eta
$$

For any uniquely decodable binary code, $\bar L\geq H(X)$. A good code makes $\bar L$ close to $H(X)$.

## Code properties

- **Fixed-length code:** every symbol uses the same number of bits. It is simple to parse but may be inefficient for unequal probabilities.
- **Variable-length code:** common symbols can use short words and rare symbols longer words.
- **Prefix-free code:** no valid code word is the prefix of another. It can be decoded immediately from left to right.
- **Uniquely decodable code:** every encoded bit sequence has only one source-symbol interpretation.
- **Optimal code:** minimises average length for the stated source probabilities.

Every prefix-free code is uniquely decodable, although a uniquely decodable code need not be prefix-free.

## Source coding

Source coding or lossless compression removes source redundancy. Assigning shorter words to more probable symbols lowers average transmission time. Morse code illustrates the idea: common letters use shorter patterns.

Entropy-coding methods introduced in the lecture include Huffman coding, arithmetic coding, and Lempel-Ziv coding.

## Huffman coding

Huffman coding produces an optimal binary prefix code for a known symbol-probability distribution.

### Procedure

1. List symbols in decreasing probability.
2. Combine the two lowest probabilities.
3. Reinsert their sum into the ordered list.
4. Repeat until one root remains.
5. Label the two branches from every merge 0 and 1.
6. Read each code word from root to symbol.

The branch-label choices can be swapped without changing code lengths or efficiency.

### Verification

After constructing the tree:

1. Confirm no code word prefixes another.
2. Calculate $\bar L=\sum p_in_i$.
3. Calculate $H(X)$ and $\eta=H/\bar L$.
4. Check the probability sum is 1.

Huffman coding satisfies:

$$
H(X)\leq\bar L<H(X)+1
$$

for a binary source code applied symbol by symbol.

## Lempel-Ziv coding

Lempel-Ziv methods do not require the source probabilities to be known in advance. They build a dictionary of strings observed in the input and replace repeated strings with compact references.

The lecture's parsing approach is:

1. Initialise the dictionary with the empty string.
2. Find the longest input prefix $W$ already in the dictionary.
3. Take the following symbol $B$.
4. Output the pair `(index of W, B)`.
5. Add $W+B$ to the dictionary.
6. Continue with the remaining input.

This adapts to repeated patterns in the data and underlies important practical lossless-compression families.

## Noiseless channel capacity: Nyquist result

For an ideal noiseless channel of bandwidth $B$ carrying $M$ distinguishable signal levels:

$$
C=2B\log_2M\quad\text{bit/s}
$$

The $2B$ factor follows the maximum independent symbol rate for a band-limited noiseless channel; $\log_2M$ is the number of bits per symbol.

Increasing signal levels raises the noiseless capacity, but in a real noisy channel closer levels become harder to distinguish.

## Noisy channel capacity: Shannon-Hartley

For channel bandwidth $B$, average signal power $S$, and noise power $N$ in that bandwidth:

$$
C=B\log_2\left(1+\frac{S}{N}\right)\quad\text{bit/s}
$$

This is the theoretical maximum reliable data rate under the model. It does not specify a particular modulation or code. Instead, it says reliable communication can be approached with suitable coding when $R<C$, while arbitrarily low error probability is impossible for $R>C$.

### Useful implications

- More bandwidth increases capacity.
- More SNR increases capacity, but logarithmically.
- Doubling transmit power does not double capacity.
- A design may trade bandwidth against SNR.

### Worked example

For $B=3\ \text{kHz}$ and $S/N=30\ \text{dB}=1000$:

$$
C=3000\log_2(1001)\approx29.9\ \text{kbit/s}
$$

## Source coding versus channel coding

| Source coding | Channel coding |
| --- | --- |
| Removes statistical redundancy | Adds structured redundancy |
| Reduces average bit rate | Improves error detection/correction |
| Limited by entropy | Limited by channel capacity |
| Examples: Huffman, Lempel-Ziv | Examples: parity, block and convolutional codes |

## Quick recall

- $I(x)=-\log_2p(x)$.
- $H(X)=-\sum p_i\log_2p_i$.
- $\bar L=\sum p_in_i$ and $\eta=H/\bar L$.
- Huffman is optimal among symbol-by-symbol binary prefix codes for known probabilities.
- Nyquist: $C=2B\log_2M$ for a noiseless channel.
- Shannon-Hartley: $C=B\log_2(1+S/N)$ for a noisy channel.

## Practice prompts

1. Calculate self-information and entropy for a source alphabet.
2. Build a Huffman tree and calculate average length and efficiency.
3. Explain why a prefix-free code is immediately decodable.
4. Compare Huffman and Lempel-Ziv assumptions.
5. Calculate and interpret Nyquist and Shannon capacity limits.
