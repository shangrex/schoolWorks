from loguru import logger
from crawler import crawl_course


if __name__ == "__main__":
    logger.info(crawl_course("F715910", "0110", "1"))
