from tkinter import *

class Ctxt(Text): 
    # Custom Text Widget with Highlight Pattern   - - - - -
    # Credits to the owner of this custom class - - - - - - - - - - - - -
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)
        count = IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Root Window Creation  - - - -
root = Tk()
root.geometry("320x240")
root.title("Sample GUI")
# - - - - - - - - - - - - - - -


# Text Widget - - - - - - - - - - - - - - -
Wtxt = Ctxt(root)
Wtxt.pack(expand = True, fill= BOTH)
Wtxt.insert("1.0","red read rid ready readily")
# - - - - - - - - - - - - - - - - - - - - -

# Highlight pattern - - - - - - - - -
Wtxt.tag_config('green', foreground="green")
Wtxt.highlight_pattern('\mread\M','green', regexp=True)



# Mainloop  -
mainloop()
# - - - - - -