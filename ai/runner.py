import asyncio, os
from autogen import GroupChat, setup_openai

from planner import Planner
from coder   import Coder
from tester  import Tester
from reviewer import Reviewer
from docsmith import DocSmith

setup_openai(api_key=os.getenv("OPENAI_API_KEY"))

async def main(ticket: str):
    chat = GroupChat(
        agents=[Planner(), Coder(), Tester(), Reviewer(), DocSmith()],
        messages=[f"### Ticket {ticket}: See backlog.md"]
    )
    await chat.run()

if __name__ == "__main__":
    import sys
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "0"))
