
import asyncio
import random

async def print_numbers_with_random_delay():
    delay = random.randint(1, 5)  # Randomly choosing a delay between 1 to 5 seconds
    print(f"Starting with a delay of {delay} seconds")
    await asyncio.sleep(delay)
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(0.5)  # Adding a small delay between prints for readability

async def main():
    await print_numbers_with_random_delay()

if __name__ == "__main__":
    asyncio.run(main())
