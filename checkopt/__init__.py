import re
import sys
'''
opts_patterns
{
        "option_name":{
            "alias": "corresponding short or long option name",
            "need_arg":bool,
            "mutiple_arg":bool,# If this option is true, the corresponding data type is a list.
        }
}

exanple of opts_pattern
m|module=*
means
-m or --module, need one or more arguments

If the option has an alias, the corresponding data be added to the long option
'''


def __decode(opts_str_pattern: str):
    opts_str_patterns = opts_str_pattern.split(" ")
    opts_patterns={}
    for item in opts_str_patterns:
        item, tmp = item[:-1], item[-1:]
        if tmp == "*":
            need_arg=True
            mutiple_arg = True
            assert item[-1:]=="=","opts_pattern must have = if it has *"
            item=item[:-1]
        elif tmp == "=":
            need_arg = True
            mutiple_arg = False
        else:
            need_arg = False
            mutiple_arg = False
            item = item + tmp

        try:
            a, b = item.split("|")
            assert len(b)>1,"long pattern must after |"
            opts_patterns[a] = {
                "alias": b,
                "need_arg": need_arg,
                "mutiple_arg":mutiple_arg
            }
            opts_patterns[b] = {
                "alias": a,
                "need_arg": need_arg,
                "mutiple_arg":mutiple_arg
            }
        except:
            opts_patterns[item] = {
                "alias": None,
                "need_arg": need_arg,
                "mutiple_arg":mutiple_arg
            }
    return opts_patterns


def __is_flag(s: str):
    if re.search("^--[a-zA-Z][a-zA-Z]+$", s) is not None:
        return 2
    if re.search("^-[a-zA-Z]$", s) is not None:
        return 1
    return 0

def checkopt(opts_str_pattern, err="please check your input"):
    opts_pattern = __decode(opts_str_pattern)
    origin_args = iter(sys.argv[1:])
    opts, args = {}, []

    if len(sys.argv[1:]) == 0:
        return opts, args

    # TODO allow args at the beginning of the line only if there is only one

    while True:
        try:
            opt_or_arg = origin_args.__next__()
        except StopIteration:
            break

        if __is_flag(opt_or_arg) == 0:
            arg = opt_or_arg
            args.append(arg)
        else:
            opt = opt_or_arg.strip("-")
            alias = opts_pattern[opt]["alias"]
            if len(opt) == 1 and alias is not None:
                opt = alias
            assert opt in opts_pattern, f"option {opt} is not expected"
            mutiple_arg = opts_pattern[opt]["mutiple_arg"]
            assert mutiple_arg or opt not in opts, f"{opt} isn't allowed (multiple) arguments"
            need_arg = opts_pattern[opt]["need_arg"]
            if need_arg:
                arg = origin_args.__next__()
                assert __is_flag(arg) == 0, f"{arg} must be an argument"
            else:
                arg=None

            if mutiple_arg and opt not in opts:
                opts[opt]=[arg]
            elif mutiple_arg and opt in opts:
                opts[opt].append(arg)
            else:# only argument
                opts[opt]=arg

    return opts, args
