import typer, time
from pathlib import Path
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor
from scanner import ProjectScanner
from ai_engine import AIEngine
from runner import TestRunner

app = typer.Typer()
console = Console()


@app.command()
def start(target_path: str = typer.Argument(".", help="Project path")):
    abs_path = Path(target_path).resolve()
    console.print(f"[bold blue]🚀 Starting AI-Tester on: {abs_path}[/bold blue]")

    scanner = ProjectScanner(str(abs_path))
    files = scanner.get_target_files()
    ai = AIEngine()
    runner = TestRunner(ai, abs_path)

    with ThreadPoolExecutor(max_workers=2) as executor:
        for file in files:
            console.print(f"[cyan]Processing {file['name']}...[/cyan]")
            code = ai.generate_tests_for_file(file)
            executor.submit(runner.run_and_fix, file, code)

    console.print(
        "[bold green]✨ All tasks complete! Check 'tests_generated_by_ai' in your project.[/bold green]"
    )


if __name__ == "__main__":
    app()
