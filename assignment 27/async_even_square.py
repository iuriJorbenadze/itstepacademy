
import asyncio

async def is_even(number):
    return number % 2 == 0

async def square_if_even(number):
    if await is_even(number):
        return number * number
    return None

async def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = await asyncio.gather(*(square_if_even(number) for number in numbers))
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
