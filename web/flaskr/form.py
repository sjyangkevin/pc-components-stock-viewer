from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from wtforms.validators import Optional

class FilterForm(FlaskForm):
    source_bestbuy = BooleanField("Best Buy",validators=[Optional()])
    source_canadacomputers = BooleanField("Canada Computers",validators=[Optional()])
    source_newegg = BooleanField("Newegg",validators=[Optional()])

    GeForce_RTX_4090 = BooleanField("GeForce RTX 4090", validators=[Optional()])
    GeForce_RTX_4080 = BooleanField("GeForce RTX 4080", validators=[Optional()])
    GeForce_RTX_3090 = BooleanField("GeForce RTX 3090", validators=[Optional()])
    GeForce_RTX_3080_Ti = BooleanField("GeForce RTX 3080 Ti", validators=[Optional()])
    GeForce_RTX_3080 = BooleanField("GeForce RTX 3080", validators=[Optional()])
    GeForce_RTX_3070_Ti = BooleanField("GeForce RTX 3070 Ti", validators=[Optional()])
    GeForce_RTX_3070 = BooleanField("GeForce RTX 3070", validators=[Optional()]) 
    GeForce_RTX_3060_Ti = BooleanField("GeForce RTX 3060 Ti", validators=[Optional()]) 
    GeForce_RTX_3060 = BooleanField("GeForce RTX 3060", validators=[Optional()]) 
    GeForce_RTX_3050 = BooleanField("GeForce RTX 3050", validators=[Optional()]) 
    GeForce_RTX_2060_Super = BooleanField("GeForce RTX 2060 Super", validators=[Optional()]) 
    GeForce_RTX_2060 = BooleanField("GeForce RTX 2060", validators=[Optional()]) 
    GeForce_GTX_1660_Ti = BooleanField("GeForce GTX 1660 Ti", validators=[Optional()]) 
    GeForce_GTX_1660_Super = BooleanField("GeForce GTX 1660 Super", validators=[Optional()]) 
    GeForce_GTX_1660 = BooleanField("GeForce GTX 1660", validators=[Optional()])
    GeForce_GTX_1650_Super = BooleanField("GeForce GTX 1650 Super", validators=[Optional()]) 
    GeForce_GTX_1650 = BooleanField("GeForce GTX 1650", validators=[Optional()])
    GeForce_GTX_1000_Series = BooleanField("GeForce GTX 1000 Series", validators=[Optional()]) 
    Radeon_RX_7900_XTX = BooleanField("Radeon RX 7900 XTX", validators=[Optional()]) 
    Radeon_RX_6900_6950_XT = BooleanField("Radeon RX 6900/6950 XT", validators=[Optional()]) 
    Radeon_RX_6800_XT = BooleanField("Radeon RX 6800 XT", validators=[Optional()]) 
    Radeon_RX_6800 = BooleanField("Radeon RX 6800", validators=[Optional()]) 
    Radeon_RX_6700_6750_XT = BooleanField("Radeon RX 6700/6750 XT", validators=[Optional()]) 
    Radeon_RX_6600_6650_XT = BooleanField("Radeon RX 6600/6650 XT", validators=[Optional()]) 
    Radeon_RX_6600 = BooleanField("Radeon RX 6600", validators=[Optional()]) 
    Radeon_RX_6500_XT = BooleanField("Radeon RX 6500 XT", validators=[Optional()])

    ASRock = BooleanField("ASRock", validators=[Optional()])
    ASUS = BooleanField("ASUS", validators=[Optional()])
    CornElectronics = BooleanField("Corn Electronics", validators=[Optional()])
    EVGA = BooleanField("EVGA", validators=[Optional()])
    GIGABYTE = BooleanField("GIGABYTE", validators=[Optional()])
    HP = BooleanField("HP", validators=[Optional()])
    INTEL = BooleanField("Intel", validators=[Optional()])
    MAXSUN = BooleanField("MAXSUN", validators=[Optional()])
    MSI = BooleanField("MSI", validators=[Optional()])
    NVIDIA = BooleanField("NVIDIA", validators=[Optional()])
    PNY = BooleanField("PNY", validators=[Optional()])
    SAPPHIRE = BooleanField("Sapphire", validators=[Optional()])
    VisionTek = BooleanField("VisionTek", validators=[Optional()])
    ZOTAC = BooleanField("ZOTAC", validators=[Optional()])
    POWERCOLOR = BooleanField("PowerColor", validators=[Optional()])
    yeston = BooleanField("yeston", validators=[Optional()])

    submit = SubmitField("Apply")