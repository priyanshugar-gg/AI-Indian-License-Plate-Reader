🚗 AI Indian License Plate Reader
A Streamlit-powered application that leverages PaddleOCR to accurately detect and extract Indian license plate numbers from uploaded images. This tool is designed for simplicity and efficiency, providing a quick way to get license plate information.

✨ Features
Intuitive User Interface: Built with Streamlit for a clean and easy-to-use experience.

Multiple Image Uploads: Process one or many images simultaneously.

Real-time OCR Processing: Get instant results for license plate detection.

Contour Visualization: See the detected contours on the license plates, helping understand the OCR process.

Confidence Scores: View the confidence level for each detected text box.

Best Match Suggestion: The application highlights the most probable license plate text.

Supports Common Image Formats: Compatible with JPG, JPEG, and PNG image files.

🚀 Getting Started
Follow these steps to get your own Indian License Plate Reader up and running!

Prerequisites
Before you begin, ensure you have Python 3.8+ installed on your system.

Installation
Clone the repository (or download the code):

git clone https://github.com/priyanshugar-gg/AI-Indian-License-Plate-Reader
cd AI-Indian-License-Plate-Reader


Create a virtual environment (recommended):

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt


streamlit
opencv-python-headless
numpy
paddleocr
Pillow

Running the Application
Once the dependencies are installed, you can run the Streamlit application:

streamlit run app.py


This command will open the application in your default web browser.

💡 Usage
Launch the application as described in the "Running the Application" section.

Click on the "Choose an images..." button to upload one or more image files (JPG, JPEG, or PNG) containing Indian license plates.

The application will display the uploaded image and then an image with detected contours.

It will then run OCR processing and show all detected text boxes along with their confidence scores.

Finally, it will suggest the "Possible License Plate Text" which is the most confident detection.

🛠️ Technologies Used
Python: The core programming language.

Streamlit: For building the interactive web application.

PaddleOCR: A powerful OCR library for text detection and recognition.

OpenCV (cv2): For image preprocessing and contour detection.

NumPy: For numerical operations, especially with image arrays.

Pillow (PIL): For image manipulation.

🔮 Future Enhancements
License Plate Validation: Implement logic to validate detected license plate formats (e.g., checking for state codes, series, numbers).

Batch Processing: Allow users to upload a zip file of images and download results in a CSV.

Improved Preprocessing: Explore more advanced image preprocessing techniques for better OCR accuracy in varied lighting conditions.

Localization: Add support for other languages or specific regional plate formats.

History Feature: Store previously processed images and results.

Webcam Integration: Allow direct image capture from a webcam.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
(You'll need to create a LICENSE file in your repository if you don't have one)

📞 Contact
If you have any questions, suggestions, or just want to connect:

priyanshugar-gg

GitHub Profile: (https://github.com/priyanshugar-gg)

Email: priyanshug879@gmail.com

Enjoy using the AI Indian License Plate Reader!