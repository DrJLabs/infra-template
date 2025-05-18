from autogen import AssistantAgent

class Coder(AssistantAgent):
    role = "coder"
    description = "Writes or edits code to satisfy planner ticket."

    async def generate_reply(self, messages, _) -> str:
        return "Implemented feature XYZ; opened PR #123."
