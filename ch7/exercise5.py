#exercise5.py
from xml.etree.ElementTree import Element,SubElement,ElementTree

blog = Element("blog")
blog.attrib["date"] = "20151231"

SubElement(blog, "subject").text = "Why python?"
SubElement(blog,"author").text = "Eric"
SubElement(blog, "content").text = "Life is too short, You need Python!"

ElementTree(blog).write("blog.xml")
