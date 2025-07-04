"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['read_icons', 'sz_attrs', 'symbol', 'sprites', 'icon', 'SvgStyle', 'SvgSprites']

# %% ../nbs/00_core.ipynb 2
from fastcore.utils import *
from fastcore.xml import *
from fasthtml.common import *
from fasthtml.svg import *
from json import loads
import pathlib

# %% ../nbs/00_core.ipynb 4
def read_icons():
    path = pathlib.Path(__file__).parent
    fpath = path/'_icons.py'
    return loads(fpath.read_text())

# %% ../nbs/00_core.ipynb 8
def sz_attrs(sz):
    "Attrs necessary to size an SVG"
    return dict(viewBox=f'0 0 24 24', width=f'{sz}px', height=f'{sz}px')

# %% ../nbs/00_core.ipynb 10
def symbol(
    icons, # icon dict
    nm, # Name of icon in lucide
    pre='' # Prefix to add to element id
):
    "Create a `symbol` element for an icon"
    ico = icons[nm]
    sym = [ft(t, **attrs) for t,attrs in ico]
    return Symbol(*sym, id=pre+nm)

# %% ../nbs/00_core.ipynb 12
def sprites(
    icons, # icon dict
    nms, # List of lucide icon names
    pre='' # Prefix to add to all element ids
):
    "SVG element containing all symbols in `nms`"
    syms = [symbol(icons, nm, pre) for nm in nms]
    return Svg(Defs(*syms), style="display: none")

# %% ../nbs/00_core.ipynb 14
def icon(
    nm, # Name of icon in lucide
    pre='', # Prefix to add to element id
    cls="lucide-icon", # class to use for svg
    sz=24, # size of svg
    **attrs # additional attrs for svg
):
    "A `use` element in an `svg` element refering to `nm`"
    return Svg(Use(href=f"#{pre}{nm}"), cls=cls, icon=nm, **sz_attrs(sz), **attrs)

# %% ../nbs/00_core.ipynb 17
def SvgStyle(cls="lucide-icon"):
    "Styles required for lucide icons to display correctly"
    return Style(f'.{cls} {{ stroke: currentColor; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }}')

# %% ../nbs/00_core.ipynb 18
class SvgSprites:
    "Create an track used icons"
    def __init__(self, pre='', sz=24, cls="lucide-icon", nms=(), **attrs):
        nms = set(nms)
        self.attrs = attrs
        self.icons = read_icons()
        store_attr()

    def __call__(self, nm, sz=None, cls="", **kw):
        self.nms.add(nm)
        if not sz: sz=self.sz
        attrs = self.attrs | kw
        return icon(nm, self.pre, sz=sz, cls = f"{self.cls} {cls}", **attrs)

    def __ft__(self):
        return SvgStyle(cls=self.cls),sprites(self.icons, self.nms, self.pre)
