# neoguard
TinyML-based wearable for early detection of neonatal choking during feeding. Fuses I2S audio + IMU on ESP32-S3 with on-device inference (&lt;50ms latency, &lt;100KB model). Aims to detect choking 10–25s earlier than pulse oximetry (literature-based). Research prototype — not a medical device. By an 18-year-old developer.
# 🍼 NeoGuard           
### TinyML-Based Wearable for Early Neonatal Choking Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: ESP32-S3](https://img.shields.io/badge/Platform-ESP32--S3-blue)](https://www.espressif.com/)
[![Framework: TensorFlow Lite Micro](https://img.shields.io/badge/Framework-TFLite--Micro-orange)](https://www.tensorflow.org/lite/microcontrollers)
[![Status: Proof of Concept](https://img.shields.io/badge/Status-Proof%20of%20Concept-red)]()
[![Developer Age: 18](https://img.shields.io/badge/Developer%20Age-18-brightgreen)]()
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)]()

> An open-source, low-cost (<$30) wearable system for **early detection of neonatal choking and aspiration during feeding**, using I2S digital audio, IMU sensor fusion, and on-device TinyML inference on ESP32-S3.

**A research prototype by an 18-year-old developer seeking full scholarship opportunities in Edge AI / Biomedical Engineering.**

---

## 📖 Table of Contents

- [The Problem](#-the-problem)
- [The Solution](#-the-solution)
- [Why Earlier Detection Matters](#️-why-earlier-detection-matters)
- [System Architecture](#️-system-architecture)
- [Hardware](#-hardware)
- [Signal Processing Pipeline](#-signal-processing-pipeline)
- [Machine Learning](#-machine-learning)
- [Comparison with Standard Monitoring](#-comparison-with-standard-monitoring)
- [Results](#-results)
- [Quick Start](#-quick-start)
- [Roadmap](#️-roadmap)
- [Limitations & Safety](#️-limitations--safety)
- [About the Developer](#-about-the-developer)
- [Why I Am Seeking a Scholarship](#-why-i-am-seeking-a-scholarship)
- [Citation](#-citation)
- [License](#-license)
- [References](#-references)

---

## ❗ The Problem

Every year, thousands of neonates experience **silent choking** or **aspiration** during bottle or nursing feeding — often at night when caregivers are exhausted and unable to react in time.

Current monitoring solutions are:

- ❌ **Expensive** ($300–$500 medical devices)
- ❌ **Hospital-only** (not designed for home use)
- ❌ **Based on SpO2 alone** → **delayed detection** due to circulatory lag
- ❌ **Not designed** for the unique acoustic signature of infant feeding
- ❌ **Not accessible** to families in low- and middle-income regions

**The gap:** By the time a pulse oximeter alarms, the choking event has already been happening for **10–30 seconds**. In neonates, this window can mean the difference between a safe recovery and permanent neurological damage.

**Our goal:** A sub-$30 wearable that detects choking events **before** oxygen desaturation occurs — using the airway's own acoustic and kinematic signals.

---

## 💡 The Solution

NeoGuard attaches to the **bottle or breast shield** — **NOT** to the infant's body — and fuses three signal sources:

- 🎤 **I2S digital microphone (INMP441)** → acoustic signature of swallow / stridor / choke
- 📐 **3-axis accelerometer (LIS3DH)** → sucking rhythm and head motion
- 🧠 **TinyML model on ESP32-S3** → real-time classification on-device
- 📱 **BLE / Wi-Fi alert** → immediate notification to caregiver

**Safety by design:**
- ✅ No sensors on the infant's skin
- ✅ No adhesives
- ✅ No neck bands
- ✅ No wires near the face

---

## ⏱️ Why Earlier Detection Matters

Pulse oximetry — the current clinical standard — has a well-documented **circulatory delay of 10–30 seconds** between the onset of a choking event and the drop in SpO2 *(Severinghaus 2002, Nitzan 2014)*.

This delay exists because the sensor measures oxygen saturation in **peripheral blood**, not at the **airway** where the event begins.

NeoGuard takes a **fundamentally different approach**: it detects the **acoustic and kinematic signature** of choking at the **airway level** — *before* oxygen desaturation occurs.

**Expected advantage:** 10–25 seconds earlier alarm compared to foot-worn pulse oximetry *(literature-based estimate, pending clinical validation)*. 

### Timeline of a choking event📧 
### Seyed Mohammad Amin Rahmani from Iran☫  
