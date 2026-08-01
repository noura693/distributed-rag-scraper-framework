MAX_RETRIES = 3

dead_letter_queue = []


def process_task(task):

    retries = task.get("retries", 0)

    try:

        if task["should_fail"]:
            raise Exception("Task failed")

        print(f"Task completed successfully: {task['id']}")

    except Exception:

        retries += 1

        print(
            f"Task {task['id']} failed "
            f"(attempt {retries})"
        )

        task["retries"] = retries

        if retries >= MAX_RETRIES:

            dead_letter_queue.append(task)

            print(
                f"Task {task['id']} moved "
                f"to Dead-Letter Queue"
            )

        else:

            process_task(task)


task_1 = {
    "id": 1,
    "should_fail": True,
    "retries": 0
}

task_2 = {
    "id": 2,
    "should_fail": False,
    "retries": 0
}

process_task(task_1)
process_task(task_2)

print("\nDead-Letter Queue:")
print(dead_letter_queue)