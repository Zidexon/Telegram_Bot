import httpx

async def test_connection():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.telegram.org", timeout=10)
            print(f"Подключение работает: {response.status_code}")
    except Exception as e:
        print(f"Ошибка подключения: {e}")

import asyncio
asyncio.run(test_connection())