

# 🚀 Multi-Functional QR Code Generator Using Python

<p align="center">
  <b>A Python-based QR Code Generator that creates customized QR codes for text, URLs, contact cards, Wi-Fi credentials, and image data.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Library-qrcode-orange" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-green" />
  <img src="https://img.shields.io/badge/Image-Pillow-yellow" />
  <img src="https://img.shields.io/badge/Status-Development-success" />
</p>

---

## 📌 Project Overview

The **Multi-Functional QR Code Generator** is a Python application designed to generate QR codes for different types of information through a simple menu-driven interface.

Instead of manually creating QR codes using online websites, users can generate them directly from their computers.

The application supports multiple QR code formats, including:

- Text and website URLs.
- Contact information using vCard format.
- Wi-Fi network credentials.
- Image data encoded into QR codes.

It also provides a graphical file selection window using Tkinter, allowing users to select images directly from their computer.

## ✨ Key Features

### 1. 🔗 Text and URL QR Code Generator
- Generate QR codes for any text or website URL.
- Accepts user input dynamically.
- Allows users to specify the output filename.
- Saves the generated QR code as a PNG image.
- Opens the generated QR code automatically.

### 2. 👤 Contact Card QR Code Generator
- Collects personal contact information.
- Supports first name and last name.
- Accepts phone numbers and email addresses.
- Generates contact information in vCard format.
- Allows QR scanners and compatible contact applications to recognize contact details.

### 3. 📶 Wi-Fi QR Code Generator
- Accepts Wi-Fi network name (SSID).
- Accepts Wi-Fi password.
- Generates QR codes using the standard Wi-Fi QR format.
- Allows compatible smartphones to scan the QR code and connect to the network.

### 4. 🖼️ Image QR Code Generator
- Opens the computer's file explorer using Tkinter.
- Allows users to select PNG, JPG, and JPEG images.
- Reads image files in binary mode.
- Converts binary image data into Base64 encoding.
- Generates a QR code containing the encoded image data.
- Includes a size validation check before QR generation.

**Note:** The current implementation supports only small images that fit within a single QR code's capacity. It does not upload images to cloud storage or automatically reconstruct images from scanned QR codes.

### 5. ⚠️ Input Validation
- Uses Python's `try-except` mechanism.
- Handles invalid numeric menu inputs.
- Prevents the program from terminating immediately when a non-numeric menu choice is entered.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| qrcode | QR code generation |
| Tkinter | Graphical file selection |
| Pillow (PIL) | Image processing |
| Base64 | Binary-to-text image encoding |
| Exception Handling | Input validation and error handling |
| Match-Case | Menu-based program control |

## 📂 Project Structure

```text
QR-Code-Generator/
│
├── qr_generator.py
│
├── generated_qr_codes/
│   ├── website_qr.png
│   ├── contact_qr.png
│   ├── wifi_qr.png
│   └── image_qr.png
│
├── README.md
│
└── requirements.txt
```

*Note: The generated QR code filenames depend on the options and filenames entered by the user.*

---

## ⚙️ Installation and Setup

### Step 1: Install Python

Download and install Python 3.10 or later.

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/nameisnarayana7/Qr_Generator.git
```

Navigate to the project directory:

```bash
cd QR-Code-Generator
```

### Step 3: Install Required Libraries

Install the dependencies:

```bash
pip install qrcode[pil]
```

Alternatively:

```bash
pip install qrcode pillow
```

**Tkinter:** Usually included with standard Python installations on Windows.

### Step 4: Run the Application

```bash
python qr_generator.py
```

---

## 💻 Application Menu

When the application starts, users will see the following menu:

```text
================================
       QR CODE GENERATOR
================================

1. Link or Text
2. Contact Card
3. WiFi Password
4. Image
5. Exit

Choose Format:
```

Users can select an option by entering its corresponding number.

---

## 📖 Detailed Usage Guide

### Option 1: Link or Text

**Input:**

```text
Choose Format: 1

Enter your Link or text:
https://www.google.com

File Name:
google
```

**Output:**

```text
google_qr.png
```

Scanning the generated QR code opens the provided URL or displays the encoded text.

### Option 2: Contact Card

**Input:**

```text
Choose Format: 2

Enter firstname: Narayana
Enter Lastname: Kondeti
Enter Phone No: 9876543210
Enter Email: narayana@gmail.com
```

**Generated vCard data:**

```text
BEGIN:VCARD
VERSION:3.0
N:Kondeti;Narayana
FN:Narayana Kondeti
TEL:9876543210
EMAIL:narayana@gmail.com
END:VCARD
```

**Output:**

```text
Narayana_qr.png
```

Compatible QR scanners can recognize the information as a contact card.

### Option 3: Wi-Fi Password

**Input:**

```text
Choose Format: 3

Enter wifi name: MyHomeWiFi
Enter Password: 12345678
```

**Generated Wi-Fi QR data:**

```text
WIFI:T:WPA;S:MyHomeWiFi;P:12345678;;
```

**Output:**

```text
MyHomeWiFi_qr.png
```

Scanning with a compatible smartphone allows the user to join the Wi-Fi network.

### Option 4: Image QR Code

**Input:**

```text
Choose Format: 4
```

A graphical file selection window opens.

1. Select an image from the computer.
2. The program reads the selected image in binary format.
3. Binary data is encoded using Base64.
4. The encoded data is checked against the configured size limit.
5. If the image fits, a QR code is generated.

**Output:**

```text
Image data QR generated!
```

**Important:** The current implementation only supports images small enough to fit in one QR code. A standard QR code has limited storage capacity. Base64 also increases the size of the original data by approximately 33%.

---

## 🧠 Concepts Demonstrated

This project demonstrates several important Python programming concepts.

**1. Functions and Libraries**

Using external Python libraries to perform specialized operations.

**2. File Handling**

Reading image files in binary mode using:

```python
with open(path, "rb") as f:
    image_data = f.read()
```

**3. Base64 Encoding**

Converting binary image data into a text representation:

```python
encoded_data = base64.b64encode(image_data).decode()
```

**4. Match-Case Statements**

Implementing menu-driven functionality using Python's structural pattern matching.

**5. Exception Handling**

Using `try-except` to handle invalid input and prevent unexpected program termination.

**6. GUI File Selection**

Using Tkinter's `filedialog.askopenfilename()` to allow users to browse and select files.

---

## ⚠️ Current Limitations

- Large images cannot fit inside a single QR code.
- Image QR codes store encoded data, not an online image link.
- Scanning Base64 image data with Google Lens does not automatically display the original image.
- Wi-Fi and contact QR codes require compatible scanner applications.
- The current application does not include a QR code decoder.
- Special characters in Wi-Fi credentials and contact information may require escaping.

---

## 🚀 Future Enhancements

The following features can be added in future versions:

- [ ] Support for large images using multiple QR codes.
- [ ] QR code scanning and image reconstruction.
- [ ] Cloud image upload and shareable QR links.
- [ ] Custom QR code colors and designs.
- [ ] Add logos and profile pictures to QR codes.
- [ ] Generate QR codes for PDF documents.
- [ ] Add a graphical user interface using Tkinter.
- [ ] Support multiple QR code output formats.
- [ ] Add QR code history and management.
- [ ] Add error handling for invalid file formats.

---

## 🔐 Security Considerations

- Wi-Fi QR codes contain network credentials. Avoid sharing them publicly.
- Contact QR codes may contain personal information.
- Image data encoded into QR codes can be accessed by anyone who scans them.
- Avoid embedding passwords or confidential information in publicly shared QR codes.
- Validate user inputs and selected file types before processing.

---

## 🎯 Learning Outcomes

By developing this project, you can gain practical experience with:

- Python programming and control flow.
- QR code generation and data encoding.
- Binary file handling.
- Image processing.
- GUI-based file selection.
- Exception handling.
- Python package installation and integration.
- Real-world problem-solving.

---

## 👨‍💻 Author

**Kondeti Lakshmi Narayana Murthy**

Python Developer | Machine Learning Enthusiast | Data Science Graduate

- GitHub: https://github.com/nameisnarayana7
- Portfolio: https://nameisnarayana7.github.io/portfolio_CV/

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ Star on GitHub.

Contributions, suggestions, and improvements are welcome!

**Built with Python ❤️**
