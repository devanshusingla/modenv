# Modenv

🌐 Modular Python virtual environments using `.pth` files — reuse heavy packages across multiple nested projects while keeping full isolation.

---

## 📦 What is modenv?

`modenv` is a Python utility that lets you **chain virtual environments**, so a child `.venv` can reuse site-packages from:

- 🧠 a **parent virtual environment**
- 👤 the user's `~/.local` Python site-packages

This allows you to:

- Avoid redundant installations (e.g., `torch`, `transformers`)
- Save storage in disk-heavy AI projects
- Keep clean, isolated environments for each project
- Override stacked packages with per-project installs if needed

---

## 🚀 Installation

Clone and install using `pip` in editable mode:

```bash
git clone https://github.com/devanshusingla/modenv.git
cd modenv
pip install -e .
```

## ⚙️ Usage

### Step 1: Create a virtual environment

```bash
python -m venv .venv\
```

### Step 2: Stack packages into it

```bash
modenv stack .venv
```

## 🙏 Acknowledgments
Thanks ChatGPT for helping out with this.

