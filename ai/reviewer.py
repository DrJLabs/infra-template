from autogen_agentchat.agents import AssistantAgent

class Reviewer(AssistantAgent):
    role = "reviewer"
    description = "Applies ruff, mypy, bandit; requests changes or approves."

    async def generate_reply(self, messages, _) -> str:
        """Run lint and tests, returning a short summary."""
        import subprocess

        lint = subprocess.run(
            ["make", "lint"], capture_output=True, text=True
        )
        tests = subprocess.run(
            ["make", "test"], capture_output=True, text=True
        )

        summary = []
        summary.append(
            "Lint passed." if lint.returncode == 0 else "Lint failed."
        )
        summary.append(
            "Tests passed." if tests.returncode == 0 else "Tests failed."
        )

        return "\n".join(summary)
