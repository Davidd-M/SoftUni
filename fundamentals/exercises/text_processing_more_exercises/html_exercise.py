print(f"<h1>\n"
      f"    {input()}\n"
      f"</h1>\n"
      f"<article>\n"
      f"    {input()}\n"
      f"</article>")
comments = []
while True:
    new_comment = input()
    if new_comment == "end of comments":
        break
    comments.append(new_comment)
for comment in comments:
    print(f"<div>\n"
          f"    {comment}\n"
          f"</div>")