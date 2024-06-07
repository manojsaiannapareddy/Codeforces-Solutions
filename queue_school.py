def queue_school():
    n, t = map(int, input().split())
    queue = list(input().strip())

    for _ in range(t):
        new_queue = queue.copy()
        for i in range(n - 1):
            if queue[i] == 'B' and queue[i + 1] == 'G':
                new_queue[i] = 'G'
                new_queue[i + 1] = 'B'
        queue = new_queue

    print("".join(queue))

queue_school()
