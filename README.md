# link_shortener
It is a basic link shortener with basic and advanced utilites with python
# Usage short_link()

´´´python
Shortf().short_link(link="link_here", path="path_here", logstats=False, proxies={"https":"ip:port"})
```

```python
print(Shortf().short_link(link="https://youtu.be/dQw4w9WgXcQ", path="my_special_path", logstats=False, proxies={}))
```

OUTPUT
```bash
https://is.gd/my_special_path
```

# Usage lookup()
´´´python
Shortf().lookup(link="link_here", proxies={"https":"ip:port"})
```
```python
#print(Shortf().lookup(link="https://is.gd/my_special_path"))
```
OUTPUT
```bash
https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be
```
