# -*- coding: utf-8 -*-
# ====================================================================
# Copyright (c) 2009-2010 Open Source Applications Foundation.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
# ====================================================================
#

import sys, os

from unittest import TestCase, main
from icu import *


class TestNormalizer2(TestCase):

    def testNormalize(self):

        try:
            from icu import Normalizer2
        except ImportError:
            return

        normalizer = Normalizer2.getInstance(None, "nfkc_cf",
                                             UNormalizationMode2.COMPOSE)

        self.assertTrue(normalizer.normalize("Hi There") == u'hi there')

        a = UnicodeString()
        normalizer.normalize("Hi There", a)
        self.assertTrue(a == UnicodeString(u'hi there'))

    def testNormalizeNFC(self):

        try:
            from icu import Normalizer2
        except ImportError:
            return

        normalizer = Normalizer2.getNFCInstance()

        self.assertTrue(normalizer.normalize("Hi There") == u'Hi There')

        a = UnicodeString()
        normalizer.normalize("Hi There", a)
        self.assertTrue(a == UnicodeString(U'Hi There'))

    def testNormalizeNFD(self):

        try:
            from icu import Normalizer2
        except ImportError:
            return

        normalizer = Normalizer2.getNFDInstance()

        self.assertTrue(normalizer.normalize("Hi There") == u'Hi There')

        a = UnicodeString()
        normalizer.normalize("Hi There", a)
        self.assertTrue(a == UnicodeString(U'Hi There'))

    def testNormalizeNFKC(self):

        try:
            from icu import Normalizer2
        except ImportError:
            return

        normalizer = Normalizer2.getNFKCInstance()

        self.assertTrue(normalizer.normalize("Hi There") == u'Hi There')

        a = UnicodeString()
        normalizer.normalize("Hi There", a)
        self.assertTrue(a == UnicodeString(U'Hi There'))

    def testNormalizeNFKD(self):

        try:
            from icu import Normalizer2
        except ImportError:
            return

        normalizer = Normalizer2.getNFKDInstance()

        self.assertTrue(normalizer.normalize("Hi There") == u'Hi There')

        a = UnicodeString()
        normalizer.normalize("Hi There", a)
        self.assertTrue(a == UnicodeString(U'Hi There'))

    def testNormalizeNFKCCasefold(self):

        try:
            from icu import Normalizer2
        except ImportError:
            return

        normalizer = Normalizer2.getNFKCCasefoldInstance()

        self.assertTrue(normalizer.normalize("Hi There") == u'hi there')

        a = UnicodeString()
        normalizer.normalize("Hi There", a)
        self.assertTrue(a == UnicodeString(U'hi there'))


if __name__ == "__main__":
    main()
