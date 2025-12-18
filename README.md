# AI-Based Web Log Anomaly Detector

## 📌 Overview
This project is a cybersecurity-focused AI system designed to detect anomalous and
suspicious behavior in web server logs. It analyzes request patterns and identifies
abnormal traffic that may indicate brute-force attacks, scanning activity, or misuse
of web resources.

The project simulates a real-world SOC (Security Operations Center) use case where
security analysts monitor logs to identify potential threats.

---

## 🎯 Problem Statement
Traditional rule-based log monitoring systems often fail to detect unknown or
unusual attack patterns. Attackers may behave differently than predefined rules.
This project addresses that gap by using Machine Learning to detect anomalies
based on behavior rather than static rules.

---

## 🛠️ Approach
1. Parsed Apache-style web access logs
2. Extracted meaningful features such as request frequency per IP address
3. Applied an unsupervised Machine Learning model (Isolation Forest)
4. Classified IP traffic as **Normal** or **Suspicious**
5. Generated an output report for further investigation

---

## 🔐 Technologies Used
- Python
- Pandas
- Scikit-learn
- Regular Expressions
- Ubuntu Linux

---

## 📊 Output
The system generates a CSV report identifying IP addresses with abnormal behavior.
Each IP is labeled as:
- **Normal**
- **Suspicious**

This output can be used by security analysts to prioritize incident investigation.

---

## 🚀 How to Run
```bash
python src/anomaly_detector.py
