from tasks import unreliable_task

for i in range(10):
    unreliable_task.delay(i)

print("10 jobs submitted")