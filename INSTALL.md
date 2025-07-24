# 🛠️ Development Environment Setup

This guide helps you set up a local development environment for the Dibhashi project.

---

## ✅ Requirements

- Python **3.11**
- [Poetry](https://python-poetry.org/) (for dependency management)
- `ffmpeg` (available in your system `PATH`)
- Node.js and `npm` (for compiling Tailwind CSS)

---

## ⚙️ Step-by-Step Installation

### 1. Install Poetry

If not already installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Ensure the Poetry binary is in your shell path:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

### 2. Set Python 3.11 for the Project

Ensure Python 3.11 is installed and configure Poetry to use it:

```bash
poetry env use python3.11
```

---

### 3. Use In-Project Virtual Environments

```bash
poetry config virtualenvs.in-project true
```

---

### 4. Install Dependencies

```bash
poetry install
```

---

### 5. Activate the Virtual Environment

```bash
poetry shell
```

---

## 🌐 Frontend Setup (Tailwind CSS)

### 6. Install TailwindCSS

```bash
npm install tailwindcss @tailwindcss/cli --save-dev
```

### 7. Compile TailwindCSS (with Watch Mode)

```bash
npx tailwindcss -i ./src/dibhashi/static/css/input.css -o ./src/dibhashi/static/dist/output.css --watch
```

---

## 🚀 Run the Application

```bash
poetry run my-script
```

Then open in your browser:

```
http://127.0.0.1:5002/
```

---

## 🧪 Notes

- Ensure `ffmpeg` is installed and in your system `PATH`:
  ```bash
  ffmpeg -version
  ```

---

Happy coding!
