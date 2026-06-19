# Task 5 expectations:
# - Sort tasks using a custom key function (no itemgetter)
# - Primary: priority (1 = highest)
# - Secondary: deadline (earliest first)
# - Filter tasks whose deadlines fall within the next 3 days from current time
# - Implement fast lookup by task "name" using a dictionary (hash map)
# - Ensure lookup complexity is O(1) for 100,000+ tasks
# - Avoid linear search for name-based retrieval
# - Maintain consistent internal task structure after parsing

import random
import time
from datetime import datetime, timedelta

def generate_mock_tasks(n=100000): #Victor
    random.seed(42)
    names = [f"Task_{i}" for i in range(n)]
    priorities = [random.randint(1, 5) for _ in range(n)]
    base = datetime(2026, 6, 19)
    deadlines = [(base + timedelta(days=random.randint(-5, 30))).strftime("%Y-%m-%d") for _ in range(n)]
    return [{"name": n, "priority": p, "deadline": d} for n, p, d in zip(names, priorities, deadlines)]


_index = {}

def build_index(tasks): # @Everyone
    for task in tasks:
        _index[task["name"]] = task
    return _index


def search_task(tasks, keyword): # Praise
    if keyword not in _index:
        build_index(tasks)
    return _index.get(keyword) # Constant search time O(1) using dictionary lookup


def cast_date_string_to_datetime(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")


def sort_tasks_by_priority(tasks): #Doreck
    for task in tasks:
        task["deadline_dt"] = cast_date_string_to_datetime(task["deadline"])
    return sorted(tasks, key=lambda t: (t["priority"], t["deadline_dt"])) #Lexiggraphical sorting by priority and deadline


def due_in_3_days(tasks): #Joseph
    now = datetime(2026, 6, 19)
    end = now + timedelta(days=3)
    return [t for t in tasks if now <= t.get("deadline_dt", cast_date_string_to_datetime(t["deadline"])) <= end]


def get_time_taken(tasks=None): # @Everyone
    times = {}

    start = time.perf_counter()
    sorted_tasks = sort_tasks_by_priority(tasks)
    times["sort"] = time.perf_counter() - start

    idx = build_index(tasks)

    start = time.perf_counter()
    search_task(tasks, "Task_50000")
    times["search"] = time.perf_counter() - start

    return times


# Testing the functions
tasks = generate_mock_tasks()

build_index(tasks)

result = search_task(tasks, "Task_50000")
print(f"Search result: {result}")

sorted_tasks = sort_tasks_by_priority(tasks)

print(f"Sorted by priority: {sorted_tasks[0]['name']} (priority {sorted_tasks[0]['priority']})")

print(f"Sorted by priority: {sorted_tasks[-1]['name']} (priority {sorted_tasks[-1]['priority']})")

due = due_in_3_days(tasks)
print(f"Tasks due in 3 days: {len(due)}")

times = get_time_taken(tasks)
print(f"Time taken - sort: {times['sort']:.4f}s, search: {times['search']:.4f}s")
