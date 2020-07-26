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
from peewee import *
from db_model import *
from configuration import *
import codecs
import os
import gettext

fr = gettext.translation('base', localedir=repertoire_script + 'locales', languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext

class AppBookmark(Toplevel):
    ''' Interface graphique ...
    '''
    def __init__(self, master, debug = False, langue = 'FRE', traduction = 'French Louis Segond', book = 1, chapitre = 1):
        Toplevel.__init__(self)
        self.debug = debug
    
    def interface(self):
        ''' Interface de la fenêtre
        '''
        self.title(_('Marque Pages'))

        ''' Implantation des composants
        '''

        
        ''' Binding
        '''
    
    def run(self):
        self.interface()

if __name__ == '__main__':
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state('icon')
    App = AppBookmark(w)
    App.run()
    w.mainloop()
