from setuptools import setup

setup(
    name="ai-tester",
    version="1.0.0",
    py_modules=["main", "scanner", "ai_engine", "runner"],
    install_requires=[
        "typer",
        "rich",
        "groq",
        "python-dotenv",
        "pytest",
        "pytest-asyncio",
    ],
    entry_points={"console_scripts": ["ai-tester=main:app"]},
)
