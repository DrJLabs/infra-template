import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient


def pretty_print(history) -> None:
    """Print conversation regardless of (role, text) tuple or Message object."""
    for m in history:
        if isinstance(m, tuple):
            role, text = m
            print(f"[{role}] {text}")
        else:  # fallback for future Message objects
            print(f"[{getattr(m, 'author', 'unknown')}] {m.content}")


async def main(ticket: str = "demo") -> None:
    llm = OpenAIChatCompletionClient(model="gpt-4o")  # needs OPENAI_API_KEY
    planner = AssistantAgent("planner", llm, description="Break task")
    coder = AssistantAgent("coder", llm, description="Write code")
    reviewer = AssistantAgent("reviewer", llm, description="Review code")

    team = RoundRobinGroupChat([planner, coder, reviewer], max_turns=4)
    history = await team.run(
        task=f"Ticket {ticket}: print hello world and stop"
    )
    pretty_print(history)


if __name__ == "__main__":
    asyncio.run(main())
