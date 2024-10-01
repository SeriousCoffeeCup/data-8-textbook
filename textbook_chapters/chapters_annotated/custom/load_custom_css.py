from IPython.core.display import HTML

def load_custom_css():
    custom_css = open('custom.css', 'r').read()
    return HTML('<style>{}</style>'.format(custom_css))

load_custom_css()
# Doesn't work