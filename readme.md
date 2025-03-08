# MkDocs Project - Documentation Guide

## 📌 Project Overview
This project contains documentation generated with **MkDocs**. It includes a local development server, a build system, and diagram generation using **Diagrams**.

---

## ⚡ Installation & Dependencies

### 🔹 Python Requirement
Ensure you have **Python >= 3.8** installed.

### 🔹 Virtual Environment (Recommended)
It is recommended to use a virtual environment to manage dependencies:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 🔹 Install Dependencies
After activating the virtual environment, install the required dependencies:
```sh
pip install -r requirements.txt
```
Make sure you have **MkDocs** installed, as well as **Graphviz** if you plan to generate diagrams.

---

## 🛠 Running the Development Server

To preview the documentation locally:
```sh
mkdocs serve
```
The documentation will be available at **http://127.0.0.1:8000**.

---

## 🔨 Building the Documentation
To generate a static site:
```sh
mkdocs build
```
This will create a `site/` folder containing the final static HTML files.

---

## 📊 Generating Diagrams
Diagrams are located in the `diagrams/` folder and generated using **Python Diagrams**.

### 🔹 Option 1: Running with Python (Requires Graphviz Installed)
```sh
python diagrams/your_diagram.py
```
If Graphviz is properly installed, this will generate a `.png` diagram in the output directory.

### 🔹 Option 2: Running with Docker (If Graphviz Issues)
If Graphviz is missing or causing issues, you can use Docker to generate diagrams:

#### 🔹 **On Linux/macOS**
```sh
cat diagrams/your_diagram.py | sudo docker run -i --rm -v $(pwd)/out:/out gtramontina/diagrams:0.23.4
```

#### 🔹 **On Windows (PowerShell)**
```powershell
Get-Content diagrams\your_diagram.py | docker run -i --rm -v ${PWD}/out:/out gtramontina/diagrams:0.23.4
```

#### 🔹 **On Windows (cmd)**
```cmd
type diagrams\your_diagram.py | docker run -i --rm -v %CD%\out:/out gtramontina/diagrams:0.23.4
```

This will generate the diagram in the `out/` directory.

---

## 🏗 Running MkDocs in a Docker Container
Instead of deploying manually, you can build and run MkDocs using Docker:

### 🔹 Build the Docker Image
```sh
sudo docker build -t mkdocs_build .
```

### 🔹 Run the MkDocs Container
```sh
sudo docker run -p 8000:80 mkdocs_build
```
This will serve the documentation inside a container.

---

## 📌 Folder Structure
```
mkdocs_project/
│── diagrams/       # Python scripts for generating architecture diagrams
│── docs/           # Markdown documentation files
│── site/           # Built static site (after running `mkdocs build`)
│── .gitignore      # Ignoring unnecessary files
│── Dockerfile      # Containerization for serving documentation with Nginx
│── mkdocs.yml      # MkDocs configuration file
│── requirements.txt # Python dependencies
```

An example of the docs is running in :
https://featversedocs-production.up.railway.app

🚀 **Now you're ready to build and serve your documentation!**