# 
#    Example Poster Identity
#
# Create a RootStyle instance by calling function. Alter some of the default values
# on initialization, so we don't that to replace them later for our version of the 
# root style.

from datetime import datetime # Make date fit today.

from pagebot.style import getRootStyle, makeStyle, MM, CENTER, NO_COLOR
# Document is the main instance holding all information about the document togethers (pages, styles, etc.)
from pagebot import newFS
from pagebot.document import Document
from pagebot.elements import Template

SHOW_GRID = False
SHOW_GRID_COLUMNS = False
SHOW_BASELINE_GRID = False

W = 520
H = 700

OVER_FILL = 0*MM # Overfill on cutting 

RS = getRootStyle(
    w=W, h=H, 
    showGrid=SHOW_GRID, 
    showGridColumns=SHOW_GRID_COLUMNS,
    showBaselineGrid = SHOW_BASELINE_GRID,
)
RS['docW'] = W + 200
RS['docH'] = H + 200

COLUMNS = 12
GUTTER = 2
TITLE = 'Pirates of the Caribbean'
CREDITS = 'Film by Andrew Clime'
URL = 'www.loganshort.com'

def drawBackground(page):
    page.rect(-OVER_FILL, -OVER_FILL, 
        page.style['w']+2*OVER_FILL, 
        page.style['h']+2*OVER_FILL, 
        fill=(0.11, 0.11, 0.22))

def drawImage(template, path, x, y, w, align, vAlign):
    template.image(path, x, y, w=w, align=align, vAlign=vAlign)

def drawDate(template, x, y, dateString, align):
    style = makeStyle(template.style, align=align, fontSize=25, 
        font='Antenna-ExtraLight', textFill=1)
    fs = newFS(dateString, style);
    template.text(fs, x, y, style=style) 

def drawTitle(template, x, y, w, title, align):
    fontSize = 50
    style = makeStyle(template.style, align=align, fontSize=fontSize, fill=NO_COLOR, font='Antenna-Black', textFill=1, leading=fontSize*1.1)
    fs = getFormattedString(title, style);
    template.textBox(fs, x, y, w=w,
        h=fontSize*3, style=style) 

def drawCredits(template, x, y, w, title, align):
    fontSize = 25
    style = makeStyle(template.style, align=align, fontSize=fontSize, fill=NO_COLOR, font='Antenna-Thin', textFill=1, leading=fontSize*1.1)
    fs = getFormattedString(title, style);
    template.textBox(fs, x, y, w=w,
        h=fontSize*3, style=style) 

def drawURL(template, x, y, w, title, align):
    fontSize = 20
    style = makeStyle(template.style, align=align, fontSize=fontSize, fill=NO_COLOR, font='Antenna-Medium', textFill=1, leading=fontSize*1.1)
    fs = getFormattedString(title, style);
    template.textBox(fs, x, y, w=w,
        h=fontSize*3, style=style) 

def makeDocument():
    
    column = (RS['w'] - (COLUMNS-1)*GUTTER)/COLUMNS
    gutter = GUTTER
    
    template = Template(RS) # Create template of main size. Front page only.
    # Show grid columns and margins if rootStyle.showGrid or rootStyle.showGridColumns are True
    template.grid(RS) 
    
    # Show baseline grid if rs.showBaselineGrid is True
    # Create empty image place holders. To be filled by running content on the page.
    #template.cContainer(2, -0.7, 5, 4, rs)  # Empty image element, cx, cy, cw, ch
    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size.
    # Initially make all pages default with template2
    doc = Document(RS, pages=1, template=template) 
    for n in range(30):
        page = doc.newPage(w=template.style['w']+n*20)
        drawBackground(page)
        drawImage(page, 'images/coin_1.png', 
            template.style['w']/2, 280,
            w=template.style['w']/1.5,
            align=CENTER, vAlign=CENTER)
        # Calculate date 2 weeks from now
        dt = datetime.now()
        d = dt.strftime("%d|%m|%y") # Make formatted string from date.
        drawDate(page, page.style['w']/2, template.style['h']-50, 
            d, CENTER)
        drawTitle(page, page.style['w']/2, 120, 
            template.style['w'] - 2*column-2*gutter,
            TITLE, CENTER)
        drawCredits(page, page.style['w']/2, 60, 
            template.style['w'] - 2*column-2*gutter,
            CREDITS, CENTER)
        drawURL(page, page.style['w']/2, 40, 
            template.style['w'] - 2*column-2*gutter,
            URL, CENTER)


    return doc
    
d = makeDocument()
d.export('_export/PosterIdentity.gif')


