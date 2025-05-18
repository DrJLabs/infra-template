import asyncio

from autogen import GroupChat, ConversableAgent
from coder import Coder
from docsmith import DocSmith
from planner import Planner
from reviewer import Reviewer
from tester import Tester


async def main(ticket: str):
    chat = GroupChat(
        agents=[Planner(), Coder(), Tester(), Reviewer(), DocSmith()],
        messages=[f"### Ticket {ticket}: See backlog.md"]
    )
    await chat.run()

if __name__ == "__main__":
    import sys
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "0"))
