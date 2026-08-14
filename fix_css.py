import re

with open('sections/purelane-hero.liquid', 'r') as f:
    content = f.read()

# Remove the broken head tags
content = content.replace('</style>\n</head>\n<body>\n', '')

with open('sections/purelane-hero.liquid', 'w') as out:
    out.write(content)

