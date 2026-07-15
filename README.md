# 📄 Image Text Extraction and Translation

A Streamlit-based OCR application that extracts text from images using **Tesseract OCR** and translates it into multiple languages using **Google Translate**.

The application provides an intuitive web interface where users can upload an image, extract textual content, and instantly translate it into their preferred language.

---

## ✨ Features

- 📷 Upload JPG, JPEG and PNG images
- 🔍 OCR-based text extraction using Tesseract
- 🌐 Multi-language translation
- 🎯 Simple and interactive Streamlit interface
- ⚡ Fast processing
- 💻 Cross-platform support

---

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenCV
- Tesseract OCR
- Google Translate API (googletrans)

---

## 📂 Project Structure

```text
Image-Text-Extraction-and-Translation/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Image-Text-Extraction-and-Translation.git
```

Move to the project directory:

```bash
cd Image-Text-Extraction-and-Translation
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## Install Tesseract OCR

### Windows

1. Download Tesseract OCR.
2. Install it.
3. Add the installation directory to your system PATH.

Example:

```
C:\Program Files\Tesseract-OCR\
```

If Tesseract is not added to PATH, update the path inside `app.py`.

---

### Linux

```bash
sudo apt install tesseract-ocr
```

---

### macOS

```bash
brew install tesseract
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🌍 Supported Translation Languages

- English
- Hindi
- Tamil
- Telugu
- Malayalam

---

## 📌 Future Improvements

- Support PDF documents
- Real-time camera OCR
- Additional language support
- OCR confidence visualization
- Export translated text

---

## 👨‍💻 Author

**Harshit**

---

## 📄 License

This project is licensed under the MIT License.