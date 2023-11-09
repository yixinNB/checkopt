# quick start
```
import checkopt  
print(checkopt.checkopt("g help m|module="))

(venv) PS D:\python> python .\test.py -m module_name --help -g project_name
({'m': 'module_name', 'help': None, 'g': None}, ['project_name'])
```

```
checkopt.checkopt("m|module=* f=")
(venv) PS D:\python> python .\demo.py -m module_name1 -m module_name2 extra_data -f 123
({'module': ['module_name1', 'module_name2'], 'f': '123'}, ['extra_data'])
```
# argument format
`short_option|long_option=*`  
example: `m|mocule=*`  
`=` (optional) means the option receives an  argument  
`*` (optional) means the option allows multiple arguments and the corresponding data will be a string list  
while space is the char to split to option pattern  

# Superiority compared to getopt
code:
```
print(getopt.getopt(sys.argv[1:], "m:h")) 
print(checkopt.checkopt("m= h|help"))

(venv) PS D:\WorkSpace\python> python .\container_update.py -h file -m abc 
```
result:
```
([('-h', '')], ['file', '-m', 'abc']) # getopt
({'h': None, 'm': 'abc'}, ['file'])   # checkopt ╰(*°▽°*)╯
```
