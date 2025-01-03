import asyncio
from random import randint

async def start_state():
    print("Start State called")
    input_value = randint(0, 1)
    await asyncio.sleep(1)
    if input_value == 0:
        result = await state_2(input_value)
    else:
        result = await state_1(input_value)
    print(f"Transition Summary: {result}")

async def state_1(input_value):
    print("State 1 with transition value =", input_value)
    await asyncio.sleep(1)
    if input_value == 0:
        return await state_2(input_value)
    else:
        return await state_3(input_value)

async def state_2(input_value):
    print("State 2 with transition value =", input_value)
    await asyncio.sleep(1)
    if input_value == 0:
        return await state_1(input_value)
    else:
        return await state_3(input_value)

async def state_3(input_value):
    print("State 3 with transition value =", input_value)
    await asyncio.sleep(1)
    return "End State reached"

if __name__ == "__main__":
    asyncio.run(start_state())