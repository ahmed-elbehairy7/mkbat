from argparse import ArgumentParser
from os import path

defaults = {
    "verbose" : lambda args : lambda _ : _,
    "command" : lambda args : f"@{path.abspath(args.exe_file)} %*",
    "dist" : lambda args : r"D:\Apps\bin",
    "name": lambda args : path.splitext(path.basename(args.exe_file))[0]
    
}
def main():
    parser = ArgumentParser("mkbat")
    
    parser.add_argument("exe_file", help="The file to make a batch for")
    parser.add_argument("-v", "--verbose",  help="Verbose mode on", action="store_const", const=print)
    parser.add_argument("-n", "--name", "-o", "--output", metavar="", help="The name of the output file")
    parser.add_argument("-d", "--dist", metavar="", help="The destination dir for the batch file")
    parser.add_argument("-c", "--command", metavar="", help="Specify a command for the batch file rather than default one")
    
    args = parser.parse_args()
        
    a = {}
    
    for key, default in defaults.items():
        if args.__getattribute__(key):
            a[key] = args.__getattribute__(key)
        else:
            a[key] = default(args)

        a["verbose"](f"{key}: {a[key]}")
    
    with open(path.join(a["dist"], f'{a["name"]}.bat'), 'w') as f:
        f.write(a["command"])
    
        
    
        
    

if __name__=="__main__":
    main()