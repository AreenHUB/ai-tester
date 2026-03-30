# runner.py
import subprocess
from pathlib import Path
from ai_engine import AIEngine
from rich.console import Console

console = Console()


class TestRunner:
    def __init__(self, ai_engine: AIEngine, target_project_path: Path):
        self.ai_engine = ai_engine
       
        self.tests_dir = target_project_path / "tests_generated_by_ai"
        self.tests_dir.mkdir(exist_ok=True)

    def run_and_fix(self, file_info: dict, test_code: str) -> bool:
        safe_name = file_info["name"].replace(".py", "")
        test_filename = self.tests_dir / f"test_{safe_name}.py"

        self._save_test(test_filename, test_code)

       
        success, error_output = self._run_pytest(test_filename)
        if success:
            console.print(f"[green]✓ PASS: {file_info['name']}[/green]")
            return True
        else:
            console.print(
                f"[yellow]↻ FAIL: {file_info['name']}. Attempting auto-fix...[/yellow]"
            )
            fixed_code = self.ai_engine.fix_test_code(test_code, error_output)
            self._save_test(test_filename, fixed_code)
           
            success, _ = self._run_pytest(test_filename)
            return success

    def _save_test(self, filepath: Path, code: str):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)

    def _run_pytest(self, test_filepath: Path):
        result = subprocess.run(
            ["pytest", str(test_filepath), "-q", "--tb=short"],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0, result.stdout + "\n" + result.stderr
