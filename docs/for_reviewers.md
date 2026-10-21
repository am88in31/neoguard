# 📄 For Scholarship Reviewers

Thank you for taking the time to review this project. This document is a concise guide to help you evaluate NeoGuard's relevance to my scholarship application.

<br>
<hr>
<br>

## 🎯 Summary

- **Project:** NeoGuard — TinyML-Based Wearable for Early Neonatal Choking Detection
- **Developer:** Seyed Mohammad Amin Rahmani, 18 years old
- **Field:** Edge AI, Embedded Systems, Biomedical Engineering
- **Goal:** Pursue a fully-funded degree in Edge AI / Biomedical Engineering at a research institution.

<br>
<hr>
<br>

## 🔬 Why This Project Is Novel

Current neonatal monitoring relies on **pulse oximetry**, which has a well-documented **circulatory delay of 10–30 seconds** (Severinghaus 2002, Nitzan 2014).

NeoGuard takes a fundamentally different approach: it detects the **acoustic and kinematic signature** of choking at the **airway level** — before SpO2 drops.

**To our knowledge, this is one of the first attempts to combine:**
1. I2S digital audio (16 kHz) for swallow/stridor detection
2. IMU-based kinematic analysis for sucking rhythm
3. On-device TinyML inference on a sub-$30 device

<br>
<hr>
<br>

## 🛠️ Technical Depth

This project spans the full stack:

| Layer | Technology | Skills Demonstrated |
|-------|------------|---------------------|
| **Sensing** | INMP441 (I2S), LIS3DH (IMU) | Hardware, protocols |
| **Firmware** | ESP32-S3, C++, PlatformIO | Embedded programming |
| **Signal Processing** | FFT, MFCC, Butterworth | DSP, mathematics |
| **Machine Learning** | TensorFlow Lite Micro, 1D-CNN | TinyML, on-device AI |
| **Alerts** | BLE, Wi-Fi, Flask dashboard | IoT, web development |

### 🌐 Clinical Web Dashboard & Multilingual Support
The project includes a full-stack web application (Flask, Python, HTML/JS). It features a dynamic multilingual interface (English/Chinese) and utilizes a custom **Tabular ML model** to automatically populate a 10-column clinical report based on aggregated sensor data. To ensure clinical standard compliance, the system generates a standardized, printable **PDF medical report in English**, bridging the gap between home monitoring and hospital electronic health records (EHR).

<br>
<hr>
<br>

## 🛡️ Intellectual Property & Protected Assets

While the hardware schematics and high-level architecture of NeoGuard are open-source to foster academic collaboration, **the core signal processing algorithms, the trained TinyML model weights, and the specific inference logic are proprietary** and are being prepared for patent filing.

**For Scholarship Reviewers & Academic Researchers:** 
I am fully prepared to grant you access to the complete private repository, the full source code, and a live demonstration. This will be provided under a standard Non-Disclosure Agreement (NDA) to ensure mutual trust and academic integrity.

<br>
<hr>
<br>

## 📊 Expected Impact

| Metric | Current Standard (SpO2) | NeoGuard (Target) |
|--------|--------------------------|-------------------|
| **Detection delay** | 15–40 seconds | ~1 second |
| **Cost** | $300–$500 | <$30 |
| **Silent choke detection** | ❌ | ✅ |
| **Home usability** | Limited | Designed for home |

**Potential impact:** 10–25 seconds earlier detection — a window that can prevent permanent neurological damage in neonates.

<br>
<hr>
<br>

## 🎓 What I Am Seeking

- **Full scholarship** for undergraduate or integrated MSc/PhD
- **Research group** working on Edge AI, Embedded ML, or Biomedical Signal Processing
- **Mentorship** from professors who care about real-world impact
- **Fully-funded program** (tuition + living costs)

<br>
<hr>
<br>

## 📬 Contact

- **Email:** [am88in31@mail.ir](mailto:am88in31@mail.ir)
- **GitHub:** [github.com/am88in31](https://github.com/am88in31)

<br>

*I am happy to provide additional documentation, a live demo, or answer any questions. Thank you for your consideration.*
