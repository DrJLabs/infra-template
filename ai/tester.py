from autogen import AssistantAgent, subprocess

class Tester(AssistantAgent):
    role = "tester"
    description = "Runs pytest + coverage."

    async def generate_reply(self, messages, _) -> str:
        result = subprocess.run("make test", shell=True, capture_output=True, text=True)
        return f"Pytest output:\\n{result.stdout}\\nErrors:\\n{result.stderr}"
