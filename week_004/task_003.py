import asyncio

async def send_email():
    print("email sending...")
    await asyncio.sleep(3)
    print("email is sent")

async def save_log():
    print("log starting...")
    await asyncio.sleep(1)
    print("log finished")

async def main():
    print("Main funksiyası başladı...")
    
    task1 = asyncio.create_task(send_email())
    task2 = asyncio.create_task(save_log())

    print("Main funksiyası bitdi, proqram bağlanır...")

# async def main():
#     print("Main funksiyası başladı...")

#     task1 = asyncio.create_task(send_email())
#     task2 = asyncio.create_task(save_log())

#     await task1
#     await task2 

#     print("Main funksiyası bitdi, proqram bağlanır...")

asyncio.run(main()) 

