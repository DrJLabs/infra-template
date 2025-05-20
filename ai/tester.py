import subprocess
from autogen_agentchat.agents import AssistantAgent


class Tester(AssistantAgent):
    role = "tester"
    description = "Runs pytest + coverage."

    async def generate_reply(self, messages, _) -> str:
        """Execute the test suite and return exit code and output."""
        try:
            result = subprocess.run(
                ["make", "test"],
                capture_output=True,
                text=True,
                timeout=120,
            )
            output = result.stdout + result.stderr
            return f"Exit code: {result.returncode}\n{output}"
        except FileNotFoundError as exc:
            return f"Failed to run tests: {exc}"
        except subprocess.TimeoutExpired as exc:
            return f"Test run timed out after {exc.timeout} seconds."
