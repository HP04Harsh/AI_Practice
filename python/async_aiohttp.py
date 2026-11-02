import asyncio
import aiohttp

async def get_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():

    urls = ["https://jsonplaceholder.typicode.com/posts/"]

    task = [get_url(url) for url in urls]
    results = await asyncio.gather(*task)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
