import sys
import os
import colorama as c

if len(sys.argv) == 1:
    print(f"{c.Fore.RED}Invalid command: None\n{c.Fore.YELLOW}Use devtools.exe help for help.{c.Style.RESET_ALL}")
    sys.exit(1)

match sys.argv[1]:
    case "help":
        print(f"build  : Builds the wheel and source distribution files.              {c.Fore.GREEN}•{c.Style.RESET_ALL} No user input")
        print(f"check  : Checks the wheel and source distribution files.              {c.Fore.GREEN}•{c.Style.RESET_ALL} No user input")
        print(f"fix    : Fixes the wheel and source distribution files.               {c.Fore.GREEN}•{c.Style.RESET_ALL} No user input")
        print(f"publish: Publish the wheel and source distribution files to PyPi.     {c.Fore.YELLOW}•{c.Style.RESET_ALL} Requires user input")
        print(f"test   : Publish the wheel and source distribution files to TestPyPi. {c.Fore.YELLOW}•{c.Style.RESET_ALL} Requires user input")
    case "build":
        if os.system("hatch build") == 0:
            print(f"{c.Fore.GREEN}Built wheel and source distribution files!{c.Style.RESET_ALL}")
        else:
            print(f"{c.Fore.RED}Failed to build wheel and source distribution files!{c.Style.RESET_ALL}")
            sys.exit(1)
    case _:
        print(f"{c.Fore.RED}Invalid command: {sys.argv[1]}\n{c.Fore.YELLOW}Use \"devtools.exe help\" for help.{c.Style.RESET_ALL}")
        sys.exit(1)

sys.exit(0)