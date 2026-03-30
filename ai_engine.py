import os, time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class AIEngine:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model_name = "llama-3.3-70b-versatile"
        self.system_prompt = (
            "You are a Senior Python QA Engineer. Write 100% reliable pytest unit tests. "
            "Cover happy paths, edge cases, and exceptions (pytest.raises). "
            "Use absolute imports based on the provided module path. "
            "Output ONLY raw python code. No markdown, no conversational text."
        )

    def _generate(self, prompt: str) -> str:
        for attempt in range(3):
            try:
                response = self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": prompt},
                    ],
                    model=self.model_name,
                    temperature=0.1,
                )
                return (
                    response.choices[0]
                    .message.content.replace("```python", "")
                    .replace("```", "")
                    .strip()
                )
            except Exception as e:
                if "429" in str(e):
                    time.sleep(10)
                else:
                    raise e
        return ""

    def generate_tests_for_file(self, file_info: dict) -> str:
        return self._generate(
            f"Write pytest for module {file_info['module_path']}:\n{file_info['content']}"
        )

    def fix_test_code(self, test_code: str, error_message: str) -> str:
        return self._generate(
            f"Failed test:\n{test_code}\n\nPytest Error:\n{error_message}\n\nFix it."
        )
