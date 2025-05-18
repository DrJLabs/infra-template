import asyncio
from ag2 import GroupChat
from planner import Planner
from coder import Coder
from tester import Tester
from reviewer import Reviewer
from docsmith import DocSmith
from tester  import Tester
from reviewer import Reviewer
from docsmith import DocSmith


async def main(ticket: str):
    chat = GroupChat(
        agents=[Planner(), Coder(), Tester(), Reviewer(), DocSmith()],
        messages=[f"### Ticket {ticket}: See backlog.md"]
    )
    await chat.run()

if __name__ == "__main__":
    import sys
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "0"))
