#
#    Example responsive FaceBook Banner
#

from pagebot.style import getRootStyle
from pagebot.document import Document
from pagebot.page import Template

SHOW_GRID = True
SHOW_GRID_COLUMNS = True
SHOW_BASELINE_GRID = False

RS = getRootStyle(
    w=851, h=313, #Default 851 x 313
    showGrid=SHOW_GRID,
    showGridColumns=SHOW_GRID_COLUMNS,
    showBaselineGrid = SHOW_BASELINE_GRID,
    )
FONT_SIZE = 24
RS['fontSize'] = FONT_SIZE
RS['baselineGrid'] = FONT_SIZE * 1.2
RS['docW'] = RS['w'] + 200
RS['docH'] = RS['h'] + 200
def makeDocument():
    
    template = Template(RS)
    template.grid(RS)
    template.baselineGrid(RS)
    cb = 3
    template.cRect(2, 1, 3, 1, RS, fill=(1, 0, 0))
    
    doc = Document(RS, pages=3, template=template)
    
    page = doc.pages[2]
    #page.style['w'] = 400
    #page.style['h'] = 200
        
    print doc.pages
    page.cRect(1, 1, cb, 1, RS, fill=(0, 0.5, 0))
    for pageNumber in doc.pages:
            page = doc.pages[pageNumber] # get this page
            # Add box with page number
            page.cText('Page %s' % pageNumber, 8, 2, 1, 1, RS, 
                textColor =0, fontSize=32)
            page.cText('Hallo', 4, 1, cb, 1, textColor=RED)
            
    return doc

d = makeDocument()
d.export('export//FaceBookBanner.pdf')


