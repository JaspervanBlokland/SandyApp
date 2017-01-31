# 
#    Example Poster Identity
#
# Create a RootStyle instance by calling function. Alter some of the default values
# on initialization, so we don't that to replace them later for our version of the 
# root style.

from pagebot.style import getRootStyle
# Document is the main instance holding all information about the document togethers (pages, styles, etc.)
from pagebot.document import Document
from pagebot.page import Template

SHOW_GRID = False
SHOW_GRID_COLUMNS = False
SHOW_BASELINE_GRID = False

W = 520
H = 700

RS = getRootStyle(
    w=W, h=H, 
    showGrid=SHOW_GRID, 
    showGridColumns=SHOW_GRID_COLUMNS,
    showBaselineGrid = SHOW_BASELINE_GRID,
)
RS['docW'] = W + 200
RS['docH'] = H + 200

def makeDocument():

    
    template = Template(RS) # Create template of main size. Front page only.
    # Show grid columns and margins if rootStyle.showGrid or rootStyle.showGridColumns are True
    template.grid(RS) 
    # Show baseline grid if rs.showBaselineGrid is True
    # Create empty image place holders. To be filled by running content on the page.
    #template.cContainer(2, -0.7, 5, 4, rs)  # Empty image element, cx, cy, cw, ch
    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template2
    return Document(RS, pages=1, template=template) 
        
d = makeDocument()
d.export('_export/PosterIdentity.pdf')


