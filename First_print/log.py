# -*- coding: utf-8 -*-
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

FORMAT = '%(asctime)s %(module)s %(levelname)s - %(message)s'
DATEFMT = '%Y-%m-%d-%H:%M:%S'
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt=DATEFMT)

LOGGER.setLevel(logging.ERROR)