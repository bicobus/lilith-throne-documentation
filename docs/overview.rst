.. include:: global.inc.rst
========
Overview
========

.. contents::

Preface
-------

The following documents will try it’s best to expose the different ways of
augmenting your experience while playing Lilith’s Throne. While the documents
tries to be as accurate as possible, you’re invited, dear reader, to consult
existing ``xml`` files residing in your ``res/mods/`` folder.

If you are unsure of anything, please use the Lilith’s Throne Discord
`Lilith's Throne Discord`_ to ask for help!

Note on status effects and how to use them
------------------------------------------

We understand by effects a set of of logic conditonally applied to a character.
The source of definining that condition differs, is ultimately applied through
an ``applyEffect`` block. Most wearable items has to go through a set bonus in
order to have access to the status effects mechanics.

Wearable have to define themselves as part of a set. The set then activate the
status effect based on simple conditionnals. Sets of one item, although counter
intuitive, are acceptable. Non-wearable items have a direct access to an
``applyEffect`` block, and as such do not require a reference to a
``statusEffect``.


.. graphviz ::

   digraph {
      coi [label = "Clothing Items"]
      wi [label = "Weapon Items"]
      cui [label = "Consumable Items"]
      appl [shape=box label = "applyEffect"]
      { coi wi } -> "setBonus";
      "setBonus" -> "statusEffect";
      { "statusEffect" cui } -> appl;
   }

Some elements expect Boolean values
-----------------------------------

Some elements are boolean switches which are either true, or false. The name of
the element is usually explicit enough to inform you of it’s function, for
example ``consumedOnUsed`` convey that the item should or should not be consumed
once the player uses it.

Whenever an element is stated to be boolean, one of the following value is
expected:

- ``true``
- ``false``

Shared tags and information
-----------------------------

Across the different types of items exists shared concepts. Some of those
concept may be expanded on a per category basis, for example weapons needs more
colours than the other kinds of items and thus expand the available list.

.. _items-identifier:

Item’s identifier
-----------------

The item identifier is the internal name of your objects and the only way to
refer to them from between ``xml`` files. It is calculated from your clothing’s
folder and ``.xml`` name using the following code:

.. code:: java

    modAuthorDirectory.getName() + "_"
        + innerChild.getParentFile().getName() + "_"
        + innerChild.getName().split("\\.")[0]

Which would resolve to ``innoxia_template_socks`` for the object located in
``res/mods/innoxia/clothing/template/socks.xml``.

The identifier is generated for every pertinent file existing in your modules
folder structure. The identifier being generated, and not user defined, is an
important variable to keep in mind. If you ever rename the folder or the ``xml``
file, the identifier will change which, in turn, will invalidate all existing
reference present in the players saves files.

.. _author-tags:

author tags
-----------

How attribution to the mod author (*you*) should be displayed in the object’s
tooltip. If left blank or not included, a default attribution based on folder
name will be used.

The content of the element should be a short one line descriptor.

Example

     *A tag discreetly sewn into the T-shirt’s inner lining informs you*
     *that it was made by ’Innoxia’.*

value
-----

The base value of an object. I roughly base things on 1 flame = 10p, so 10
flames = £1.

name
----

The name element contain the singular form of the name of the object (One
*sock*, two *socks*).

The name element can on occasion accept variables, refer to the specific
documentation of the object you aim to create for details.

Names can be informal, for objects that are not normally shown to the player
like outfits, and are only used for debugging purpose.

plural name
~~~~~~~~~~~

Each object with the possession of a name also has a plural form. If you have to
inform name, expect to fill in it’s plural form.

determiner
----------

The determiner which is displayed before an item’s name. While they are usually
“a” or “an”, for things like socks or gloves, you’ll want to use “a pair of”
where it makes sense. I use the ``CDATA`` tag for all text values, as it allows
html markup to be embedded without causing issues.

Should this element remain undefined, the game will automatically select either
“a” or “an” based on the name of the item. The game will ignore values passed to
this elements if they equate “a” or “an”.

Literate Example

    Innoxia was holding *a pair of* scissors.

Code Example

    .. code:: xml

        <determiner><![CDATA[a pair of]]></determiner>

Description
-----------

A long form description of the item. Should be present for each object under the
items category.

.. _items-image:

Item’s image
------------

The element ``imageName`` will be found through the different objects. It
informs of the file path for the object’s image. All images *must be* .svg
format. Colours to be used are described below, above the ``primaryColours``
element. I use the free program `InkScape <https://inkscape.org>`_ to make my
.svg images. .svg images scale perfectly up and down to any size, so, while it
should be a square, it doesn’t really matter what size your canvas is (although
I use 256 × 256 as a personal preference).

If the item can be equipped, then an ``imageEquippedname`` must also be
provided. Please refer to the appropriate documentation for more details.

.. _rarity:

rarity
------

The rarity of several object can be defined using the constants listed in the
file :ltgithub:`src/com/lilithsthrone/game/inventory/Rarity.java`.

Please note that any item set with a rarity of LEGENDARY will not appear
naturally in the game, neither from the shop keepers nor random encounters.

.. _colours:

colours
-------

Colours are available for most moddable items. The rules to follow are generally
the same for all type of item, with the exception for the weapons which expand
on the core mechanic.

Your items can be coloured any way you like, but if you’d like the player to be
able to dye your clothing, you can specify available colours here.
``primaryColours``, ``secondaryColours``, and ``tertiaryColours`` can all spawn
in as a default colour, while their ’Dye’ counterparts are only available if the
player chooses to dye the clothing in that colour. The game detects specific
colour values, and recolours them to the value chosen by the player. These
values are as follows:

- *Red* is used as base colour for changing the primary colour of the graphic
  in-game, and the game will only recognise and change the following colours:

  1. ``#ff2a2a``
  2. ``#ff5555``
  3. ``#ff8080``
  4. ``#ffaaaa``
  5. ``#ffd5d5``

- *Orange* is used as base colour for changing the secondary colour of the
  graphic in-game, and the game will only recognise and change the following
  colours:

  1. ``#ff7f2a``
  2. ``#ff9955``
  3. ``#ffb380``
  4. ``#ffccaa``
  5. ``#ffe6d5``

- *Yellow* is used as base colour for changing the tertiary colour of the
  graphic in-game, and the game will only recognise and change the following
  colours:

  1. ``#ffd42a``
  2. ``#ffdd55``
  3. ``#ffe680``
  4. ``#ffeeaa``
  5. ``#fff6d5``

.. important::

   Any gradients that you use should be called: ``innoGrad1``, ``innoGrad2``,
   etc.

A visual representation of these colours is available on the :wiki:`wiki
<creating_clothes>`.

Colour lists to be used can be found here:
:ltgithub:`src/com/lilithsthrone/utils/colours`.

You can leave the attribute ``recolouringAllowed`` out of colour definitions. If
you want the player to be unable to change this colour, then set it as false.
This is only used in very niche situations (such as for the filly choker).

You can also make your own, custom list of colours to be used. The following
colours in ``tertiaryColoursDye`` are all found within the list preset ``ALL``,
but this is for a demonstration.

If you want to include custom colours, do not define a ``values`` attribute, and
instead, list each Colour.

.. important::

   please use the ``Colour`` values that start with ``CLOTHING_``.

Code Example
    .. code:: xml

        <primaryColours recolouringAllowed="true" values="JUST_WHITE"/>
        <primaryColoursDye values="ALL"/>
        <secondaryColours values="JUST_BLACK"/>
        <secondaryColoursDye values="ALL"/>
        <tertiaryColours values="JUST_WHITE"/>
        <tertiaryColoursDye>
        	<colour>CLOTHING_WHITE</colour>
        	<colour>CLOTHING_BLACK</colour>
        	<colour>CLOTHING_GREY</colour>
        	<colour>CLOTHING_RED</colour>
        	<colour>CLOTHING_RED_BRIGHT</colour>
        	<colour>CLOTHING_RED_DARK</colour>
        	<colour>CLOTHING_ORANGE</colour>
        	<colour>CLOTHING_ORANGE_BRIGHT</colour>
        	<colour>CLOTHING_ORANGE_DARK</colour>
        	<colour>CLOTHING_BROWN</colour>
        	<colour>CLOTHING_TAN</colour>
        	<colour>CLOTHING_YELLOW</colour>
        	<colour>CLOTHING_GREEN_LIME</colour>
        	<colour>CLOTHING_GREEN</colour>
        	<colour>CLOTHING_GREEN_DARK</colour>
        	<colour>CLOTHING_TURQUOISE</colour>
        	<colour>CLOTHING_BLUE_LIGHT</colour>
        	<colour>CLOTHING_BLUE</colour>
        	<colour>CLOTHING_BLUE_DARK</colour>
        	<colour>CLOTHING_PURPLE</colour>
        	<colour>CLOTHING_PURPLE_DARK</colour>
        	<colour>CLOTHING_PURPLE_LIGHT</colour>
        	<colour>CLOTHING_PINK</colour>
        	<colour>CLOTHING_PINK_LIGHT</colour>
        </tertiaryColoursDye>

Custom Colours
~~~~~~~~~~~~~~

You can define any number of custom colours to replace the shades you’ve
coloured your svg with.

The ``copyColourIndex`` attribute seen in the example below defines which colour
index should be copied into this colour slot on weapon generation. This
particular colour, having an index of 0, will always be coloured the same as the
primary colour when generated. Indexes go from 0 :math:`\to` X, where X is the
number of defined colours. i.e. If you only define primary and secondary, the
first custom colour will have an index of 2.

Attributes from ``c0`` :math:`\to` ``c4`` are the colours which you’ve used in
your svg and would like replaced with the colours you define below. ``c0`` is
the darkest shade. Shades can go up to any number, but setting just 5 shades
should work best.

If you have used the ``primary`` / ``secondary`` / ``tertiary`` elements up
above, then do not use their associated colour hexes. (i.e. If you’ve defined a
``primaryColours`` element, do not use either of ``#ff2a2a``, ``#ff5555``,
``#ff8080``, ``#ffaaaa``, or ``#ffd5d5`` in the customColour attributes.)

You should also **not** use any of the following, as they are reserved for
pattern colours:

.. hlist::
   :columns: 3

   * ``#f4d7d7``
   * ``#e9afaf``
   * ``#de8787``
   * ``#d35f5f``
   * ``#c83737``
   * ``#f4e3d7``
   * ``#e9c6af``
   * ``#deaa87``
   * ``#d38d5f``
   * ``#c87137``
   * ``#f4eed7``
   * ``#e9ddaf``
   * ``#decd87``
   * ``#d3bc5f``
   * ``#c8ab37``

.. code:: xml

    <customColours>
    	<customColour copyColourIndex="0" c0="#6C5353" c1="#916F6F" c2="#AC9393" c3="#C8B7B7" c4="#E3DBDB"> (ref:cci)
    		<defaultColours>
    			<colour>CLOTHING_GREY</colour> <!-- The colours which this clothing should spawn in with. -->
    		</defaultColours>
    		<extraColours values="ALL"/> <!-- The colours which this clothing can be dyed to. -->
    	</customColour>
    </customColours>

status effects special case
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Status effects also accept colours, but to a lesser degree. The colours for
status effects are there to recolor the icon, as such at most three values are
expected for ``primary``, ``secondary``, and ``tertiary`` colours.
