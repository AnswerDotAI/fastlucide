from .core import SvgSprites
from functools import partial

__all__ = ['spritesheet','combined']

spritesheet = SvgSprites()

def __getattr__(nm):
    if nm.startswith('_'): raise AttributeError()
    nm = nm.lower().replace('_','-')
    if nm not in spritesheet.icons: raise AttributeError()
    spritesheet.nms.add(nm)
    return partial(spritesheet, nm)

def combined(nm1, nm2, position='overlap', sz=None, 
             stroke1=None, fill1=None, stroke2=None, fill2=None, **kw):
    return spritesheet.combined(nm1, nm2, position, sz, 
             stroke1=stroke1, fill1=fill1, stroke2=stroke2, fill2=fill2, **kw)

def __dir__():
    return [(o[0].upper()+o[1:]).replace('-','_')
            for o in spritesheet.icons]
