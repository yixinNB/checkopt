import re
import sys


def __decode(opts_pattern: str):
    opts_pattern = opts_pattern.split(" ")
    short_opts, long_opts = {}, {}
    for item in opts_pattern:
        item, tmp = item[:-1], item[-1:]
        if tmp == "=":
            need_arg = True
        else:
            need_arg = False
            item = item + tmp
        # 短或长只允许一个
        try:
            a, b = item.split("|")
            short_opts[a] = {
                "alias": b,
                "need_arg": need_arg
            }
            long_opts[b] = {
                "alias": a,
                "need_arg": need_arg
            }
        except:
            if len(item) == 1:
                short_opts[item] = {
                    "alias": None,
                    "need_arg": need_arg
                }
            else:
                long_opts[item] = {
                    "alias": None,
                    "need_arg": need_arg
                }
    return short_opts, long_opts


def __is_flag(s: str):
    if re.search("^--[a-zA-Z][a-zA-Z]+$", s) is not None:
        return 2
    if re.search("^-[a-zA-Z]$", s) is not None:
        return 1
    return 0


def checkopt(opts, err="please check your input"):
    short_opts, long_opts = __decode(opts)
    origin_args = iter(sys.argv[1:])
    # origin_args=iter(["-h","123", "-o", "123"]) #todo change it
    opts, args = {}, []

    if len(sys.argv[1:]) == 0:
        return opts, args

    # allow args at the beginning of the line if there is only one
    first = origin_args.__next__()
    if __is_flag(first) == 0:
        args.append(first)
    else:
        origin_args = iter(sys.argv[1:])
        # origin_args = iter(["-h","123", "-o", "123"]) #todo change it

    while True:
        try:
            flag_or_arg = origin_args.__next__()
        except StopIteration:
            break
        if __is_flag(flag_or_arg) == 2:
            flag2 = flag_or_arg.strip("-")
            assert flag2 in long_opts, f"--{flag2} is not expected"
            assert long_opts[flag2]["alias"] not in opts
            if long_opts[flag2]["need_arg"]:
                arg = origin_args.__next__()
                assert __is_flag(arg) == 0
                opts[flag2] = arg
            else:
                opts[flag2] = None

        elif __is_flag(flag_or_arg) == 1:
            flag1 = flag_or_arg.strip("-")
            assert flag1 in short_opts, f"-{flag1} is not expected"
            assert short_opts[flag1]["alias"] not in opts
            if short_opts[flag1]["need_arg"]:
                arg = origin_args.__next__()
                assert __is_flag(arg) == 0
                opts[flag1] = arg
            else:
                opts[flag1] = None
        else:
            arg = flag_or_arg
            args.append(arg)
    return opts, args
