from selenium import webdriver
from selenium.webdriver.common.by import By

file = "C:\\Users\\Windows\\Downloads\\ResumeFile.txt"

fileOpen = open(file)

readfile = fileOpen.read()

print(readfile)
fileOpen.close()

