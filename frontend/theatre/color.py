class COLOR:
    class UI:
        TEXT        = "#080808"
        OUTLINE     = "#181818"
        BACKGROUND  = "#101010"


    # Playercolors
    GRAYl2      = "#e0e0e0"
    GRAYl1      = "#c0c0c0"
    GRAY        = "#a0a0a0"
    GRAYd1      = "#808080"
    GRAYd2      = "#606060"

    REDl2       = "#e00000"
    REDl1       = "#c00000"
    RED         = "#a00000"
    REDd1       = "#800000"
    REDd2       = "#600000"

    GREENl2     = "#00e000"
    GREENl1     = "#00c000"
    GREEN       = "#00a000"
    GREENd1     = "#008000"
    GREENd2     = "#006000"

    BLUEl2      = "#0000e0"
    BLUEl1      = "#0000c0"
    BLUE        = "#0000a0"
    BLUEd1      = "#000080"
    BLUEd2      = "#000060"

    MAGENTAl2   = "#e000e0"
    MAGENTAl1   = "#c000c0"
    MAGENTA     = "#a000a0"
    MAGENTAd1   = "#800080"
    MAGENTAd2   = "#600060"

    YELLOWl2    = "#e0e000"
    YELLOWl1    = "#c0c000"
    YELLOW      = "#a0a000"
    YELLOWd1    = "#808000"
    YELLOWd2    = "#606000"

    CYANl2      = "#00e0e0"
    CYANl1      = "#00c0c0"
    CYAN        = "#00a0a0"
    CYANd1      = "#008080"
    CYANd2      = "#006060"

    BLACKl2      = "#c0c0c0"
    BLACKl1      = "#a0a0a0"
    BLACK        = "#808080"
    BLACKd1      = "#606060"
    BLACKd2      = "#202020"

    def __getitem__(self, key):
        return getattr(self, key, "#000000")
