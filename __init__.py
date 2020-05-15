#// auth_ Mohamad Janati
#// AmirHassan Asvadi ;)
#// Copyright (c) 2020 Mohamad Janati (freaking stupid, right? :|)


from __future__ import annotations
from typing import Any, Optional
from aqt.toolbar import Toolbar, TopToolbar
from aqt import gui_hooks


_body = """
<center id=outer>
<table id=header width=100%%>
<tr>
<td class=tdcenter align=center>%s</td>
<td class=tdcenter width=10 align=right>%s</td>
</tr></table>
</center>
"""


def _centerLinks(self):
	links = [
		self.create_link("decks", _("Decks"), self._deckLinkHandler, tip=_("Shortcut key: %s") % "D", id="decks"),
		self.create_link("add", _("Add"), self._addLinkHandler, tip=_("Shortcut key: %s") % "A", id="add"),
		self.create_link("browse", _("Browse"), self._browseLinkHandler, tip=_("Shortcut key: %s") % "B", id="browse"),
	]
	gui_hooks.top_toolbar_did_init_links(links, self)
	return "\n".join(links)


def _rightLinks(self):
	links = [
		self.create_link("stats", _("Stats"), self._statsLinkHandler, tip=_("Shortcut key: %s") % "T", id="stats"),
		self._create_sync_link()
	]
	gui_hooks.top_toolbar_did_init_links(links, self)
	return "\n".join(links)


def draw(self, buf: str = "", web_context: Optional[Any] = None, link_handler: Optional[Callable[[str], Any]] = None):
	web_context = web_context or TopToolbar(self)
	link_handler = link_handler or self._linkHandler
	self.web.set_bridge_command(link_handler, web_context)
	self.web.stdHtml(self._body % (self._centerLinks(), self._rightLinks()), css=["toolbar.css"], context=web_context)
	self.web.adjustHeightToFit()
	if self.mw.media_syncer.is_syncing():
		self.set_sync_active(True)


Toolbar._body = _body
Toolbar._centerLinks = _centerLinks
Toolbar._rightLinks = _rightLinks
Toolbar.draw = draw
