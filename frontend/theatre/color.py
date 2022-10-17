class COLOR:
    class UI:
        TEXT = "#050505"
        OUTLINE = "#101010"

    BACKGROUND = "#323232"
    UI_TEXT = "#050505"
    UI_BACKGROUND = "#323296"
    UI_HIGHLIGHT = "#329696"
    UI_SELECT = "#963296"
    UI_DISABLE = "#969696"
    UI_WARN = "#963232"
    GOOD = "#"
    BAD = "#"
    NEUTRAL = "#"


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

    GREEN   = "#00a000"
    BLUE    = "#0000a0"
    MAGENTA = "#a000a0"
    YELLOW  = "#a0a000"
    CYAN    = "#00a0a0"

    def __getitem__(self, key):
        return getattr(self, key, "#000000")
