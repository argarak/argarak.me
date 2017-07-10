
from common import app

class text_style:
    normal  = " [-]"
    header  = "\033[95m"
    info    = "\033[94m [#]"
    success = "\033[92m [+]"
    warn    = "\033[93m [*]"
    fail    = "\033[91m [!]"
    end     = "\033[0m"
    bold    = "\033[1m"
    uline   = "\033[4m"

@app.template_filter('print')
def debug_print(value):
    print(text_style.warn, end="\t")
    print(value, end=text_style.end)

    return value
