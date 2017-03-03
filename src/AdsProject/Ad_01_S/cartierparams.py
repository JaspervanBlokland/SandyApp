from pagebot.style import MM

AD_PARAMS = { # Values in millmeters
    # mr = Margin right
    # ml = Margin left
    # mt = Margin top
    # mb = Margin bottom
    # lw = Logo width
    # ll = Logo leading
    # lrm = Logo right margin
    # imx = Image origin x
    # imy = Image origin y
    # imw = Image origin width
    # aml = Address margin left
    # amb = Address margin bottom
    # afs = Address font size
    # dml = Diamond margin left
    # dmb = Diamond margin bottom
    #
    # imw == None --> Don't show image
    # lrm == None --> Center logo
    #
    'SpreadBleed':     dict(ml=10, mr=10, mt=20, mb=40, 
        aml=27, amb=30, afs=18, dml=40, dmb=30, lw=100, lrm=10, ll=-17, imx=0, imy=-130, imw=150),    'FullPageBleed':   dict(ml=10, mr=10, mt=20, mb=30, 
        aml=30, amb=33, afs=12, lw=70, lrm=10, ll=-8, imx=10, imy=0, imw=111),    'FullPageA4':      dict(ml=10, mr=10, mt=20, mb=30, 
        aml=30, amb=33, afs=12, lw=70, lrm=10, ll=-9, imx=10, imy=0, imw=110),    'Horizontal2_3':   dict(ml=0, mr=0, mt=10, mb=30, 
        aml=30, amb=10, afs=10, lw=65, lrm=10, ll=-15, imx=0, imy=0, imw=120),    'Horizontal1_3':   dict(ml=0, mr=0, mt=20, mb=30, 
        aml=5, amb=30, afs=8, lw=50, lrm=None, ll=0, imx=-40, imy=0, imw=220),    
    'Horizontal1_2':   dict(ml=0, mr=0, mt=20, mb=20, 
        aml=5, amb=30, afs=10, lw=50, lrm=5, ll=2, imx=0, imy=0, imw=100),    'Horizontal1_4':   dict(ml=0, mr=0, mt=20, mb=20, 
        aml=5, amb=30, afs=6, lw=40, lrm=None, ll=5, imx=-30, imy=0, imw=240),    'Vertical1_2':     dict(ml=5, mr=5, mt=20, mb=20, 
        aml=14, amb=33, afs=12, lw=50, lrm=5, ll=3, imx=0, imy=-50, imw=104),    'Vertical1_4':     dict(ml=5, mr=5, mt=20, mb=20, 
        aml=10, amb=35, afs=8, lw=40, lrm=None, ll=5, imx=5, imy=-10, imw=100),    'Horizontal1_8':   dict(ml=0, mr=0, mt=40, mb=40, 
        aml=0, amb=10, afs=6, lw=40, lrm=None, ll=5, imx=0, imy=0, imw=None),    'VogueMagazine':   dict(ml=10, mr=10, mt=20, mb=30, 
        aml=30, amb=33, afs=12, lw=70, lrm=10, ll=-9, imx=10, imy=0, imw=100),       
}
