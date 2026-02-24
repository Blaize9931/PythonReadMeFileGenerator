from questions import collect_answers
from markdown import markdown
results = collect_answers()
print(results)
md_content = markdown(results)

print(md_content)