import slimmer
from compress.filter_base import FilterBase

class SlimmerCSSFilter(FilterBase):
    def filter_css(self, css):
        return slimmer.css_slimmer(css)