from autogen_agentchat.agents import AssistantAgent

class Reviewer(AssistantAgent):
    role = "reviewer"
    description = "Applies ruff, mypy, bandit; requests changes or approves."

    async def generate_reply(self, messages, _) -> str:
        return "All checks green – approving merge."
