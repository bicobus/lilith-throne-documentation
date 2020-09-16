.. include:: global.inc.rst

=============
Item Clothing
=============

    :Author: innoxia, bicobus

Clothing and anything that is wearable, even inside.

You can find working examples of clothing in the
:ltgithub:`res/mods/innoxia/items/clothing` folder.

General Information
-------------------

Any clothing item whose rarity is set to LEGENDARY or above will not show up in
the game, as no shopkeepers have been being defined as selling items of that
quality. You can spawn it from the debug menu if you wish. The debug menu is
accessed by typing ``buggy`` at any point in the game. It is best to enter the
debug menu when not in the middle of combat, sex, or movement-locked dialogue,
as it will break you out of it.

coreAttributes
--------------

authorTag
~~~~~~~~~
.. index:: author-tags

Author attribution, if you want one.

.. seealso::

   :ref:`author-tags`

.. code:: xml

    <authorTag><![CDATA[A tag discreetly sewn into the T-shirt's inner lining informs you that it was made by 'Innoxia'.]]></authorTag>

value
~~~~~
.. index:: item-value

Please refer to the general information about :ref:`item value<item-value>`.

Example
    I’ve defined this as 60, which is about the price for a basic pair
    of socks or something similar.

.. code:: xml

    <value>60</value>

determiner
~~~~~~~~~~

The determiner which is displayed before this item’s name. While usually “a” or
“an”, for things like socks or gloves, you’ll want to use “a pair of”. I use the
``CDATA`` tag for all text values, as it allows html markup to be embedded
without causing issues.

Example
    I’ve defined this as “a pair of”, so in-game, this item will be
    referred to as “a pair of socks”.

.. code:: xml

    <determiner><![CDATA[a pair of]]></determiner>

name
~~~~

The **singular** name of this clothing.

Example
    I’ve named this “template sock”, as the singular for “template
    socks” is of course “sock”...

.. code:: xml

    <name appendColourName="true"><![CDATA[template sock]]></name>

You can leave out the ``appendColourName`` attribute, but if you never want this
clothing to be described by its colour, then set it as false. (i.e. If set to
false, this clothing would always be called “template socks” instead of, for
example, “white template socks”.)

namePlural
~~~~~~~~~~

The plural form of the name. The attribute ``pluralByDefault`` determines
whether this item is naturally referred to as a plural (use true for things like
socks or gloves).

Example
   I’ve named the plural as “template socks”, and defined ``pluralByDefault`` as
   true, so that this item will be referred to by this plural name in all but
   extremely exceptional circumstances.

.. code:: xml

    <namePlural pluralByDefault="true"><![CDATA[template socks]]></namePlural>

description
~~~~~~~~~~~

This is the description which is shown in tooltips and on the item’s inspection
page.

Example
    The description for ordinary, “boring” items of clothing might be a
    little dry, but as they won’t be read by the player much, it doesn’t really
    matter.

.. code:: xml

    <description><![CDATA[An ordinary pair of socks, intended to be worn on the feet in order to absorb perspiration and provide both insulation and comfort. A silly person may choose to wear them on their hands...]]></description>

physicalResistance
~~~~~~~~~~~~~~~~~~

The default physical resistance for this piece of clothing. Usually use 0, but
if it’s armour, then values of 1 up to 5 would be fitting (any more than that
might be very OP). Physical resistance is a very powerful stat, so please keep
within the range of 0-5. For all normal clothing, the value should be 0. This
accepts decimal values, so for things like leather jackets (which aren’t really
armour, but are still protective), you can use 0.5 or so.

Example
    Left as 0, as it’s nomral, unarmoured clothing.

.. code:: xml

    <physicalResistance>0</physicalResistance>

femininity
~~~~~~~~~~

Use ``FEMININE`` for if this clothing is intended for feminine characters,
``MASCULINE`` for masculine, and ``ANDROGYNOUS`` if it’s able to be worn by
anyone without penalties.

Example
    Normal socks could be worn by both males and females without issue,
    so I set this to ``ANDROGYNOUS``.

.. code:: xml

    <femininity>ANDROGYNOUS</femininity>

equipSlots
~~~~~~~~~~

The slots that this clothing is able to be fit into. The game only supports up
to 4 unique slots, so if you define more than 4, the rest of them won’t show up
in-game. These definitions preserve ordering, so use the top one for the most
common slot to be fitted into. This is especially important for NPCs, as they
will use the top slot for determining which slot this clothing should fit into.

Possible slots are found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/InventorySlot.java`

Example
    I defined ``SOCK`` as the top slot, as this is the intended slot for
    socks. As I also want the player to be able to equip socks onto their hands, I
    defined ``HAND`` as a secondary slot.

.. code:: xml

    <equipSlots>
    	<slot>SOCK</slot>
    	<slot>HAND</slot>
    </equipSlots>

rarity
~~~~~~

The rarity of this item. Anything less than ``EPIC`` may end up being modified
in the code. Possible rarities are found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/Rarity.java`

Example
    Socks are most definitely ``COMMON``, but I’ve defined these as
    ``LEGENDARY`` so as to prevent them from naturally spawning in the game.

.. code:: xml

    <rarity>LEGENDARY</rarity>

clothingSet
~~~~~~~~~~~

The set that this clothing belongs to.

.. seealso::

   :doc:`/setBonuses`

Navigate to :ltgithub:`res/setBonuses` to see existing sets.

- Example: Just use the name of the set.

.. code:: xml

    <clothingSet>innoxia_template</clothingSet>

imageName
~~~~~~~~~

The file paths for this clothing’s image. Please refer to the
:ref:`documentation about images<items-image>`.

Example
    I’ve defined this as “sock.svg”, which should be placed in the same
    folder location alongside this xml file.

.. code:: xml

    <imageName>socks.svg</imageName>

imageEquippedName
~~~~~~~~~~~~~~~~~

The file paths for this clothing’s image while equipped. The “slot” attribute
determines the InventorySlot in which the defined file will be used.

Example
    When equipped to the ``SOCK`` slot, the sock will be displayed using the
    ``sock.svg`` file. When equipped to the “HAND” slot, it will instead use the
    ``sock_hand.svg`` file. Again, this file must be placed in the same folder
    location alongside this xml file.

.. code:: xml

    <imageEquippedName slot="SOCK">socks.svg</imageEquippedName>
    <imageEquippedName slot="HAND">socks_hand.svg</imageEquippedName>

stickers
~~~~~~~~

``Stickers`` are additional svgs which can be overlaid on top of (or beneath
the) base svg image. Definitions are all within the ``stickers`` element.

category
^^^^^^^^

All stickers defined within this category are **mutually exclusive** with one
another, but not with stickers defined in other ``category`` elements. The
``id`` should be unique to each category, and can be defined as whatever you
want, but for formatting purposes, it would be preferable for it to just contain
basic alpha-numerical values and underscores. The ``priority`` variable
determines the position of this category in UI rendering order (in the
inventory’s clothing dye screen), with lower values being rendered nearer to the
top of the category list.

Variables
    - id (string)

    - priority (integer)

Example
    .. code:: xml

        <category id="top_txt" priority="1">
          <!-- ... -->
        </category>

categoryName
::::::::::::

This is used in-game as the title for this sticker category in the sticker
application menu UI. As such, please try to make this human-readable.

Example
    .. code:: xml

        <categoryName><![CDATA[Top Text]]></categoryName>

.. index:: ! sticker
   :name: sticker

sticker
:::::::

A sticker element. Each sticker are exclusive with other stickers present in the
same category. Stickers of different cagetories can be combined.

The ``id`` element should be unique to stickers within this category element.
Define this variable to ``none`` (lit.) to give to the player the ability to
leave the selection blank.

The ``priority`` variable determines the position of this sticker in UI
rendering order (in the inventory’s clothing dye screen), with lower values
being rendered nearer to the left of the buttons list. A ``priority`` of ``0``
will set the sticker at the top of the list, regardless of it’s position in your
xml file.

``defaultSticker`` defines whether this sticker is applied to this clothing item
by default when spawned in.

``zLayer`` defines the rendering z-layer priority. These ``zLayer`` values are
compared against one another when rendering, with higher values being drawn on
top of stickers with lower values. **The base svg has a zLayer value of 0**,
meaning that negative values will be drawn beneath the base svg. Defining
``zLayer`` as 0 is not advised (although it is handled by always being drawn on
top of the base layer).

``colourDisabled`` and ``colourSelected`` are optional variables which you can
use to define the colour of the text within the button used to select this
sticker in the clothing dye UI. You can leave these blank or delete them
entirely to use default button colours. The default values, if you were to
define them using these variables, would look like: ``colourDisabled="TEXT_GREY"
colourSelected="GENERIC_GOOD"``

.. note::

   If you do not define an `imageName <sticker-imageName>`_ sub-element, or if
   you leave it blank, the default selected colour will be ``TEXT_GREY`` instead
   of ``GENERIC_GOOD``.

Available colours can be found here:
:ltgithub:`src/com/lilithsthrone/utils/colours/PresetColour.java`

You can also define custom colours instead of a PresetColour id, in which case
you **must** use a standard RGB hex code as the value.

e.g. ``colourDisabled="777777" colourSelected="57DB7E"``

Variables
    - id (string)

    - priority (integer)

    - defaultSticker (boolean)

    - zlayer (integer)

    - colourDisabled (constant)

    - colourSelected (constant)

Example
    .. code:: xml

        <sticker id="rental" priority="1" defaultSticker="true" zLayer="1" colourDisabled="" colourSelected="">
          <!-- ... -->
        </sticker>
        <sticker id="dommy" priority="2" defaultSticker="false" zLayer="1">
          <!-- ... -->
        </sticker>

stickerName
'''''''''''

This is used in-game as the title for this sticker’s button in the sticker
application menu UI. As such, please try to make this human-readable.

Example
    .. code:: xml

        <stickerName><![CDATA[Rental]]></stickerName>

namePrefix
''''''''''

Define a ``namePrefix`` to add a prefix to the base clothing’s name when this
sticker is applied.

The ``priority`` variable defines the order in which multiple sticker
``namePrefix`` are displayed. A **lower value** means they will be **displayed
first**. This can be left undefined.

Variables
    - priority (integer)

Example
    .. code:: xml

        <namePrefix priority="1"><![CDATA[Rental]]></namePrefix>

namePostfix
'''''''''''

Exactly the same as `namePrefix`_, but the text is appended after the base
clothing name.

descriptionmodification
'''''''''''''''''''''''

You can set whether this sticker should define a new description for the
clothing.

If ``fullReplacement`` is true, then the clothing’s description is completely
replaced with ``descriptionModification`` while this sticker is applied. If
``fullReplacement`` is false, then it is appended to the base clothing
description (so long as another sticker has not applied a ``fullReplacement``).

The ``priority`` element defines in what order the description appending is
performed, or, if ``fullReplacement`` is true for multiple active stickers,
which sticker’s description has priority.

Variables
    - fullReplacement (boolean)

    - priority (integer)

Example
    .. code:: xml

        <descriptionModification fullReplacement="false" priority="1"><![CDATA[<i>Rental </i>]]></descriptionModification>

imageName
'''''''''

The path name for this sticker, which should be in the same folder location as
this xml file.

The ``slot`` variable can be omitted, in which case the default slot for the
clothing item is used.

If the clothing can be equipped into multiple slots, you don’t **need** to
define an ``imageName`` element for every slot, but if you don’t, the game will
end up using any of your defined ``imageName`` at random (which is not a problem
if you only define one ``imageName`` that’s suitable for any of the clothing’s
base ``imageName``).

The ``zLayer`` attribute defines the rendering order for this svg image. You do
not need to define this attribute, as if it is missing, this svg will use the
sticker’s ``zLayer`` attribute which you’ve already defined up above in the root
``sticker`` element. I have included it here just as an example.

.. note::

   You can add as many ``imageName`` elements as you like.

Variables
    - zLayer (interger)

    - slot (constant)

Example
    .. code:: xml

        <imageName zLayer="1" slot="TORSO_UNDER">text_rental.svg</imageName>

itemTagsAdded
'''''''''''''

If this sticker should add any ItemTags to the clothing, then you can define
them in here. Use ``<tag>`` elements within the ``itemTagsAdded`` element (e.g.
``<tag>SOLD_BY_NYAN</tag>``) using ``ItemTag`` names as defined here:
:ltgithub:`src/com/lilithsthrone/game/inventory/ItemTag.java`

Example
    .. code:: xml

        <itemTagsAdded>
          <tag>SOLD_BY_NYAN</tag>
        </itemTagsAdded>

itemTagsRemoved
'''''''''''''''

If this sticker should remove any ``ItemTags`` to the clothing, then you can
define them in here. Use ``<tag>`` elements in the same manner as
`itemTagsAdded`_.

.. warning::

   If you define either a single sticker or multiple stickers to have
   conflicting tag behaviour -- i.e. both adding and removing identical tags --,
   then behaviour is undefined and you will end up with the ``ItemTag`` applied
   or removed at random.

unavailabilityText
''''''''''''''''''

Sticker are available to be used by the player by default, but if you want there
to be requirements for using this sticker, then define this element as a
``CDATA`` text element, with any non-whitespace text returned signalling to the
game that this sticker is unavailable. The returned text will be displayed to
the player in the button’s tooltip, so it should describe why this sticker is
unavailable.

You can define a ``showDisabledButton`` attribute, which by default is set to
true, and which defines whether or not this sticker’s selection button is shown
to the player when disabled.

Please note that no ``npc`` tag can be used, as this clothing might not belong
to anyone.

Variables
    - showDisabledButton (boolean)


An example where the player could only use the sticker while being feminine
would be:

.. code:: xml

    <unavailabilityText showDisabledButton="true"><![CDATA[
    	#IF(!pc.isFeminine())
    	Only feminine characters can apply this sticker!
    	#ENDIF
    ]]></unavailabilityText>

And for this example, the disabled button is not shown to the player, so there’s
no need for an elaborate description, as the player will never see it:

.. code:: xml

    <unavailabilityText showDisabledButton="false"><![CDATA[
    	#IF(pc.getSubspeciesOverrideRace()!=RACE_DEMON && !pc.isFeminine())
    		unavailable
    	#ENDIF
    ]]></unavailabilityText>

availabilityText
''''''''''''''''

The counterpart to `unavailabilityText`_, this text is shown when
`unavailabilityText`_ is returning an empty String, and therefore this sticker
is available. Use a ``CDATA`` text element.

Counterpart examples to the two above:

.. code:: xml

    <availabilityText><![CDATA[
    	You have unlocked this sticker due to being feminine!
    ]]></availabilityText>

    <availabilityText><![CDATA[
    	#IF(pc.getSubspeciesOverrideRace()==RACE_DEMON)
    		You have unlocked this sticker due to being a demon!
    	#ELSE
    		You have unlocked this sticker due to being feminine!
    	#ENDIF
    ]]></availabilityText>

echantmentLimit
~~~~~~~~~~~~~~~

How many enchantments can be fit into this item. It’s typically best to let the
game handle the default number of enchantments, which typically results in 100.

Example

    I have not defined this, as I’ll let the game keep the 100
    enchantments default value.

Using default value

.. code:: xml

    <enchantmentLimit/>

Using custom value

.. code:: xml

    <enchantmentLimit>100</enchantmentLimit>

effects
~~~~~~~

The default effects that this clothing spawns in with. To know what to put in
here, it would probably be easiest to enchant clothing in your game, save the
game, then copy over that clothing’s ’effects’ in your save file.

Example

    The first defined effect will give +3 to physical damage, while the
    second will give the wearer the masturbation fetish while worn.

.. code:: xml

    <effects>
    	<effect itemEffectType="CLOTHING" limit="0" potency="MAJOR_BOOST" primaryModifier="CLOTHING_ATTRIBUTE" secondaryModifier="DAMAGE_PHYSICAL" timer="0"/>
    	<effect itemEffectType="CLOTHING" limit="0" potency="MAJOR_BOOST" primaryModifier="TF_MOD_FETISH_BEHAVIOUR" secondaryModifier="TF_MOD_FETISH_MASTURBATION" timer="0"/>
    </effects>

blockedPartsList
~~~~~~~~~~~~~~~~

This section determines how the clothing interacts with other clothing and the
wearer’s body.

Example

    I’ve defined this section as being the one to be used when equipped
    to the “SOCK” slot.

    .. code:: xml

        <blockedPartsList slot="SOCK">
        	<blockedParts>
        		<displacementType>REMOVE_OR_EQUIP</displacementType>
        		<clothingAccessRequired>
        			<clothingAccess>FEET</clothingAccess>
        		</clothingAccessRequired>
        		<blockedBodyParts>
        			<bodyPart>FEET</bodyPart>
        		</blockedBodyParts>
        		<clothingAccessBlocked/>
        		<concealedSlots/>
        	</blockedParts>
        </blockedPartsList>

This is another section to determines how the clothing interacts with other
clothing and the wearer’s body.

Example

    I’ve defined this section as being the one to be used when equipped
    to the ``HAND`` slot.

    .. code:: xml

        <blockedPartsList slot="HAND">
        	<blockedParts>
        		<displacementType>REMOVE_OR_EQUIP</displacementType>
        		<clothingAccessRequired>
        			<clothingAccess>FINGERS</clothingAccess>
        		</clothingAccessRequired>
        		<blockedBodyParts/>
        		<clothingAccessBlocked/>
        		<concealedSlots/>
        	</blockedParts>
        </blockedPartsList>

blockedParts
^^^^^^^^^^^^

You can add as many ``blockedParts`` elements as you like, but they should each
have a different `displacementType`_, and **there should be at least one, of
type** ``REMOVE_OR_EQUIP``.

displacementType
^^^^^^^^^^^^^^^^

If this clothing is displaced in the following way (in this case, by being
removed), then the `blockedBodyParts`_, `clothingAccessBlocked`_, and
`concealedSlots`_ will all be revealed. If multiple `blockedParts`_ block or
conceal the same slot, only one `blockedParts`_ needs to be displaced to reveal
it. (e.g. If a pair of trousers has ``UNZIPS`` and ``PULLS_DOWN``
displacementTypes, and both of these contain the ``concealedSlots`` ``slot``
``PENIS``, then the penis will be revealed if either ``UNZIPS`` or
``PULLS_DOWN`` is activated.)

A full list of displacementTypes can be found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/clothing/DisplacementType.java`

clothingAccessRequired
^^^^^^^^^^^^^^^^^^^^^^

The access required to perform this `displacementType`_.

``clothingAccess`` values can be found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/clothing/ClothingAccess.java`

blockedBodyParts
^^^^^^^^^^^^^^^^

The body parts that are blocked by this `displacementType`_.

``bodyPart`` values can be found here:
:ltgithub:`src/com/lilithsthrone/game/character/body/CoverableArea.java`

clothingAccessBlocked
^^^^^^^^^^^^^^^^^^^^^

The access that this `displacementType`_ blocks. Again, clothingAccess values
can be found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/clothing/ClothingAccess.java`

This element must contain a list of tag ``clothingAccess`` for values inserted
here.

Example
    .. code:: xml

        <clothingAccess>MOUTH</clothingAccess>

concealedSlots
^^^^^^^^^^^^^^

The slots that this `displacementType`_ conceals. Possible slots are found
here: :ltgithub:`src/com/lilithsthrone/game/inventory/InventorySlot.java`


You can also use a preset list by adding an attribute named “values” to this
element (an example -- “CS Example” -- is in the `blockedParts`_ section below
this one). The preset lists that you can use are found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/clothing/PresetConcealmentLists.java`

Use the tag ``slot`` for values inserted here.

Example
    .. code:: xml

        <slot>HEAD</slot>

incompatibleSlots
~~~~~~~~~~~~~~~~~

Inventory slots that are incompatible with this clothing. The game’s swimsuit
makes use of this, and, while fitting into the ``CHEST`` slot, also blocks
``GROIN`` and ``STOMACH``. Possible slots are found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/InventorySlot.java`

Example

    You need to define an ``incompatibleSlots`` element for each slot that the
    clothing can be equipped into, so here, I’ve defined an empty one for
    ``SOCK``, and another empty one for ``HAND``.

Example 2
    If you want to add slots, then use the element like so (which
    would block the ``FINGER`` slot when equipped into the ``WRIST`` slot):

.. code:: xml

    <incompatibleSlots slot="WRIST">
    	<slot>FINGER</slot>
    </incompatibleSlots>
    <incompatibleSlots slot="SOCK"/>
    <incompatibleSlots slot="HAND"/>

colours
~~~~~~~

Please consult the relevant :ref:`documentation<colours>`.

Your clothing can be coloured any way you like, but if you’d like the player to
be able to dye your clothing, you can specify available colours here.
``primaryColours``, ``secondaryColours``, and ``tertiaryColours`` can all spawn
in as a default colour, while their ’Dye’ counterparts are only available if the
player chooses to dye the clothing in that colour. The game detects specific
colour values, and recolours them to the value chosen by the player. These
values are as follows:

Colour types can be found in the files present in the following folder:
:ltgithub:`src/com/lilithsthrone/utils/colours`

.. important::

   please use the ``Colour`` values that start with ``CLOTHING_``.

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
    	<!-- ... -->
    	<colour>CLOTHING_PINK_LIGHT</colour>
    </tertiaryColoursDye>

customColours
^^^^^^^^^^^^^

You can define any number of custom colours to replace the shades you’ve
coloured your svg with.

.. code:: xml

    <customColours>
    	<customColour copyColourIndex="0" c0="#6C5353" c1="#916F6F" c2="#AC9393" c3="#C8B7B7" c4="#E3DBDB">
    		<defaultColours>
    			<colour>CLOTHING_GREY</colour> <!-- The colours which this clothing should spawn in with. -->
    		</defaultColours>
    		<extraColours values="ALL"/> <!-- The colours which this clothing can be dyed to. -->
    	</customColour>
    </customColours>

patterns
~~~~~~~~

This section details how to define patterns. If your svg file does not have a
``patternLayer`` defined, you can safely delete this whole section:

``defaultPatterns``
    lists the patterns that this clothing can spawn with.

    - ``patternChance``

        is the chance that this clothing will spawn with a pattern. Values are
        from 0 to 1, and should end with an “f”. i.e. 0.5f is a 50% chance,
        0.75f is 75%, 0.1275 is 12.75%, etc.
      
    - ``colourNameDerivedFromPattern``

        sets whether the pattern’s primary colour should be used for the
        clothing’s name, instead of the “colour” value. i.e. If set to ``true``,
        then a green+black tiger-striped item of clothing would be called
        “green”, even if the base colour was something else.

``pattern``
    Pattern values can be found as svg file names in the folder ``res/patterns``

.. code:: xml

    <defaultPatterns patternChance="0" colourNameDerivedFromPattern="false"> 
    	<pattern>camo</pattern>
    </defaultPatterns>

patternPrimaryColours, patternSecondaryColours, and patternTertiaryColours
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Colours work the same as explained in the `colours`_ section.

.. code:: xml

    <patternPrimaryColours>
    	<colour>CLOTHING_GREEN</colour>
    </patternPrimaryColours>
    <patternSecondaryColours values="ALL"/>
    <patternTertiaryColours/>

customPatternColours
^^^^^^^^^^^^^^^^^^^^

Custom pattern colours can be defined just like the customColours up above.

.. code:: xml

    <customPatternColours/>

itemTags
~~~~~~~~

These tags determine where in the world your clothing can be found, and what
special attributes your clothing should have. Possible tags are defined in
:ltgithub:`src/com/lilithsthrone/game/inventory/ItemTag.java`

``itemTags`` without a ``slot`` defined will have these tags added to every
equippable slot. Should only be used for generic tags like those related to
which vendors sell it.

``itemTags`` with a ``slot`` defined will have these tags applied ONLY when the
clothing is equipped into that slot. In this example, equipping the socks onto
your hands hinders arm movement. This is not entirely logical, and I added this
just for demonstration purposes.

.. code:: xml

    <itemTags>
    	<tag>NOT_FOR_SALE</tag>
    </itemTags>
    <itemTags slot="HAND">
    	<tag>HINDERS_ARM_MOVEMENT</tag>
    </itemTags>

sexAttributesSelf
-----------------

See the :ltgithub:`res/clothing/innoxia/buttPlugs/butt_plug.xml` file for a
working example of this element.

These are the sex attributes applicable to the wearer (i.e. when inserted in the
wearer’s orifices or when the wearer is penetrating this clothing type. Mainly
used for insertable dildos.)

.. code:: xml

    <sexAttributesSelf>
    	<penetration>
    		<length>15</length>
    		<girth>5</girth>
    		<modifiers>
    			<mod>VEINY</mod>
    		</modifiers>
    	</penetration>
    	<orifice>
    		<depth>0</depth>
    		<capacity>0</capacity>
    		<elasticity>3</elasticity>
    		<plasticity>3</plasticity>
    		<wetness>0</wetness>
    		<modifiers>
    			<mod>PUFFY</mod>
    		</modifiers>
    	</orifice>
    </sexAttributesSelf>

penetration
~~~~~~~~~~~

length
    value in cm

grith
    0-6 corresponding to ``PenetrationGirth Enum`` values

modifiers
    For adding modifiers, add ``mod`` tags containing
    ``PenetrationModifier Enum`` values

orifice
~~~~~~~

.. versionchanged:: 0.3.7

   orifice sex toy support is not fully implemented into the game!

depth
    value in cm

capacity
    value in cm, corresponding to the diameter of the orifice

elasticity
    0-7 corresponding to ``OrificeElasticity Enum`` values

plasticity
    0-7 corresponding to ``OrificePlasticity Enum`` values

wetness
    0-7 corresponding to ``Wetness Enum`` values

modifiers
    list of ``mod`` tags, each containing ``OrificeModifier Enum`` values

sexAttributesOther
------------------

These are the sex attributes applicable to someone who is interacting with the
wearer (i.e. the penetration/orifice which is available for people other than
the wearer. Mainly used for strap-on dildos.)

.. seealso::

   Consult the file
   :ltgithub:`res/clothing/norin/strapless_dildo/strapless_dildo.xml` for a
   working example of the following excerpt.

For an explanation of the effects of the different sub elements, please refer to
`sexattributesself`_.

.. code:: xml

    <sexAttributesOther>
    	<penetration>
    		<length>25</length>
    		<girth>3</girth>
    		<modifiers/>
    	</penetration>
    	<orifice/>
    </sexAttributesOther>

replacementText
---------------

The following sections are for defining the descriptions of displacing or
replacing your clothing. The attribute ``type`` defines which ``DisplacementType``
your descriptions are applied to. For standard equipping and unequipping, use
``REMOVE_OR_EQUIP``.

.. seealso::

   List of type contant:
   :ltgithub:`src/com/lilithsthrone/game/inventory/clothing/DisplacementType.java`.

Example
    This is the equip text for when socks are equipped to the ``SOCK`` slot:

    .. code:: xml

        <replacementText slot="SOCK" type="REMOVE_OR_EQUIP">
        	<self>
        		<![CDATA[[npc.Name] [npc.verb(pull)] the socks on to cover [npc.her] [npc.feet].]]>
        	</self>
        	<other>
        		<![CDATA[[npc.Name] [npc.verb(pull)] the socks onto [npc2.namePos] [npc2.feet].]]>
        	</other>
        	<otherRough>
        		<![CDATA[[npc.Name] roughly [npc.verb(pull)] the socks onto [npc2.namePos] [npc2.feet].]]>
        	</otherRough>
        </replacementText>

Example
    This is the equip text for when socks are equipped to the ``HAND`` slot:

    .. code:: xml

        <replacementText slot="HAND" type="REMOVE_OR_EQUIP">
        	<self>
        		<![CDATA[[npc.Name] [npc.verb(pull)] the socks on to cover [npc.her] [npc.hands].]]>
        	</self>
        	<other>
        		<![CDATA[[npc.Name] [npc.verb(pull)] the socks onto [npc2.namePos] [npc2.hands].]]>
        	</other>
        	<otherRough>
        		<![CDATA[[npc.Name] roughly [npc.verb(pull)] the socks onto [npc2.namePos] [npc2.hands].]]>
        	</otherRough>
        </replacementText>

displacementText
----------------

This section is used for removal and displacement.

Example
    This is the unequip text for when socks are removed from the ``SOCK`` slot:

    .. code:: xml

        <displacementText slot="SOCK" type="REMOVE_OR_EQUIP">
        	<self>
        		<![CDATA[[npc.Name] [npc.verb(pull)] off [npc.her] socks.]]>
        	</self>
        	<other>
        		<![CDATA[[npc.Name] [npc.verb(pull)] off [npc2.namePos] socks.]]>
        	</other>
        	<otherRough>
        		<![CDATA[[npc.Name] roughly [npc.verb(pull)] off [npc2.namePos] socks.]]>
        	</otherRough>
        </displacementText>

Example
    This is the unequip text for when socks are removed from the ``HAND`` slot:

    .. code:: xml

        <displacementText slot="HAND" type="REMOVE_OR_EQUIP">
        	<self>
        		<![CDATA[[npc.Name] [npc.verb(pull)] the socks from off of [npc.her] [npc.hands].]]>
        	</self>
        	<other>
        		<![CDATA[[npc.Name] [npc.verb(pull)] the socks from off of [npc2.namePos] [npc2.hands].]]>
        	</other>
        	<otherRough>
        		<![CDATA[[npc.Name] roughly [npc.verb(pull)] the socks from off of [npc2.namePos] [npc2.hands].]]>
        	</otherRough>
        </displacementText>
