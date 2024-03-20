from asyncio import run
from url_parser import url_parser
from modes import Modes
url_list = []


if __name__ == '__main__':

    url_list = url_parser()
    # если ничего не передали, используется папка с изображениями по умолчанию

    print(f"{'-' * 20} Многопоточный подход {'-' * 20}")
    Modes.handle_urls_thread(url_list, './images/threads')

    print(f"{'-' * 20} Многопроцессорный подход {'-' * 20}")
    Modes.handle_urls_process(url_list, './images/processes')

    print(f"{'-' * 20} Асинхронный подход {'-' * 20}")
    run(Modes.handle_urls_async(url_list, './images/asynchron'))
