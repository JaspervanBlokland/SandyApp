# Example responsive facebook banner 

from pagebot.style import getRootStyle
from pagebot.document import Document 
from pagebot.page import Page 

mm = 25.4 / 72

SHOWGRID = True
SHOW_GRID_COLUMNS = True
template = 
RS  = getRootStyle(
    w = 851, h = 313)
    

def makedocument():
    print 'hallo'
    doc = Document(RS, pages = 4, )
    return doc
    
d = makedocument()
d.export('_export/facebookbanner.pdf')    