# quick start
```
import checkopt  
print(checkopt.checkopt("g help m|module="))

(venv) PS D:\python> python .\test.py -m module_name --help -g project_name
({'m': 'module_name', 'help': None, 'g': None}, ['project_name'])
```

# argument format
`short_opts|long_opts=`
`=`means the flag receives an  argument

# advantages
**getopt**
```
getopt.getopt(args, "m:h", ["help", "module="])
(venv) PS D:\WorkSpace\python> python .\test.py -h file -o -m abc
([('-h', '')], ['file', '-o', '-m', 'abc'])
```
**checkopt**
```
checkopt.checkopt("m= h|help")
(venv) PS D:\WorkSpace\python> python .\test.py -h file -o -m abc
AssertionError: -o is not expected
```


```
print(getopt.getopt(sys.argv[1:], "m:h")) 
print(checkopt.checkopt("m= h|help"))

(venv) PS D:\WorkSpace\python> python .\container_update.py -h file -m abc   
([('-h', '')], ['file', '-m', 'abc']) # getopt
({'h': None, 'm': 'abc'}, ['file'])   # checkopt
```
