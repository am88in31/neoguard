# 📄 For Scholarship Reviewers

Thank you for taking the time to review this project. This document is a concise guide to help you evaluate NeoGuard's relevance to my scholarship application.

---

## 🎯 Summary

**Project:** NeoGuard — TinyML-Based Wearable for Early Neonatal Choking Detection
**Developer:** Seyed Mohammad Amin Rahmani, 18 years old
**Field:** Edge AI, Embedded Systems, Biomedical Engineering
**Goal:** Pursue a fully-funded degree in Edge AI / Biomedical Engineering at a research institution.

---

## 🔬 Why This Project Is Novel

Current neonatal monitoring relies on **pulse oximetry**, which has a well-documented **circulatory delay of 10–30 seconds** (Severinghaus 2002, Nitzan 2014).

NeoGuard takes a different approach: it detects the **acoustic and kinematic signature** of choking at the **airway level** — before SpO2 drops.

**To our knowledge, this is one of the first attempts to combine:**
1. I2S digital audio (16 kHz) for swallow/stridor detection
2. IMU-based kinematic analysis for sucking rhythm
3. On-device TinyML inference on a sub-$30 device

---

## 🛠️ Technical Depth

This project spans the full stack:

| Layer | Technology | Skills Demonstrated |
|-------|------------|---------------------|
| Sensing | INMP441 (I2S), LIS3DH (IMU) | Hardware, protocols |
| Firmware | ESP32-S3, C++, PlatformIO | Embedded programming |
| Signal Processing | FFT, MFCC, Butterworth | DSP, mathematics |
| Machine Learning | TensorFlow Lite Micro, 1D-CNN | TinyML, on-device AI |
| Alerts | BLE, Wi-Fi, Flask dashboard | IoT, web development |

---

## 📊 Expected Impact

| Metric | Current Standard (SpO2) | NeoGuard (Target) |
|--------|--------------------------|-------------------|
| Detection delay | 15–40 seconds | ~1 second |
| Cost | $300–$500 | <$30 |
| Silent choke detection | ❌ | ✅ |
| Home usability | Limited | Designed for home |

**Potential impact:** 10–25 seconds earlier detection — a window that can prevent permanent neurological damage in neonates.

---

## 🎓 What I Am Seeking

- **Full scholarship** for undergraduate or integrated MSc/PhD
- **Research group** working on Edge AI, Embedded ML, or Biomedical Signal Processing
- **Mentorship** from professors who care about real-world impact
- **Fully-funded program** (tuition + living costs)

---

## 📬 Contact

- **Email:** [am88in31@mail.ir](mailto:am88in31@mail.ir)
- **GitHub:** [github.com/am88in31](https://github.com/am88in31)

---

*I am happy to provide additional documentation, a live demo, or answer any questions. Thank you for your consideration.*
