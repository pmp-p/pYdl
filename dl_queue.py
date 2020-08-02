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
import gettext
from configuration import *
from structures import *
import datetime
import subprocess
from time import strftime

fr = gettext.translation('base', localedir=repertoire_script + 'locales', languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext

class dl_queue(Toplevel):
    ''' Interface graphique ...
    '''
    def __init__(self, debug = False):
        Toplevel.__init__(self)
        self.debug = debug
        self.Tdl_list = []
        self.interval = 60000
        self.after(self.interval, self.check_queue)
    
    def interface(self):
        ''' Interface de la fenêtre
        '''
        self.title(_('pYdl - Serveur'))
        self.iconphoto(False, PhotoImage(file=f'{repertoire_script}images{os.sep}icone.png'))
        self.geometry('400x200')
    
    def run(self):
        self.interface()
        
    def add_tdl(self, download):
        self.Tdl_list.append(download)
        
    def check_queue(self):
        heure = int(datetime.datetime.now().strftime('%H'))
        if (heure >= h_dep) and (heure <= h_fin):
            
            # Suppression des téléchargement obsolètes
            for download in self.Tdl_list:
                if (download.date_exp - datetime.datetime.now()).total_seconds() < 0:
                    # Download time expired or download done
                    self.Tdl_list.remove(download)
            
            # Lancement des téléchargements
            for download in self.Tdl_list:
                if (download.date_cre - datetime.datetime.now()).total_seconds() < 0:
                    self.letsdl_fake(download)
                    self.Tdl_list.remove(download)
        
        self.after(self.interval, self.check_queue)
    
    def letsdl_fake(self, download):
        print(f'{download.URL} est maintenant téléchargé')
    
    def letsdl(self, download):
        # Lancement de l'encodage
        # MP3 Version
        if download.is_audio:
            try:
                subprocess.call(f'{path_youtubedl} -q -x --audio-format mp3 {download.URL} -o \'{path_mp3}%(title)s.%(ext)s\'', shell = True)
            except:
                pass

        if download.is_video:
            # Video Version
            try:
                subprocess.call(f'{path_youtubedl} -q {download.URL} -o \'{path_videos}%(title)s.%(ext)s\'')
            except:
                pass

if __name__ == '__main__':
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state('icon')
    App = dl_queue()
    App.run()
    w.mainloop()
