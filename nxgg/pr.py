# coding = 'utf-8'
import re
content = 'hello 123 4567 world_This is Regex Demo'

print(len(content))

result = re.match('^hello\s\d\d\d\s\d\d\d\d\s',content)
print(result)