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
    'SpreadBleed':     dict(ml=10, mr=10, mt=32, mb=30, aml=20, amb=40, afs=24, lw=80, lrm=10, ll=5, imx=0, imy=-200, imw=150),
    'FullPageBleed':   dict(ml=10, mr=10, mt=50, mb=60, aml=20, amb=30, afs=18, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=150),
    'FullPageA4':      dict(ml=10, mr=10, mt=40, mb=40, aml=25, amb=30, afs=18, lw=80, lrm=None, ll=5, imx=0, imy=0, imw=150),
    'Horizontal2_3':   dict(ml=0, mr=0, mt=20, mb=40, aml=40, amb=30, afs=18, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=130),
    'Horizontal1_3':   dict(ml=0, mr=0, mt=20, mb=20, aml=10, amb=30, afs=16, lw=50, lrm=5, ll=5, imx=0, imy=0, imw=180),    
    'Horizontal1_2':   dict(ml=0, mr=0, mt=20, mb=20, aml=20, amb=30, afs=18, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=140),
    'Horizontal1_4':   dict(ml=0, mr=0, mt=30, mb=40, aml=10, amb=30, afs=10, lw=45, lrm=3, ll=12, imx=0, imy=0, imw=220),
    'Vertical1_2':     dict(ml=0, mr=0, mt=20, mb=20, aml=20, amb=30, afs=18, lw=40, lrm=10, ll=5, imx=0, imy=0, imw=120),
    'Vertical1_4':     dict(ml=0, mr=0, mt=20, mb=20, aml=20, amb=30, afs=18, lw=40, lrm=10, ll=5, imx=0, imy=0, imw=120),
    'Horizontal1_8':   dict(ml=0, mr=0, mt=40, mb=40, aml=20, amb=30, afs=18, lw=50, lrm=10, ll=5, imx=0, imy=0, imw=300),
    'VogueMagazine':   dict(ml=10, mr=10, mt=40, mb=40, aml=20, amb=30, afs=18, lw=80, lrm=10, ll=5, imx=0, imy=0, imw=130),       
}
