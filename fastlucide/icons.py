from .core import SvgSprites
from functools import partial

__all__ = ['spritesheet']

spritesheet = SvgSprites()

def __getattr__(nm):
    if nm.startswith('_'): raise AttributeError()
    nm = nm.lower().replace('_','-')
    if nm not in spritesheet.icons: raise AttributeError()
    spritesheet.nms.add(nm)
    return partial(spritesheet, nm)

def __dir__():
    return [(o[0].upper()+o[1:]).replace('-','_')
            for o in spritesheet.icons]

