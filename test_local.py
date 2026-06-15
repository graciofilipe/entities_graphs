import asyncio
from src.agent.agent import app

async def main():
    test_input = "Filipe Gracio visited the British Museum in London. He then took a train to Paris to meet Yann LeCun."
    print("Testing locally...")
    response = app.async_stream_query(message=test_input, user_id="test_user")
    async for chunk in response:
        print(chunk)

asyncio.run(main())
