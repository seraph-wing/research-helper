# research-helper
This small web application aims to help in literature review by taking in a corpus of research papers, and analysing the abstracts to generate tags, clusters, and a simple searchable corpus for review and simple recovery during the course of writing a thesis/paper/journal etc.

Research Corpus Analyzer and Search Engine

# Introduction

This project is a Streamlit-based application designed to analyze a corpus of research texts in PDF format. It not only allows for the in-depth analysis of the texts to extract meaningful insights but also generates a search engine for quick and efficient searching through the PDF documents. This tool is especially useful for researchers, scholars, and anyone looking to mine data or find information within a large collection of research papers.

# Features

- **PDF Upload**: Users can upload multiple PDF documents to the application for analysis.
- **Text Extraction:** The application extracts text from the uploaded PDFs for processing.
- **Analysis Tools:** Includes various tools for analyzing the text, such as frequency analysis, keyword extraction, and more.
- **Search Engine:** A built-in search engine allows users to query the uploaded documents for specific information.
- **User Interface:** A clean and intuitive UI built with Streamlit, making it easy for users of all levels to interact with the application.

# Requirements

- Python 3.10
- Streamlit
- PyPDF2 or pdfminer.six (for PDF processing)
- NLTK or any other NLP library (for text analysis)

# Installation

To get started with the Research Corpus Analyzer and Search Engine, follow these steps:

1. Clone this repository to your local machine.
```bash
git clone <repository-url>
```
2. Navigate to the cloned repository's directory.
```bash
cd <repository-name>
```
3. Install the required dependencies.
```bash
pip install -r requirements.txt
```
4. Run the Streamlit application.
```bash
streamlit run app/app.py
```
# Usage

After launching the application, follow the on-screen instructions to upload your PDF files and start analyzing your corpus. You can use the analysis tools to generate insights and use the search engine to find specific information within your documents.

# Contributing

Contributions to the Research Corpus Analyzer and Search Engine are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

# License

This project is licensed under the GNU License - see the LICENSE file for details.


