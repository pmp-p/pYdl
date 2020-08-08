# -*- coding:utf-8 -*-
#
# Copyright © 2020 cGIfl300
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the “Software”),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from tkinter import *
from .structures import *
from .configuration import *
import datetime
from .image_set import image_set
import os


class dl(Label):
    """ Interface graphique ...
    """

    def __init__(self, debug=False, master=None, tdl=Tdl()):
        Label.__init__(self, master)
        self.debug = debug
        self.master = master
        self.tdl = tdl
        self.config(bg=couleur_fond, fg=couleur_texte)

    def interface(self):
        """ Interface du widget
        """
        if self.tdl.is_active:
            self.img_status = image_set(self, f"images{os.sep}point_vert", expand_=False)
        else:
            self.img_status = image_set(self, f"images{os.sep}point_rouge", expand_=False)
        self.lbl_dl = Label(self, bg=couleur_fond, fg=couleur_texte, text=self.tdl.URL)

        """ Implantation des composants
        """
        self.lbl_dl.pack(expand=True, fill=BOTH)

    def run(self):
        self.interface()


if __name__ == "__main__":
    w = Tk()
    w.after(30000, w.destroy)
    w.geometry("400x200")
    a_charger = Tdl()
    a_charger.is_audio = True
    a_charger.is_video = True
    a_charger.date_cre = datetime.datetime.now()
    a_charger.date_exp = datetime.datetime.now() + datetime.timedelta(1)
    a_charger.URL = "essai dl"
    App = dl(master=w, tdl=a_charger)
    App.run()
    App.pack(fill=BOTH)
    w.mainloop()
