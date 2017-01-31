# 
#    Example responsive FaceBook Banner
#
# Create a RootStyle instance by calling function. Alter some of the default values
# on initialization, so we don't that to replace them later for our version of the 
# root style.

from pagebot.style import getRootStyle
# Document is the main instance holding all information about the document togethers (pages, styles, etc.)
from pagebot.document import Document
from pagebot.page import Template

def mm(v):
    return int(round(v*72/25.4))

SHOW_GRID = True
SHOW_GRID_COLUMNS = True
SHOW_BASELINE_GRID = False


RS = getRootStyle(
    w=851, h=313, # Default 851 x 313
    showGrid=SHOW_GRID, 
    showGridColumns=SHOW_GRID_COLUMNS,
    showBaselineGrid = SHOW_BASELINE_GRID,
    )
FONT_SIZE = 24
RS['fontSize'] = FONT_SIZE
RS['baselineGrid'] = FONT_SIZE * 1.2
RS['docW'] = RS['w'] + 200
RS['docH'] = RS['h'] + 200

RED = (1, 0, 0, 0.5)

def makeDocument():

    
    template = Template(RS) # Create template of main size. Front page only.
    # Show grid columns and margins if rootStyle.showGrid or rootStyle.showGridColumns are True
    template.grid(RS) 
    # Show baseline grid if rs.showBaselineGrid is True
    template.baselineGrid(RS)
    cb = 3
    template.cRect(1, 0, cb, 1, RS, fill=(1, 0, 0))
    template.cRect(1+cb, 0, 3, 1, RS, fill=(0, 0, 0.5))
    # Create empty image place holders. To be filled by running content on the page.
    #template.cContainer(2, -0.7, 5, 4, rs)  # Empty image element, cx, cy, cw, ch
    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template2
    doc = Document(RS, pages=3, template=template) 
    
    doc.newStyle(name='title', fontSize=32, font='Verdana', textColor=RED)

    page = doc.pages[2]
    #page.style['w'] = 400
    #page.style['h'] = 200
    page.cRect(1, 1, cb, 1, RS, fill=(0, 0.5, 0))
    
    # For all pages in the document, add page number.
    for pageNumber in doc.pages:
        page = doc.pages[pageNumber] # Get this page
        # Add box with page number
        # TODO: Vertical page index is reversed direction now.
        page.cText('Page %s' % pageNumber, 8, 2, 1, 1, RS, 
            textColor=0, fontSize=32)
        # TODO: Apply style direct on this function.
        page.cText('Hallo', 4, 1, cb, 1, RS, textColor=RED)
    
    return doc 
    
d = makeDocument()
d.export('export/FaceBookBanner.pdf')


