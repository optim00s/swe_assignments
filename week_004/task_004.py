import asyncio
import time

async def task():
    """
    time.sleep() əvəzinə await ilə asyncio.sleep() istifadə etməliyik,
    çünki bu halda hər task üçün 2 saniyə gözləyərək 
    ümumi prossesin müddətini 6 saniyə edirik
    +
    bir növ sinxron koda çevirmiş oluruq
    """
    time.sleep(2)
    print("Done")

async def main():
    await asyncio.gather(
    task(), task(), task()
    )

# ikinci xəta isə kodun düzgün icra olunmaması
asyncio.run(main())

