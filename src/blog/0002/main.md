---
title: Better state machines with yield
date: 2016-10-23
---

The current *state* of things (haha).

```python
state = 'just starting'

while True:
    if state == 'just starting':
        print(1)
    elif state == 'the next step':
        print(2)
```

<!-- more -->
