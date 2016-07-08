from threading import Thread
from time import time

def benchmark(func):
    def bench(*args, **kwargs):
        start = time()

        func(*args, **kwargs)

        end = time()
        print("Run took {:0.3f}".format(end - start))

    return bench

def run(start, stop=None):

    # build the start and stop args for range()
    if stop is None:
        args = [start]
    else:
        args = [start, stop]

    for i in range(*args):
        filename = 'files/{}.txt'.format(i)
        with open(filename) as f:
            f.read()

@benchmark
def unthreaded_run(start, stop=None):
    run(start, stop)

@benchmark
def threaded_run(start, stop=None, thread_count=4):
    threads = []
    block_size = 1000 // thread_count
    for i in range(thread_count):
        start = i * block_size
        stop = (i+1) * block_size
        thread = Thread(target=run, kwargs={'start': start, 'stop': stop})
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    print("Unthreaded access to 1000 files...")
    unthreaded_run(1000)
    print("Threaded access to 1000 files...")
    threaded_run(1000, thread_count=4)
