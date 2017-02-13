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
    #
    # imw == None --> Don't show image
    # lrm == None --> Center logo
    #
    'SpreadBleed':     dict(ml=0, mr=0, mt=20, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=None, ll=5, imx=0, imy=-200, imw=150),
    'FullPageBleed':   dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=100),
    'FullPageA4':      dict(ml=0, mr=0, mt=40, mb=40, aml=25, amb=30, afs=24, lw=80, lrm=None, ll=5, imx=0, imy=0, imw=100),
    'Horizontal2_3':   dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=100),
    'Horizontal1_3':   dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=100),    
    'Horizontal1_2':   dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=100),
    'Horizontal1_4':   dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=100),
    'Vertical1_2':     dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=100),
    'Vertical1_4':     dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=100),
    'Horizontal1_8':   dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=50, lrm=10, ll=5, imx=0, imy=0, imw=None),
    'VogueMagazine':   dict(ml=0, mr=0, mt=40, mb=40, aml=5, amb=10, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=100),       
}
