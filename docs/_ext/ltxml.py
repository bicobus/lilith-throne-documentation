from docutils import nodes
from sphinx import addnodes
from sphinx.domains.python import PyField
from sphinx.util.docfields import Field, GroupedField
from sphinx.locale import _


class ltxmlvar(nodes.FixedTextElement):
    pass


def visit_xmlvar_html(self, node):
    pass


def depart_xmlvar_html(self, node):
    pass


def parse_nodevar(env, sig, signode):
    nodevar, t, default = sig.split(" ", 2)
    nodevar = nodevar.strip()
    if nodevar.startswith('[') and nodevar.endswith(']'):
        nodevar = nodevar.strip('[]')
        optional = True
    else:
        optional = False
    t = "Type: %s" % t.strip(" <>").lower()
    d = "%s" % default.strip(" ()")

    signode += addnodes.desc_name(nodevar, nodevar)
    signode += nodes.Text(' ')
    signode += addnodes.desc_type(t, t)
    if d:
        signode += nodes.Text(', ')
        default = "Default: %s" % d
        signode += addnodes.desc_annotation(default, default)
    if optional:
        signode += nodes.Text(', ')
        signode += addnodes.desc_annotation("Optional", "Optional")
    return nodevar


def setup(app):

    fopt = Field(
        name='optional',
        names=('opt', 'optional',),
        label=_('Optional'),
        has_arg=False,
    )

    ftype = PyField(
        'type',
        label=_('Type'),
        has_arg=False,
        names=('type',),
        bodyrolename='class'
    )

    fdef = GroupedField(
        'default',
        label=_('Default'),
        names=('default',),
        can_collapse=True,
    )

    app.add_object_type(
        'nodevar',
        'nodevar',
        objname='variable value',
        indextemplate='pair: %s; node variable value',
        doc_field_types=[fopt, ftype, fdef],
        parse_node=parse_nodevar,
    )
    # app.add_node(
    #     ltxmlvar,
    #     html=(visit_xmlvar_html, depart_xmlvar_html)
    # )
