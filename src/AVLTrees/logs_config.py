import logging


def set_log_config():
    logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        encoding='utf-8',
                        handlers=[logging.FileHandler("my_logs.log"),
                                  logging.StreamHandler()],
                        level=logging.INFO)
