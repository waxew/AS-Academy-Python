"""Todo CLI آموزشی با نگهداری داده در حافظه."""

from dataclasses import dataclass


@dataclass
class Task:
    """یک کار با وضعیت انجام‌شدن."""

    title: str
    done: bool = False


def add_task(tasks: list[Task], title: str) -> Task:
    """کار معتبر را به فهرست اضافه می‌کند."""
    clean_title = title.strip()
    if not clean_title:
        raise ValueError("title cannot be empty")
    task = Task(clean_title)
    tasks.append(task)
    return task


if __name__ == "__main__":
    tasks: list[Task] = []
    add_task(tasks, "Learn Python")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.title}")
