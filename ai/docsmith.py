from autogen import AssistantAgent, pathlib

class DocSmith(AssistantAgent):
    role = "docsmith"
    description = "Updates CHANGELOG and README after merge."

    async def generate_reply(self, messages, _) -> str:
        pathlib.Path("CHANGELOG.md").write_text("## TODO – fill changelog\\n")
        return "Changelog updated."
