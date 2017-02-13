# 
#    Example responsive FaceBook Banner
#
# Create a RootStyle instance by calling function. Alter some of the default values
# on initialization, so we don't that to replace them later for our version of the 
# root style.

from pagebot import getFormattedString
from pagebot.style import getRootStyle, MM
# Document is the main instance holding all information about the document togethers (pages, styles, etc.)
from pagebot.document import Document
from pagebot.page import Template

import pagesizes
reload(pagesizes)
from pagesizes import pageSizes

import cartierparams
reload(cartierparams)
from cartierparams import AD_PARAMS

#    Cartier ads

SHOW_GRID = True
SHOW_GRID_COLUMNS = True
SHOW_BASELINE_GRID = False

def getStyle(W, H):
    rs= getRootStyle(
        w=W, h=H, # Default 851 x 313
        showGrid=SHOW_GRID, 
        showGridColumns=SHOW_GRID_COLUMNS,
        showBaselineGrid = SHOW_BASELINE_GRID,
        )
    FONT_SIZE = 24
    rs['fontSize'] = FONT_SIZE
    rs['baselineGrid'] = FONT_SIZE * 1.2
    rs['docW'] = rs['w'] + 0
    rs['docH'] = rs['h'] + 0
    return rs
    
imagePath = '../content/cartier/beeld.jpg'
logoPath = '../content/cartier/Cartier.pdf'

ADDRESS = 'Adres van Cartier Xxxxxxxx'

def makeAd(pageSizeName):
    w, h = pageSizes[pageSizeName]
    d = AD_PARAMS[pageSizeName]
    RS = getStyle(w, h)
    template = Template(RS) # Create template of main size. Front page only.

    maskWidth = w - d['mr']*MM - d['ml']*MM
    maskHeight = h - d['mt']*MM - d['mb']*MM
    logoWidth = d['lw']*MM
    logoRightMargin = d['lrm']
    if d['lrm'] is None:
        logoX = w/2 - logoWidth/2
    else:
        logoX = w-d['lrm']*MM-logoWidth
        
    if d['imw'] is not None:
        template.image(imagePath, d['imx']*MM, d['imy']*MM, 
        w=d['imw']/100.0*maskWidth, style=RS,
        clipRect=(d['ml']*MM, d['mt']*MM, maskWidth, maskHeight))
    
    template.image(logoPath, logoX, h-d['mt']*MM+d['ll']*MM, 
        w=logoWidth, style=RS)

    address = getFormattedString(ADDRESS, dict(font='Georgia', fontSize=d['afs']))
    template.text(address, d['aml'], d['amb']) 
    
    doc = Document(RS, pages=1, template=template) 
    
    page = doc.pages[1]
        
    return doc 

def makeAds():
    for pageSizeName in pageSizes:
        doc = makeAd(pageSizeName)
        doc.export('_export/%s.pdf' % pageSizeName, multiPage=False)
       
makeAds()


