# Machine Code Optimizer

## Overview
Machine Code Optimizer is a Streamlit web application that utilizes language models to optimize machine code. This tool allows users to upload machine code files, specify a machine name, and receive optimized code as well as cycle time analysis.

## Features
- Upload machine code files in various formats.
- Specify the machine name for optimization.
- View optimized code and cycle time analysis results.
- Download the optimized code report.

## ScreenShots
![image](https://github.com/chinmay404/Machine-Code-Optimiser/assets/92822013/b8623e8c-9b81-4c22-a1ca-817651a5b3c1)

![image](https://github.com/chinmay404/Machine-Code-Optimiser/assets/92822013/ec95ec44-e29a-4399-a2bb-41e57007cf97)
![image](https://github.com/chinmay404/Machine-Code-Optimiser/assets/92822013/be4df808-d443-449f-a3bf-3f3a77cb7b10)
## Getting Started
To run the Machine Code Optimizer locally, follow these steps:

1. Clone the repository:

   ```sh
   https://github.com/chinmay404/Machine-Code-Optimiser.git

2. Install requirement:

   ```Terminal
   pip install -r requirement.txt

3. Add Gemini API key :
   ```Terminal
   Create .env file and write GOOGLE_API_KEY="YOUR API KEY"

4. Run App:

   ```Terminal
   streamlit run main.py
