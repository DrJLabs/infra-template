# ai/runner.py  (replace existing file)
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main(ticket: str = "demo") -> None:
    llm = OpenAIChatCompletionClient(model="gpt-4o")  # reads OPENAI_API_KEY
    planner  = AssistantAgent("planner",  llm, description="Break task")
    coder    = AssistantAgent("coder",    llm, description="Write code")
    reviewer = AssistantAgent("reviewer", llm, description="Review code")
    team = RoundRobinGroupChat([planner, coder, reviewer], max_turns=4)
    history = await team.run(task=f"Ticket {ticket}: print hello world and stop")
    for m in history:
        print(f"[{m.author}] {m.content}")

if __name__ == "__main__":
    asyncio.run(main())
