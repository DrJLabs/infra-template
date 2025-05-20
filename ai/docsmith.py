from autogen_agentchat.agents import AssistantAgent
import pathlib

class DocSmith(AssistantAgent):
    role = "docsmith"
    description = "Updates CHANGELOG and README after merge."

    async def generate_reply(self, messages, _) -> str:
        """Append the provided message to CHANGELOG.md."""
        changelog = pathlib.Path("CHANGELOG.md")
        entry = messages[-1]["content"] if messages else "No details provided."

        if changelog.exists():
            original = changelog.read_text()
        else:
            original = "# Changelog\n"

        changelog.write_text(f"{original}\n{entry}\n")
        return "Changelog updated."
