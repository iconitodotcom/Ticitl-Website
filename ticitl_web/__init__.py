# ticitl-web/__init__.py
#
# Description: Ticitl Web site organization file
#
# Change History:
# Issue(opt)   Modifier            MM/DD/YYYY  Description
# ------       ------------------  ----------  ----------------------------------
#  n/a         Julio Conchas       05/03/2025  Initial include of change history header.

from flask import Flask
from ticitl_web.core.views import core

app = Flask(__name__)

app.register_blueprint(core)