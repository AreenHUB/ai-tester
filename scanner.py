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
                exclude in root
                for exclude in ["venv", ".git", "__pycache__", "generated_tests"]
            ):
                continue

            for file in files:
                if (
                    file.endswith(".py")
                    and not file.startswith("test_")
                    and file not in self.AGENT_FILES
                ):
                    file_path = Path(root) / file

                    # السحر هنا: استخراج مسار الاستيراد الصحيح للمشروع
                    # مثلا: تحويل "app/core/security.py" إلى "app.core.security"
                    relative_path = file_path.relative_to(self.project_path)
                    module_import_path = str(relative_path.with_suffix("")).replace(
                        os.sep, "."
                    )

                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()

                    if content:
                        target_files.append(
                            {
                                "name": file_path.name,
                                "path": str(file_path),
                                "module_path": module_import_path,  # أضفنا هذا المفتاح الجديد
                                "content": content,
                            }
                        )
        return target_files
