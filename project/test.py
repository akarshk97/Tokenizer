import os
import re
import sys
from bs4 import BeautifulSoup
inputDir = sys.argv[1]
outputDir = sys.argv[2]
entries = os.listdir(inputDir)
print(entries)
print(outputDir)