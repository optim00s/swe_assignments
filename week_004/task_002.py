import asyncio

async def download_file(name):
    print(f"downloading {name} file ...")
    await asyncio.sleep(2)
    return f"{name} file is downloaded"

async def main():
    results = await asyncio.gather(
        download_file("app_v2.exe"),
        download_file("syllabus.pdf"),
        download_file("mnist_data.csv")
    )

    print(results)

asyncio.run(main())


