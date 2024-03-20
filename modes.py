from threading import Thread
from multiprocessing import Process
from asyncio import create_task, gather
from time import time
from image_loader import ImageLoader


class Modes():

    def handle_urls_thread(url_list: list, path_to_save: str = './images/') -> None:
        start_time = time()
        threads = []

        for url in url_list:
            thread = Thread(target=ImageLoader.get_image_from_url, args=(url, path_to_save))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f'Загрузка при многопоточном подходе: {time() - start_time:.2f} сек')

    def handle_urls_process(url_list: list, path_to_save: str = './images/') -> None:
        start_time = time()
        processes = []

        for url in url_list:
            process = Process(target=ImageLoader.get_image_from_url, args=(url, path_to_save))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print(f'Загрузка при многопроцессорном подходе: {time() - start_time:.2f} сек')

    async def handle_urls_async(url_list: list, path_to_save: str = './images/') -> None:
        start_time = time()
        tasks = []

        for url in url_list:
            task = create_task(ImageLoader.async_get_image_from_url(url, path_to_save))
            tasks.append(task)

        await gather(*tasks)

        print(f'Загрузка при асинхронном подходе: {time() - start_time:.2f} сек')
