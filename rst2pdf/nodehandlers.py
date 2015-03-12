# -*- coding: utf-8 -*-
# See LICENSE.txt for licensing terms
#$URL: http://rst2pdf.googlecode.com/svn/trunk/rst2pdf/nodehandlers.py $
#$Date: 2012-02-29 00:07:21 +0000 (Wed, 29 Feb 2012) $
#$Revision: 2443 $

# Import all node handler modules here.
# The act of importing them wires them in.

import genelements
import genpdftext

#sphinxnodes needs these
from genpdftext import NodeHandler, FontHandler, HandleEmphasis

# createpdf needs this
nodehandlers = NodeHandler()
