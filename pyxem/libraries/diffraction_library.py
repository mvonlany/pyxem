# -*- coding: utf-8 -*-
# Copyright 2017-2018 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.

import pyxem as pxm
import pickle

def load_DiffractionLibrary(filename,safety=False):
    if safety:
        with open(filename, 'rb') as handle:
            return pickle.load(handle)
    else:
        raise RuntimeError('Unpickling is risky, turn safety to True if \
        trust the author of this content')


class DiffractionLibrary(dict):
    """Maps crystal structure (phase) and orientation (Euler angles or
    axis-angle pair) to simulated diffraction data.
    """

    def get_library_entry(self,phase=None,angle=None):
        """ Extracts a single library entry for viewing,
        unspecified layers of dict are selected randomly and so this method
        is not entirely repeatable


        Parameters
        ----------

        Phase : Label for the Phase you are interested in. Randomly chosen
        if False
        Angle : Label for the Angle you are interested in. Randomly chosen
        if False

        """

        if phase is not None:
            if angle is not None:
                return self[phase][angle]
            else:
                for rotation in self[phase].keys():
                    return self[phase][rotation]
        else:
            for phase in self.keys():
                for rotation in self[phase].keys():
                    return self[phase][rotation]



    def pickle_library(self,filename):
        with open(filename, 'wb') as handle:
            pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)
