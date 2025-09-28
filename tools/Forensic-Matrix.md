# Tool Matrix Scroll — Open‑Source Listening & Forensic Kit {#top}

VaultMesh • Blackout LUX

Single‑file • Search & filter • Printable • Local progress

## Overview

Tags: lawful, research, regulated, network, radio, mobile, osint, malware, defense, hashing

Sections
- [Network Capture & Analysis](#network-capture--analysis)
- [Radio / IMSI Research](#radio--imsi-research)
- [Mobile Forensics](#mobile-forensics)
- [OSINT & Metadata](#osint--metadata)
- [Malware / Memory](#malware--memory)
- [Defensive & Awareness](#defensive--awareness)
- [Hashing & Chain of Custody](#hashing--chain-of-custody)
- [Quick Hash & Chain‑of‑Custody Snippets](#quick-hash--chain-of-custody-snippets)
- [Ethics & Boundaries](#ethics--boundaries)

Badges: Lawful defensive use • Research‑only / lab • Heavily regulated context • All

---

## Network Capture & Analysis {#network-capture--analysis}

### Wireshark (lawful)
Category: Network Capture & Analysis
Purpose: Deep packet analysis; decode hundreds of protocols for lab captures.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install wireshark

# macOS
brew install --cask wireshark

# Fedora
sudo dnf install wireshark

# Arch
sudo pacman -S wireshark-qt
```

Run captures in lab or with explicit consent. Use span/mirror ports for clean traffic.

### tcpdump (lawful)
Category: Network Capture & Analysis
Purpose: CLI packet capture; ideal for quick PCAPs with chain-of-custody.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install tcpdump

# macOS
brew install tcpdump

# Fedora
sudo dnf install tcpdump

# Arch
sudo pacman -S tcpdump
```

Capture and hash .pcap files immediately after acquisition.

### tshark (lawful)
Category: Network Capture & Analysis
Purpose: Wireshark’s CLI; scriptable filtering and extraction.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install tshark

# macOS
brew install wireshark

# Fedora
sudo dnf install wireshark-cli

# Arch
sudo pacman -S wireshark-cli
```

Great for batch processing large PCAPs.

### mitmproxy (research)
Category: Network Capture & Analysis
Purpose: Interactive HTTPS proxy for lawful testing with trusted cert.
Install & Notes:

```
# Ubuntu/Debian
pipx install mitmproxy

# macOS
brew install mitmproxy

# Fedora
pipx install mitmproxy

# Arch
pipx install mitmproxy
```

Use only in lab or with explicit consent; client must install proxy CA cert.

### Kismet (research)
Category: Network Capture & Analysis
Purpose: Wireless sniffer for Wi‑Fi/Bluetooth/other radios.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install kismet

# macOS
brew install kismet

# Fedora
sudo dnf install kismet

# Arch
sudo pacman -S kismet
```

Requires compatible wireless adapters and monitor mode.

---

## Radio / IMSI Research {#radio--imsi-research}

### srsRAN (srsLTE) (research)
Category: Radio / IMSI Research
Purpose: Open LTE/5G stack for SDR research (eNodeB/UE in lab).
Install & Notes:

```
# Ubuntu/Debian
sudo apt install srsran

# macOS
brew install srsran

# Fedora
sudo dnf install srsran

# Arch
sudo pacman -S srsran
```

For lab spectrum research with SDR (USRP/BladeRF). Respect licensing/regulatory limits.

### gr-gsm (research)
Category: Radio / IMSI Research
Purpose: GNU Radio blocks for GSM signal analysis with SDR.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install gr-gsm

# macOS
brew install gnuradio gr-gsm

# Fedora
sudo dnf install gr-gsm

# Arch
sudo pacman -S gr-gsm
```

Research only; requires SDR and lawful RF use.

### GNU Radio (research)
Category: Radio / IMSI Research
Purpose: DSP toolkit for building radio pipelines; base for gr-* stacks.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install gnuradio

# macOS
brew install gnuradio

# Fedora
sudo dnf install gnuradio

# Arch
sudo pacman -S gnuradio
```

Foundation for SDR experiments; steep learning curve.

### SnoopSnitch (Android) (lawful)
Category: Radio / IMSI Research
Purpose: Detects fake base stations, silent SMS, and network attacks (root recommended).
Install & Notes: Install from F-Droid/APK. Works best on Qualcomm devices with root.

---

## Mobile Forensics {#mobile-forensics}

### ALEAPP / ILEAPP (lawful)
Category: Mobile Forensics
Purpose: Parse Android/iOS artifacts from backups or extractions.
Install & Notes:

```
# Ubuntu/Debian
pipx install aleapp ileapp

# macOS
pipx install aleapp ileapp

# Fedora
pipx install aleapp ileapp

# Arch
pipx install aleapp ileapp
```

Run against logical backups; produces HTML reports of artifacts.

### Autopsy (Sleuth Kit) (lawful)
Category: Mobile Forensics
Purpose: General forensic suite; modules for mobile artifacts.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install autopsy sleuthkit

# macOS
brew install sleuthkit && brew install --cask autopsy || true

# Fedora
sudo dnf install sleuthkit autopsy

# Arch
sudo pacman -S sleuthkit
```

Java GUI; good for case management and timelines.

### libimobiledevice (lawful)
Category: Mobile Forensics
Purpose: Interact with iOS devices on Linux/macOS; backups, syslog/sysdiagnose.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install libimobiledevice6 libimobiledevice-utils ifuse

# macOS
brew install libimobiledevice ifuse

# Fedora
sudo dnf install libimobiledevice ifuse

# Arch
sudo pacman -S libimobiledevice ifuse
```

For consent-based iOS backup/collection; pair device first.

### Android Backup Extractor (abe) (lawful)
Category: Mobile Forensics
Purpose: .ab to tar conversion/decryption for Android backups.
Install & Notes:

```
# Ubuntu/Debian
git clone https://github.com/nelenkov/android-backup-extractor.git

# macOS
brew install openjdk && git clone repo

# Fedora
dnf install java && git clone repo

# Arch
pacman -S jdk-openjdk && git clone repo
```

Use on backups obtained with consent; handle keys carefully.

### AFLogical OSE (lawful)
Category: Mobile Forensics
Purpose: Android logical acquisition (older but useful).
Install & Notes:

```
# Ubuntu/Debian
git clone https://github.com/nowsecure/aflogical

# macOS
brew install android-platform-tools

# Fedora
sudo dnf install android-tools

# Arch
sudo pacman -S android-tools
```

Good for legacy devices; prefer modern exports where possible.

---

## OSINT & Metadata {#osint--metadata}

### SpiderFoot OSS (lawful)
Category: OSINT & Metadata
Purpose: Automated OSINT (domains, IPs, breaches).
Install & Notes:

```
# Ubuntu/Debian
pipx install spiderfoot

# macOS
brew install spiderfoot

# Fedora
pipx install spiderfoot

# Arch
pipx install spiderfoot
```

Run locally; disable modules you don’t need to avoid over-collection.

### Maltego CE (lawful)
Category: OSINT & Metadata
Purpose: Graph OSINT data relationships (community edition).
Install & Notes: Download CE packages or install via brew cask; respect privacy laws.

### ExifTool (lawful)
Category: OSINT & Metadata
Purpose: Extract EXIF/metadata from images and documents.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install libimage-exiftool-perl

# macOS
brew install exiftool

# Fedora
sudo dnf install perl-Image-ExifTool

# Arch
sudo pacman -S exiftool
```

Great for validating media in evidence sets.

---

## Malware / Memory {#malware--memory}

### Volatility 3 (lawful)
Category: Malware / Memory
Purpose: Memory forensics framework for RAM images.
Install & Notes:

```
# Ubuntu/Debian
pipx install volatility3

# macOS
brew install volatility3

# Fedora
pipx install volatility3

# Arch
pipx install volatility3
```

Best with well-documented acquisition method.

### YARA (lawful)
Category: Malware / Memory
Purpose: Pattern-based scanner for malware/spyware indicators.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install yara

# macOS
brew install yara

# Fedora
sudo dnf install yara

# Arch
sudo pacman -S yara
```

Maintain your own ruleset for mobile IOCs.

### MobSF (lawful)
Category: Malware / Memory
Purpose: Mobile Security Framework for APK/IPA static & dynamic analysis.
Install & Notes:

```
# Ubuntu/Debian
docker run -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest

# macOS
brew install --cask docker

# Fedora
podman run -p 8000:8000 docker.io/opensecurity/mobile-security-framework-mobsf

# Arch
podman run -p 8000:8000 docker.io/opensecurity/mobile-security-framework-mobsf
```

Run sandboxed; never analyze live client data on the internet.

---

## Defensive & Awareness {#defensive--awareness}

### Haven (Android) (lawful)
Category: Defensive & Awareness
Purpose: Turns an old Android into a local sensor node (motion, mic, logs).
Install & Notes: Install from F-Droid/APK.

### Cuckoo Sandbox (research)
Category: Defensive & Awareness
Purpose: Automated malware analysis sandbox (VM-based).
Install & Notes: See official docs; isolate from production networks.

---

## Hashing & Chain of Custody {#hashing--chain-of-custody}

### hashdeep (lawful)
Category: Hashing & Chain of Custody
Purpose: Recursive hashing and audit verification.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install hashdeep

# macOS
brew install hashdeep

# Fedora
sudo dnf install hashdeep

# Arch
sudo pacman -S hashdeep
```

Use for manifest generation and later verification.

### OpenSSL (dgst) (lawful)
Category: Hashing & Chain of Custody
Purpose: General hashing for evidence manifests.
Install & Notes:

```
# Ubuntu/Debian
sudo apt install openssl

# macOS
brew install openssl

# Fedora
sudo dnf install openssl

# Arch
sudo pacman -S openssl

openssl dgst -sha256 <file>
```

---

## Quick Hash & Chain‑of‑Custody Snippets {#quick-hash--chain-of-custody-snippets}

```
# Generate SHA‑256 for all evidence files
sha256sum *.pcap *.tar.gz *.zip > EVIDENCE.sha256

# macOS
shasum -a 256 *.dmg *.zip > EVIDENCE.sha256

# Append new hashes
sha256sum newfile >> EVIDENCE.sha256

# Minimal custody log (append only)
printf "%s | %s | %s | %s\n" "$(date -u +%F\ %T)" "From→To" "Action" "Location" >> CUSTODY.log
```

---

## Ethics & Boundaries {#ethics--boundaries}

Operate in lab/consent contexts. Respect export controls and dual‑use restrictions. Document tool versions and methods so your work survives scrutiny.

[Back to Top](#top)

---


— VaultMesh · Earth’s Civilization Ledger —
© Vault Sovereign · https://vaultmesh.example/

