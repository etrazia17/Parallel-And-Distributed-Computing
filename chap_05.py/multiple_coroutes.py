import asyncio

async def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print(f"Compute factorial({i})")
        await asyncio.sleep(1)
        f *= i
    print(f"factorial({number}) = {f}")

async def fibonacci(number):
    a, b = 0, 1
    for _ in range(number):
        print(f"Compute fibonacci({_})")
        await asyncio.sleep(1)
        a, b = b, a + b
    print(f"fibonacci({number}) = {a}")

async def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print(f"Compute binomial_coefficient({i})")
        await asyncio.sleep(1)
    print(f"binomial_coefficient({n}, {k}) = {result}")

async def main():
    tasks = [
        asyncio.create_task(factorial(10)),
        asyncio.create_task(fibonacci(10)),
        asyncio.create_task(binomial_coefficient(20, 10))
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())