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
from configuration import *
from peewee import *
import pygame
import gettext

fr = gettext.translation('base', localedir=repertoire_script + 'locales', languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext

pygame.init()

class pYdl(Tk):
    ''' Interface graphique ...
    '''
    def __init__(self, debug = False):
        Tk.__init__(self)
        self.debug = debug
    
    def interface(self):
        ''' Interface de la fenêtre
        '''
        self.title(_('pYdl'))
        
        self.panel_001 = Label(self,
                               bg = couleur_fond)
        self.panel_002 = Label(self,
                               bg = couleur_fond)
        
        self.txt_url = Label(self.panel_002,
                             text = _('URL'),
                             bg = couleur_fond,
                             fg = couleur_texte)
        self.entry_url = Entry(self.panel_002,
                               bg = couleur_fond_saisie,
                               fg = couleur_texte_saisie)
        
        ''' Implantation des composants
        '''
        self.panel_001.pack(expand = True,
                            fill = BOTH)
        self.panel_002.pack(expand = True,
                            fill = BOTH)
        self.txt_url.pack(expand = True,
                          fill = BOTH,
                          side = LEFT)
        self.entry_url.pack(expand = True,
                            fill = BOTH)
        
        ''' Binding
        '''
    
    def run(self):
        self.interface()
        self.mainloop()

if __name__ == '__main__':
    App = pYdl(debug = True)
    App.run()
