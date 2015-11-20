# --.-- encoding: utf8 --.--
from abc import ABCMeta
from jinja2.filters import do_mark_safe


class Html:
    """
    Interface for renderable components as html fragments
    """
    __metaclass__ = ABCMeta

    tag_id = None
    classes = None

    def __init__(self, tag_id=None, classes=None):
        if classes is None:
            classes = None
        self.tag_id = tag_id
        self.classes = classes

    """
    string conversion with the renderable contents of the component
    """
    def __str__(self):
        return do_mark_safe(self.render())

    """
    the explicit call to the render component function
    returns None by default
    """
    def render(self):
        pass


class Footer(Html):

    text = None

    def __init__(self, text=None):
        self.text = text

    def render(self):
        return u"""<footer id="footer">
  <div class="mui-container-fluid">
    %s
  </div>
</footer>""" % self.text


class LinkItem(Html):
    name = None
    href = None

    def __init__(self, name, href=None):
        self.name = name
        self.href = href

    def render(self):
        return '<li><a href="%s">%s</a></li>'%(self.href, self.name)


class SidebarCategory(Html):
    name = None
    links = None

    def __init__(self, name):
        self.name = name
        self.links = []

    def add_link(self, link):
        self.links.append(link)

    def render(self):
        return u"""<li>
      <strong>%s</strong>
      <ul>
        %s
      </ul>
    </li>""" % (self.name, "".join(map(str, self.links)))


class Sidebar(Html):
    name = None
    categories = None

    def __init__(self, name=None):
        self.name = name
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def render(self):
        return u"""<div id="sidedrawer" class="mui--no-user-select">
      <div id="sidedrawer-brand" class="mui--appbar-line-height mui--text-title">%s</div>
      <div class="mui-divider"></div>
      <ul>
          %s
      </ul>
    </div>""" % (self.name, "".join(map(str, self.categories)))