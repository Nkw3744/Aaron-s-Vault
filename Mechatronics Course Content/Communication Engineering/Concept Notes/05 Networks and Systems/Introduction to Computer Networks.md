---
aliases:
  - ENEL700 Week 11
  - Introduction to Computer Network
lecture: 11
source: L11 Introduction to Computer Network.pdf
---

# Introduction to Computer Networks

> [!info] Course navigation
> [[Communication Engineering Overview|Subject overview]] - [[Communication Engineering Roadmap|Course roadmap]] - [[Communication Engineering Practice Index|Practice index]] - Previous: [[Coding and Multiplexing]] - Next: [[Modern Telecommunication Systems and Measurements]]
>
> [[L11 Introduction to Computer Network.pdf|Lecture slides]] - [[ENEL700 T11.pdf|Tutorial 11]]

## Core idea

Layered network models divide communication into manageable services. Each layer uses the layer below, provides a service to the layer above, and communicates logically with its peer on another host through a protocol.

## Why layers are useful

```text
application data
  -> transport segment/stream
    -> network packet
      -> data-link frame
        -> physical bits/signals
```

On transmission, each layer adds control information called **encapsulation**. The receiver removes it in reverse order. Layering allows a technology to change at one layer without redesigning the whole network, provided the service boundary remains consistent.

## OSI seven-layer model

| Layer | Name | Main function | Examples/concepts from the lecture |
| ---: | --- | --- | --- |
| 7 | Application | Network services visible to applications | HTTP, SMTP, FTP, remote login |
| 6 | Presentation | Data representation | Character formats, byte order, encryption, compression |
| 5 | Session | Persistent dialog and session control | Login, authentication, transaction/session management |
| 4 | Transport | Process-to-process delivery | Reliability, streams/datagrams, port addresses |
| 3 | Network | End-host delivery across multiple links | Packets, logical addressing, routing, IP |
| 2 | Data link | Delivery over one local link | Frames, MAC/physical addressing, media access |
| 1 | Physical | Signals and media | Cables, fibre, radio, bit representation and order |

### Addressing by layer

- Layer 2 address identifies an interface on a local link.
- Layer 3 address identifies a host/interface across interconnected networks.
- Layer 4 port identifies the destination process or service inside the host.

## TCP/IP model

The practical Internet model is commonly shown with five layers:

| TCP/IP layer | Main job | OSI mapping |
| --- | --- | --- |
| Application | Application/session-specific protocols | OSI 5-7 |
| Transport | Application-to-application delivery | OSI 4 |
| Internetwork | Addressing and routing between networks | OSI 3 |
| Link | Local-link framing and access | OSI 2 |
| Physical | Transmission media and signals | OSI 1 |

Some descriptions combine link and physical into one network-access layer, producing a four-layer model.

## Physical-layer media

- **Coaxial cable:** bulky but relatively resistant to noise.
- **Twisted pair:** light, inexpensive, and uses twisting to reject coupled noise.
- **Multimode fibre:** supports high rates over shorter fibre distances.
- **Single-mode fibre:** supports very high rates and long distances.
- **Radio, microwave, and satellite:** provide wireless links but require propagation, interference, and security considerations.

No physical medium is inherently secure; protection comes from access control, encryption, monitoring, and physical safeguards.

## Ethernet and data-link devices

Ethernet transports data in **frames** containing destination and source addresses, a type/length field, payload, and a frame-check sequence.

The lecture describes classic shared Ethernet's listen-before-transmit and collision behaviour, commonly associated with CSMA/CD. Modern full-duplex switched Ethernet does not experience collisions on each point-to-point link.

### Devices

- **Transceiver:** converts between host/interface signalling and the physical medium.
- **Repeater:** regenerates signals between physical segments; it does not inspect frame addresses.
- **Hub:** a multiport repeater; repeats incoming traffic to other ports.
- **Bridge:** forwards or filters frames between segments based on data-link addresses.
- **Switch:** a hardware multiport bridge; gives each port an independent segment.
- **Wireless access point:** bridges wireless and wired segments; wireless clients share radio airtime.

## Internetwork layer and IPv4

Layer 3 connects separate layer-2 networks, even when they use different technologies or speeds. An IPv4 packet contains a header and payload. Important header concepts include source and destination addresses, protocol identifier, total length, time to live (TTL), fragmentation fields, and header checksum.

An IPv4 address is 32 bits, normally written as four decimal octets. It contains a network portion and a host portion, with the boundary defined by a subnet mask.

## Subnet masks and CIDR

A subnet mask has contiguous 1 bits for the network prefix followed by 0 bits for host positions. CIDR slash notation states the number of prefix bits:

| Prefix | Mask | Addresses per subnet |
| ---: | --- | ---: |
| /24 | 255.255.255.0 | $2^8=256$ |
| /28 | 255.255.255.240 | $2^4=16$ |

The network address is the bitwise AND of the IP address and mask:

$$
\text{network}=\text{IP}\ \text{AND}\ \text{mask}
$$

### Worked example: /28

For `172.156.62.23/28`:

- Mask: `255.255.255.240`.
- Block size in final octet: $256-240=16$.
- Subnet ranges begin at 0, 16, 32, ...
- 23 lies in 16-31.
- Network address: `172.156.62.16`.
- Broadcast address: `172.156.62.31`.
- Conventional usable host range: `172.156.62.17`-`172.156.62.30`.

For `172.24.57.18/24`, the network address is `172.24.57.0`.

## Transport and application layers

The lecture focuses on TCP:

- Connection-oriented.
- Reliable byte stream.
- Delivers data in order and suppresses duplicates.
- Establishes a connection with a three-way handshake.

Traditional application protocols listed include Telnet and SSH for remote access, FTP/SCP for file transfer, SMTP for email, and HTTP for the web. Their transport ports identify which receiving process should handle the data.

## End-to-end packet path

```text
application -> TCP data and ports -> IP packet and addresses
-> Ethernet/Wi-Fi frame and local addresses -> physical signal
-> switches forward frames locally -> routers forward IP packets between networks
-> destination decapsulates upward
```

At each routed hop, the layer-2 frame can change, while the IP packet continues toward its destination subject to routing and header updates such as TTL.

## Quick recall

- Layers provide services upward and use services downward.
- Frames are layer 2, packets are layer 3, and ports belong to layer 4.
- A hub repeats; a switch selectively forwards frames; a router connects IP networks.
- Network address = IP AND mask.
- `/n` gives the number of network-prefix bits.
- TCP provides a reliable ordered byte stream between applications.

## Practice prompts

1. Map an HTTP message through the TCP/IP and OSI layers.
2. Compare repeater, hub, bridge, switch, access point, and router.
3. Identify layer-2, layer-3, and layer-4 addresses in a packet exchange.
4. Calculate network, broadcast, and host ranges for a CIDR address.
5. Explain which headers change when a packet crosses a router.
