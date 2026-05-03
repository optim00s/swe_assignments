import asyncio
import aiohttp

urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com"
]

async def fetch(session, url):
    async with session.get(url) as response:
        print(f"{url} - {response.status}")
    
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]

        await asyncio.gather(*tasks)

asyncio.run(main())
