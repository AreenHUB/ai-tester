import os
from pathlib import Path


class ProjectScanner:
    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self.AGENT_FILES = ["main.py", "ai_engine.py", "scanner.py", "runner.py"]

    def get_target_files(self):
        target_files = []
        for root, dirs, files in os.walk(self.project_path):
            
            if any(
                part
                in [
                    ".git",
                    "venv",
                    "__pycache__",
                    "tests_generated_by_ai",
                    "tests_generated",
                ]
                for part in Path(root).parts
            ):
                continue

            for file in files:
                if (
                    file.endswith(".py")
                    and not file.startswith("test_")
                    and file not in self.AGENT_FILES
                ):
                    file_path = Path(root) / file

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read().strip()

                        if len(content) > 10:
                            
                            try:
                                relative_path = file_path.relative_to(self.project_path)
                                module_import_path = (
                                    str(relative_path)
                                    .replace(os.sep, ".")
                                    .replace(".py", "")
                                )
                            except ValueError:
                                module_import_path = (
                                    file_path.stem
                                )  

                            target_files.append(
                                {
                                    "name": file_path.name,
                                    "path": str(file_path),
                                    "module_path": module_import_path,
                                    "content": content,
                                }
                            )
                    except Exception as e:
                        continue
        return target_files
