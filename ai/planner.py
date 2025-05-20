from autogen_agentchat.agents import AssistantAgent

class Planner(AssistantAgent):
    role = "planner"
    description = "Breaks backlog tasks into atomic tickets."

    async def generate_reply(self, messages, _) -> str:
        """Parse backlog.md and return a checklist of sub-tasks."""
        import pathlib

        backlog_path = pathlib.Path("backlog.md")
        if not backlog_path.exists():
            return "No backlog available."

        lines = backlog_path.read_text().splitlines()
        tasks = [line.lstrip("- ").strip() for line in lines if line.startswith("-")]

        if not tasks:
            return "Backlog contains no actionable items."

        subtasks = "\n".join(f"- [ ] {task}" for task in tasks)
        return f"Planned tasks:\n{subtasks}"
