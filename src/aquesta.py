from pypy.rlib.parsing.ebnfparse import parse_ebnf, make_parse_function
from pypy.rlib.parsing.parsing import ParseError
from pypy.rlib.streamio import open_file_as_stream
from os.path import abspath, join, dirname
import sys


def parse(code):
    GFILE = open_file_as_stream(abspath(join(dirname(__file__), "grammar.txt")))

    t = None
    try:
        t = GFILE.read()
        regexs, rules, ToAST = parse_ebnf(t)
    except ParseError,e:
        print e.nice_error_message(filename=str(GFILE),source=t)
        raise

    parsef = make_parse_function(regexs, rules, eof=True)

    t = parsef(code)
    return ToAST().transform(t)

def main(argv):
    code = parse(argv[1])
    print code
    return 0

def target(driver, args):
    return main, None

if __name__ == '__main__':
    main(sys.argv)
