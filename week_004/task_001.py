import asyncio

async def make_tea():
    print("making tea...")
    await asyncio.sleep(2)
    print("tea is ready")

async def make_coffee():
    print("making coffee...")
    await asyncio.sleep(3)
    print("coffee is ready")

async def make_sandwich():
    print("making sandwich...")
    await asyncio.sleep(4)
    print("sandwich is ready")

async def main():
    await asyncio.gather(
        make_tea(),
        make_coffee(),
        make_sandwich()
    )

asyncio.run(main())



