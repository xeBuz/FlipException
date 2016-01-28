# FlipException
_uoᴉʇdǝɔxƎdᴉꞁᖵ ǝsᴉɐɹ_

The best way to flip an exception out of rage.


## Installation
```bash
pip install flipexception
```


## Usage

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flipexception import FlipException


try:
    raise FlipException("Oops, something happens")
except Exception, e:
    print str(e)
```

```
(╯°□°）╯︵ suǝddɐɥ ƃuᴉɥʇǝɯos 'sdoO
```



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flipexception import FlipException
    
try:
    raise FlipException()
except FlipException, e:
    print str(e)
```

```
(╯°□°）╯︵ ┻━┻
```


