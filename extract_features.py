import re
import os

with open("purelane-homepage.html", "r") as f:
    content = f.read()

def extract_css(classes):
    css_blocks = []
    # VERY basic regex, better to just extract the whole <style> block and grep it manually if this fails.
    # We will search the CSS manually.
    pass

# Instead of complex regex, let's just create a python script that will extract the HTML and we will manually extract CSS.
