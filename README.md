# 🛡️ XSS-Obliterator

**XSS-Obliterator** is a Python-based automated scanner designed to detect **Cross-Site Scripting (XSS)** vulnerabilities in web applications.  
It performs intelligent payload injection, response analysis, and reflection detection to help security researchers and developers identify potential XSS attack vectors.

> ⚠️ **For educational and authorized security testing only.**  
> Do NOT scan websites without explicit permission.

---

## 🚀 Features

- 🔍 Automated XSS vulnerability scanning
- 🧠 Smart payload injection & reflection detection
- 🌐 Scans GET & POST parameters
- 📄 Supports URL parameter discovery
- ⚡ Fast and lightweight Python implementation
- 🧪 OWASP Juice Shop compatible (ideal for practice)

---

## 📂 Project Structure

xss-obliterator/
│
├── main.py # Entry point
├── payloads.txt # XSS payload list
├── scanner.py # Core scanning logic
├── utils.py # Helper utilities
├── requirements.txt # Python dependencies
└── README.md

yaml
Copy code

---

## 🛠️ Installation

### 1️⃣ Clone the repository
git clone https://github.com/yourusername/xss-obliterator.git
cd xss-obliterator

shell
Copy code

### 2️⃣ Install dependencies
pip install -r requirements.txt

yaml
Copy code

---

## ▶️ Usage

### Basic scan
```python main.py -u https://example.com

graphql
Copy code
```
### Scan a test target (OWASP Juice Shop)
```python main.py -u https://owasp.org/www-project-juice-shop/

yaml
Copy code
```
---

## ⚙️ Arguments

| Argument | Description |
|--------|-------------|
| `-u`   | Target URL to scan |
| `-p`   | Custom payload file (optional) |
| `-o`   | Output results to a file (optional) |

---
## Screenshots
<img width="1676" height="683" alt="image" src="https://github.com/user-attachments/assets/c432c0b4-36a8-453b-8428-b1199f374b07" />


---

## 🔐 Legal Disclaimer

This tool is intended **only for ethical hacking, learning, and authorized security assessments**.

By using XSS-Obliterator, you agree that:
- You have explicit permission to test the target
- You take full responsibility for your actions
- The author is not liable for misuse or damages

---

## 📚 Learning Resources

- OWASP XSS Guide: https://owasp.org/www-community/attacks/xss/
- OWASP Juice Shop: https://owasp.org/www-project-juice-shop/

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (`feature/xss-enhancement`)
3. Commit your changes
4. Open a Pull Request

---

## ⭐ Support

If you find this project useful:
- ⭐ Star the repository
- 🐛 Report issues
- 💡 Suggest features

---

## 🧑‍💻 Author

Built with ❤️ by **Prathyay**  
Security • Python • Offensive Tooling

---

## 📜 License

This project is licensed under the **There's no license** licence.
