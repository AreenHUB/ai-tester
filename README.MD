# 🤖 AI-Tester CLI

> **Autonomous AI-powered testing for Python projects — generate, run, and fix tests automatically.**

AI-Tester is a powerful CLI tool that leverages **Groq’s ultra-fast inference models** to automatically generate, execute, and intelligently fix unit tests for any Python codebase. It is designed to streamline testing workflows, reduce manual effort, and improve code reliability with minimal setup.

---

## ✨ Features

* 🔍 **Automated Code Discovery**
  Scans your project structure and intelligently identifies Python modules and functions using AST analysis.

* 🧠 **AI-Generated Test Suites**
  Automatically creates robust `pytest` test cases, including edge cases and exception handling.

* 🔁 **Self-Healing Auto-Fix Loop**
  Detects failing tests, analyzes root causes, and applies AI-driven fixes iteratively.

* ⚡ **High-Speed Execution**
  Powered by Groq’s low-latency inference and multi-threaded processing for rapid results.

* 🧩 **Zero-Setup Integration**
  No manual configuration required — handles imports, fixtures (`conftest.py`), and test structure automatically.

* 📂 **Isolated Test Environment**
  Generates tests in a dedicated directory to keep your project clean and organized.

---

## 🚀 Installation

```bash
git clone https://github.com/AreenHUB/ai-tester.git
cd ai-tester
pip install -r requirements.txt
```

---

## ⚙️ Configuration

1. Get your API key from: https://console.groq.com
2. Create a `.env` file in the project root:

```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

---

## 🛠️ Usage

Run the tool inside any Python project:

```bash
ai-tester .
```

Or specify a custom path:

```bash
ai-tester /path/to/your/python/project
```

---

## 📌 Example Output

```bash
✔ Scanning project structure...
✔ Generating test cases with AI...
✔ Running pytest...
✖ Some tests failed — applying fixes...
✔ Re-running tests...
✔ All tests passed ✅
```

---

## 📁 Project Structure

```
ai-tester/
│── scanner.py        # AST-based code analyzer
│── ai_engine.py      # Groq AI integration & retry logic
│── runner.py         # Pytest runner with auto-fix loop
│── main.py           # CLI entry point (Typer)
│── tests_generated_by_ai/  # Auto-generated test cases
```

---

## 🧠 How It Works

1. **Scan** → Analyzes your Python code using AST
2. **Generate** → Creates test cases using AI
3. **Execute** → Runs tests with pytest
4. **Fix** → Detects failures and applies AI fixes
5. **Repeat** → Iterates until tests pass

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Submit a pull request

Feel free to open issues for bugs, ideas, or feature requests.

---

## 📝 License

This project is licensed under the **MIT License**.
See the `LICENSE` file for more details.

---

## 🚀 Future Improvements

* Support for additional testing frameworks
* Smarter test coverage reporting
* Integration with CI/CD pipelines
* Plugin system for extensibility

---

## 💡 Why AI-Tester?

Testing is often time-consuming and repetitive. AI-Tester eliminates that burden by automating the entire process — from generation to validation — allowing developers to focus on building, not debugging.

---

**⭐ If you find this project useful, consider giving it a star on GitHub!**
