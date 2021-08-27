from dataclasses import dataclass
from typing import List
import requests
from os import listdir
from lxml import etree


@dataclass
class CourseInfo():
    department: str
    instructor: str
    year: str
    semester: str
    serial_number: str # act as registeration code
    attribute_code: str
    system_number: str
    class_code: str
    credit: str
    language: str


def crawl_course(course_id: str, year: str, semester: str, class_code: str = None) -> CourseInfo:
    """Crawl NCKU course website for infomation

    Args:
        course_id (str): Course ID
        year (str): Course year
        semester (str): Course semester
        class_code (str): Class code, default to None
    """
    # Need to re-decode with utf-8, original is encoded with ISO-8859-1
    text: str = requests.get(
        "http://class-qry.acad.ncku.edu.tw/syllabus/online_display.php",
        params={
            "syear": year,
            "sem": semester,
            "co_no": course_id,
            "class_code": class_code
        }
    ).text.encode("ISO-8859-1").decode("utf-8")
    html: etree._Element = etree.HTML(text)
    sidebar: etree._Element = html.xpath('//*[@id="sidebar"]/div')[0]

    # remove unused br and strip whitespace head
    children: List[etree._Element] = sidebar.getchildren()
    filtered = list(filter(lambda child: child.tag == "span", children))
    information = list(map(lambda child: child.tail.strip(), filtered))

    return CourseInfo(*information)

crawl_course("F715910", "0110", "1")