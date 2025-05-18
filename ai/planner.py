from autogen_agentchat.agents import AssistantAgent

class Planner(AssistantAgent):
    role = "planner"
    description = "Breaks backlog tasks into atomic tickets."

    async def generate_reply(self, messages, _) -> str:
        # VERY simple; refine later.
        return "Split task into smaller chunks and assign to coder."
