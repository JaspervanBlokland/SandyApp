# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#
#     CartierMagazine.py
#
from __future__ import division
from datetime import datetime # Make date on magazine cover fit today.

import pagebot
from pagebot import newFS, Gradient, Shadow
from pagebot.style import getRootStyle, CENTER, LEFT, TOP, RIGHT, A4Letter
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.document import Document
from pagebot.composer import Composer
from pagebot.typesetter import Typesetter
from pagebot.toolbox.transformer import s2Color, int2Color, lighter
# Import other than default view class, showing double pages spread
from pagebot.elements.views.spreadview import SpreadView

from pagebot.fonttoolbox.variablefontbuilder import getVariableFont, Font 
PageWidth = 800
PageHeight = 1018

PADDING = (24, 24, 20, 24) # General page padding.

EXPORT_PATH = '_export/CartierMagazineCover.png' # Export path of the document.
COVER_IMAGE_PATH1 = '../AdsProject/content/cartier/beeld.jpg' # Path of the cover image.

# Use this color to show "error" debugging, e.g. to show bounding box of an element.
debugColor = (1, 1, 0, 0.5)

# Set some values of the default template (as already generated by the document).
# Make squential unique names for the flow boxes inside the templates
MAIN_FLOW = 'main' # ELement id of the text box on pages the hold the main text flow.
FLOWID1 = MAIN_FLOW+'1' 
FLOWID2 = MAIN_FLOW+'2'
FLOWID3 = MAIN_FLOW+'3'

# Get the root path of open source fonts, enclosed in PageBot.
ROOT_PATH = pagebot.getRootPath()
# Main Variable Font for all text in the magazine. Change this line to build with
# another Variable Font. Using Optical Size (opsz), Weight (wght) and Width (wdth) axes.
FONT_PATH = ROOT_PATH + '/Fonts/fontbureau/AmstelvarAlpha-VF.ttf'

# Open the font, so we can query values that are not available in standard DrawBot functions,
# such as stem width, overshoot of roundings, etc.
f = Font(FONT_PATH)
#print f.axes Uncomment to see the available axes printed.

# Pre-calculate instances of locations in the Variable Font.
LIGHT72 = getVariableFont(FONT_PATH, dict(wght=0.5, wdth=0.6, opsz=72))
BOOK_LIGHT = getVariableFont(FONT_PATH, dict(wght=0.5, wdth=0.7))
BOOK_CONDENSED = getVariableFont(FONT_PATH, dict(wght=0.7, wdth=0.4))
BOOK = getVariableFont(FONT_PATH, dict(wght=0.25, wdth=0))
BOOK_ITALIC = getVariableFont(FONT_PATH, dict(wght=0.25, wdth=1))
MEDIUM = getVariableFont(FONT_PATH, dict(wght=0.40, wdth=0))
SEMIBOLD = getVariableFont(FONT_PATH, dict(wght=0.40, wdth=1))
SEMIBOLD_CONDENSED = getVariableFont(FONT_PATH, dict(wght=0.40, wdth=0.5))
BOLD = getVariableFont(FONT_PATH, dict(wght=0.70, wdth=1))
BOLD_ITALIC = getVariableFont(FONT_PATH, dict(wght=0.7, wdth=1))

shadow = Shadow(offset=(6, -6), blur=10, color=(0.2, 0.2, 0.2, 0.5))

def makeCoverTemplate(imagePath, w, h):
    print w, h, w/h

    bleed = 0
    textColor = 1
    # Make styles
    # TODO: Make this fit, using size/wdth axis combination of Amstelvar
    coverTitleSize = 160
    # Not optical size yet. Play more with the axes
    coverTitleFont = getVariableFont(FONT_PATH, 
        dict(wght=0.9, wdth=0.02))#, opsz=coverTitleSize))
    coverTitleStyle = dict(font=coverTitleFont.installedName, fontSize=coverTitleSize, 
        textShadow=shadow, textFill=textColor, tracking=-3)

    coverSubTitleSize = 80
    # Not optical size yet. Play more with the axes
    coverSubTitleFont = getVariableFont(FONT_PATH, dict(wght=0.6, wdth=0.02)) #opsz=coverSubTitleSize))
    coverSubTitleStyle = dict(font=coverSubTitleFont.installedName, fontSize=coverSubTitleSize,         
        textFill=(1, 1, 1, 0.8), tracking=0)

    # Cover
    coverTemplate = Template(w=w, h=h, padding=PADDING) # Cover template of the magazine.
    newImage(imagePath, z=10, parent=coverTemplate,
        h=PageHeight, conditions=[Top2TopSide(), Fit2WidthSides()])
    # Title of the magazine cover.
    coverTitle = newFS('Cartier', style=coverTitleStyle, w=PageWidth/2)
    tw, th = textSize(coverTitle)


    # Make actual date in top-right with magazine title. Draw a bit transparant on background photo.
    dt = datetime.now()
    d = dt.strftime("%B %Y")
    fs = newFS(d, style=dict(font=MEDIUM.installedName, fontSize=17,
        textFill=(1, 1, 1, 0.8), tracking=0.5))
    # TODO: padding righ could come from right stem of the "n"
    newTextBox(fs, parent=coverTemplate, xTextAlign=RIGHT, z=20, pr=10, pt=20, conditions=[Top2TopSide(), Right2Right()])


    # Calculate width if single "F" for now, to align "Magazine"
    # TODO: Change in example to go through the coverTitle to get positions and widths.        
    newText(coverTitle, parent=coverTemplate, z=20, pt=-20, 
        textShadow=shadow, conditions=[Right2Right(), Float2Top()])

    coversubTitle = newFS('Magazine', style=coverSubTitleStyle, w=PageWidth*0.4)
    tw, th = textSize(coverTitle)
    newTextBox(coversubTitle, parent=coverTemplate, pt=-th/3-20, z=20,
        xTextAlign=RIGHT, textShadow=shadow,
        conditions=[Right2Right(), Fit2Width(), Float2Top()])
    
    # Titles could come automatic from chapters in the magazine.
    fs = newFS('$6.95',  style=dict(font=BOOK.installedName, fontSize=12, 
        textFill=textColor, tracking=1, leading=12 ))
    newText(fs, parent=coverTemplate, mt=8, conditions=[Top2Bottom(), Right2Right()])
  
    makeCoverTitles(coverTemplate)
    
    return coverTemplate

def makeCoverTitles(coverTemplate):
    u"""Build the text box elements in the coverTemplate, containing the chapter titles
    of the magazine."""

    # TODO: Titles should come automatic from random blurb chapter titles in the magazine.
    pl = 8 # Generic offset as padding left from the page padding to aligh with cover title.
    fs = newFS('\n', style=dict(font=BOOK_CONDENSED.installedName, 
        fontSize=64, textFill=1, tracking=0.5, leading=0, rLeading=0.9))
    newTextBox(fs, z=20, pl=15, pt=60, parent=coverTemplate, 
        conditions=[Left2Left(), Fit2Width(), Float2Top()])
        
    # TODO: Titles should come automatic from random blurb chapter titles in the magazine.
    fs = newFS('Ideal style:\n', style=dict(font=MEDIUM.installedName, fontSize=32, 
        textFill=1, tracking=0.5, leading=50))
    fs += newFS('Diamond collection', style=dict(font=BOOK.installedName, 
        fontSize=45, textFill=1, tracking=0.5, leading=48))
    newTextBox(fs, z=20, pl=8, w=400, pt=0, parent=coverTemplate, 
        textShadow=shadow, 
        conditions=[Left2Left(), Float2Top()])
        
    # TODO: Titles should come automatic from random blurb chapter titles in the magazine.
    fs = newFS('Visit store\nP.C. Hooftstraat', style=dict(font=BOOK_LIGHT.installedName, 
        fontSize=72, textFill=1, tracking=0.5, leading=74))
    newTextBox(fs, z=20, pl=8, pt=40, parent=coverTemplate, 
        style=dict(shadowOffset=(4, -4), shadowBlur=20, shadowFill=(0,0,0,0.6)),
        textShadow=shadow, 
        conditions=[Left2Left(), Fit2Width(), Float2Top()])
      
    # TODO: Titles should come automatic from random blurb chapter titles in the magazine.
    c = (1, 0, 0, 0.7) #lighter(int2Color(0x99CBE9)) # Pick from light spot in the photo
    if PageWidth >= 500:
        s = 'Exclusive: '
    else:
        s = ''
    fs = newFS(s, style=dict(font=MEDIUM.installedName, fontSize=24, 
        textFill=c, tracking=0.5, lineHeight=34))
    fs += newFS('Necklace and bracelets ', style=dict(font=BOOK.installedName, 
        fontSize=24, textFill=c, tracking=0.5, lineHeight=34))
    newTextBox(fs, z=20, pl=pl, parent=coverTemplate, 
        style=dict(shadowOffset=(4, -4), shadowBlur=20, shadowFill=(0,0,0,0.6)),
        textShadow=shadow, 
        conditions=[Left2Left(), Fit2Width(), Float2Bottom()])
           
# -----------------------------------------------------------------         
def makeDocument():
    u"""Demo page composer."""
    W = PageWidth
    H = PageHeight
    coverTemplate1 = makeCoverTemplate(COVER_IMAGE_PATH1, W, H)
       
    # Create new document with (w,h) and fixed amount of pages.
    # Make number of pages with default document size, start a page=1 to make SpreadView work.
    # Initially make all pages default with template2.
    # Oversized document (docW, docH) is defined in the rootStyle.
    doc = Document(title=EXPORT_PATH, w=W, h=H, autoPages=1, originTop=False,
        template=coverTemplate1, startPage=1) 
 
    # TODO Will be expanded with more pages later.
    view = doc.getView()
    #view = SpreadView(parent=doc) # Show as spread, not a single pages.
    view.padding = 0
    view.showPageCropMarks = True
    view.showPageRegistrationMarks = True
    view.showPageFrame = False
    view.showPagePadding = False
    view.showElementOrigin = False
    view.showElementDimensions = False
    
    # Change template of page 1
    page1 = doc[0]
    page1.applyTemplate(coverTemplate1)
        
    doc.solve()
    
    return doc

Variable([
    #dict(name='ElementOrigin', ui='CheckBox', args=dict(value=False)),
    dict(name='PageWidth', ui='Slider', args=dict(minValue=349, value=800, maxValue=800)),
    dict(name='PageHeight', ui='Slider', args=dict(minValue=242, value=1018, maxValue=1018)),
], globals())

d = makeDocument()
d.export(EXPORT_PATH) 

