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

import os

chemin_script = os.path.abspath(__file__)
repertoire_script = chemin_script[: next(i for i in reversed(range(len(chemin_script))) if chemin_script[i] == os.path.sep) + 1]
couleur_fond = "black"
couleur_texte = "green"
couleur_fond_saisie = "black"
couleur_texte_saisie = "green"
couleur_activebackground = couleur_texte_saisie
couleur_activeforeground = couleur_fond_saisie
debug = True
langue_appli = "fr"

path_youtubedl = "youtube-dl"
path_mp3 = repertoire_script + f"data{os.sep}"
path_videos = repertoire_script + f"data{os.sep}"

h_dep = 0
h_fin = 23
