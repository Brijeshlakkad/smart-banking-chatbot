#!/usr/bin/python
import sys
import os
def no_found(str_show):
	return """<div class="row" align="center" style="margin-top: 80px;">
	<div id="no_found"><img src="images/not-found.png" width="100px" alt="no found" /></div>
	<br/>
	<div style="color:gray;"><h4>%s</h4></div>
	</div>"""%str_show