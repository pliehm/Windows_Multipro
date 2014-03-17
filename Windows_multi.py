### Import modules

import numpy as np
import time
import multiprocessing as mp
import time as time


number_of_processes = 4

if __name__ == '__main__':

    def reverse_np_array(arr):
        arr = arr + 1
        return arr

    a = np.ndarray((200,1024,1280),dtype=np.uint16)

    def put_into_queue(_Queue,arr):
        _Queue.put(reverse_np_array(arr))


    Queue_list = []
    Process_list = []
    list_of_arrays = []

    for i in range(number_of_processes):
        Queue_list.append(mp.Queue())


    for i in range(number_of_processes):
        Process_list.append(mp.Process(target=put_into_queue, args=(Queue_list[i],a)))

    for i in range(number_of_processes):
        Process_list[i].start()

    for i in range(number_of_processes):
        list_of_arrays.append(Queue_list[i].get())

    for i in range(number_of_processes):
        Process_list[i].join()





