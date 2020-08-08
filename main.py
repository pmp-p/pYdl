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


import gettext
import os
import subprocess
import datetime

from tkinter import *

from .configuration import *
from .structures import *

from .image_set import image_set
from .dl_queue import dl_queue


fr = gettext.translation("base", localedir=repertoire_script + "locales", languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext


class pYdl(Tk):
    """ Interface graphique ...
    """

    def __init__(self, debug=False):
        Tk.__init__(self)
        self.debug = debug
        self.is_audio_value = IntVar()
        self.is_video_value = IntVar()

    def interface(self):
        """ Interface de la fenêtre
        """
        self.dl_queue = dl_queue()
        self.dl_queue.run()

        self.title(_("pYdl"))
        self.iconphoto(False, PhotoImage(file=f"{repertoire_script}images{os.sep}icone.png"))

        self.panel_001 = Label(self, bg=couleur_fond)
        self.panel_002 = Label(self, bg=couleur_fond)
        self.panel_003 = Label(self, bg=couleur_fond)

        self.txt_url = Label(self.panel_002, text=_("URL"), bg=couleur_fond, fg=couleur_texte)
        self.entry_url = Entry(self.panel_002, bg=couleur_fond_saisie, fg=couleur_texte_saisie)

        self.is_audio = Checkbutton(
            self.panel_002,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            activebackground=couleur_texte_saisie,
            activeforeground=couleur_fond_saisie,
            variable=self.is_audio_value,
            text=_("Capturer Audio"),
        )
        self.is_video = Checkbutton(
            self.panel_002,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            activebackground=couleur_texte_saisie,
            activeforeground=couleur_fond_saisie,
            variable=self.is_video_value,
            text=_("Capturer Vidéo"),
        )

        self.btn_001 = Button(
            self.panel_003,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            activebackground=couleur_texte_saisie,
            activeforeground=couleur_fond_saisie,
            text=_("C'est parti !"),
            command=self.letsgo,
        )

        self.entete = image_set(self.panel_001, f"images{os.sep}logo-small")

        """ Implantation des composants
        """
        self.panel_001.pack(expand=True, fill=BOTH)
        self.panel_002.pack(expand=True, fill=BOTH)
        self.panel_003.pack(expand=True, fill=BOTH)
        self.txt_url.pack(expand=True, fill=BOTH)
        self.entry_url.pack(expand=True, fill=BOTH)
        self.is_audio.pack(expand=True, fill=BOTH, side=LEFT)
        self.is_video.pack(expand=True, fill=BOTH)
        self.btn_001.pack(expand=True, fill=BOTH)

        """ Initialise widgets values
        """
        self.is_audio_value.set("1")
        self.is_video_value.set("1")

        """ Binding
        """

        # No binding needed for this app

    def letsgo(self):
        self.entry_url.config(state=DISABLED)
        self.btn_001.config(state=DISABLED)
        self.is_audio.config(state=DISABLED)
        self.is_video.config(state=DISABLED)

        a_charger = Tdl()
        if self.is_audio_value.get() == 1:
            a_charger.is_audio = True
        if self.is_video_value.get() == 1:
            a_charger.is_video = True
        a_charger.date_cre = datetime.datetime.now()
        a_charger.date_exp = datetime.datetime.now() + datetime.timedelta(1)
        a_charger.URL = self.entry_url.get()
        self.dl_queue.add_tdl(a_charger)

        self.entry_url.config(state=NORMAL)
        self.btn_001.config(state=NORMAL)
        self.is_audio.config(state=NORMAL)
        self.is_video.config(state=NORMAL)
        self.entry_url.delete("0", "end")

    def run(self):
        self.interface()
        self.mainloop()


if __name__ == "__main__":
    App = pYdl(debug=True)
    App.run()
