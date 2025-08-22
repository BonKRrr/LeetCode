def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    days_to_wait = [0] * n
    mono_stack = []
    for i in range(n):
        while len(mono_stack) > 0:
            j = mono_stack[-1]
            if temperatures[i] <= temperatures[j]:
                break
            mono_stack.pop()
            days_to_wait[j] = i - j
        mono_stack.append(i)
    return days_to_wait
