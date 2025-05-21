from autogen_agentchat.agents import AssistantAgent

class Coder(AssistantAgent):
    role = "coder"
    description = "Writes or edits code to satisfy planner ticket."

    async def generate_reply(self, messages, _) -> str:
        """Return a short summary of planned code changes for the ticket."""
        ticket = messages[-1]["content"] if messages else "(no ticket provided)"

        plan = [
            f"Working on: {ticket}",
            "- identify target modules",
            "- edit or create functions/classes",
            "- add unit tests",
            "- open a pull request",
        ]

        return "\n".join(plan)
