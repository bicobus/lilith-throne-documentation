=======
Outfits
=======

    :Author: innoxia, bicobus

.. contents::

Outfits are a way to make randomly generated NPCs’ outfit generation less
chaotic.

As a final note, I will add support for allowing the automatic generation of
piercings in the next update.

1 coreAttributes
----------------

1.1 name
~~~~~~~~

Names are only used for debugging purposes. Still, in case the name is used
elsewhere later on, it’s best to give your outfit a suitable (lowercase) name.

.. code:: xml

    <name><![CDATA[casual dress with toys]]></name>

1.2 description
~~~~~~~~~~~~~~~

Again, descriptions are only used for debugging purposes. Still, in case the
name is used elsewhere later on, it’s best to give your outfit a suitable
description.

.. code:: xml

    <description><![CDATA[A dress hides the fact that the wearer has a toy or two inserted into their orifices...]]></description>

1.3 femininity
~~~~~~~~~~~~~~

The femininity needed for someone to generate this outfit.

The three acceptables values are respectively:

1. ``MASCULINE``

2. ``ANDROGYNOUS`` (anyone can use this outfit)

3. ``FEMININE``

.. code:: xml

    <femininity>FEMININE</femininity>

1.4 worldTypes
~~~~~~~~~~~~~~

The worlds in which this outfit may be used for randomly generated characters.
You can leave this empty, or delete the element entirely, if you do not want
this outfit to be restricted based on ``WorldType`` (so it can be used anywhere).
Values can be found here:
`src/com/lilithsthrone/world/WorldType.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/world/WorldType.java>`_

.. code:: xml

    <worldTypes>
    	<world>DOMINION</world>
    	<world>SUBMISSION</world>
    </worldTypes>

1.5 outfitTypes
~~~~~~~~~~~~~~~

Outfit types that this outfit can be used in. For a list of acceptable
``OutfitTypes``, consult:
`src/com/lilithsthrone/game/inventory/clothing/OutfitType.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/inventory/outfit/OutfitType.java>`_

Note: At the time of creation (*v0.3.0.6*), only the ``MUGGER`` outfitType is
used in the game. All outfit types will be added eventually.

.. code:: xml

    <outfitTypes>
    	<type>CASUAL_DATE</type>
    </outfitTypes>

1.6 acceptableLegConfigurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Which leg configurations can equip this outfit. For a list of
``legConfigurations``, see:
`src/com/lilithsthrone/game/character/body/valueEnums/LegConfiguration.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/character/body/valueEnums/LegConfiguration.java>`_

.. code:: xml

    <acceptableLegConfigurations>
    	<legConfiguration>BIPEDAL</legConfiguration>
    </acceptableLegConfigurations>

1.7 conditional
~~~~~~~~~~~~~~~

The condition that needs to be satisfied for someone to generate this outfit.
``npc.hasFetish(FETISH_EXHIBITIONIST)`` should probably always be taken into
account. This conditional instance does **not** support the ``clothingConditionalX``
elements.

- Accepted method calls for the “npc” can be found here:
  `src/com/lilithsthrone/game/character/GameCharacter.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/character/GameCharacter.java>`_

- Accepted method calls for the main game (using the ``game`` tag) can be found
  here: `src/com/lilithsthrone/game/Game.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/Game.java>`_

- And also here: `com/lilithsthrone/game/dialogue/utils/UtilText.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/dialogue/utils/UtilText.java>`_

The method ``initScriptEngine()`` in ``UtilText.java`` shows you what you can get a
handle on.

.. code:: xml

    <conditional><![CDATA[!npc.hasFetish(FETISH_EXHIBITIONIST) && npc.hasFetish(FETISH_MASTURBATION) && npc.getFetishDesire(FETISH_SUBMISSIVE).isPositive()]]></conditional>

1.8 weight
~~~~~~~~~~

How likely this outfit is to be randomly chosen out of all available ones.
Default outfits have a weight of 100. As there could be several outfits added to
the weighting method, the chance of this outfit being selected is not able to be
precisely determined.

A bigger number makes the outfits more common. There is no upper limit.

.. code:: xml

    <weight>100</weight>

2 generationAttributes
----------------------

2.1 Conditional statements
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can define any number of conditional statements to use elsewhere in this
file. They must be enclosed in CDATA tags, and must use a format of
``clothingConditionalX`` or ``condX``, where ``X`` is a unique ``String`` (e.g. ``cond1``,
``condUnderwear``, ``clothingConditionalMeleeWeapons`` are all valid tags). If they
have the attribute: ``constant="true"``, then they are evaluated once at the start
of clothing generation. If not, they are re-evaluated every time.

Example:

.. code:: xml

    <cond1 constant="true"><![CDATA[RND.nextInt(100)<=50]]></cond1>
    <cond2 constant="true"><![CDATA[RND.nextInt(100)<=75]]></cond2>

2.2 presetColourGroups
~~~~~~~~~~~~~~~~~~~~~~

Preset colour groups have one of their defined ``randomColour`` randomly chosen
for further use in this XML file. You can have up to 20 ``presetColourGroupX``,
however the numbers must be consecutive. (i.e. You can have
``presetColourGroup1``, ``presetColourGroup2``, and ``presetColourGroup3``, but **not**
``presetColourGroup1``, ``presetColourGroup2``, and ``presetColourGroup4``, as that
skips out a “3”.)

Accepted values can be found in the files present in the
`src/com/lilithsthrone/utils/colours <https://github.com/Innoxia/liliths-throne-public/tree/dev/src/com/lilithsthrone/utils/colours>`_ directory.

The optional ``singleColour`` attribute, when set to ``true``, means that this group
will always return the same, randomly chosen colour from its list.

Preceding ``presetColourGroups`` can be used, but not succeeding ones. (i.e.
``presetColourGroup3`` could not be used in ``presetColourGroup2``.)

.. code:: xml

    <presetColourGroup1 singleColour="true">
    	<randomColour>CLOTHING_PINK</randomColour>
    	<randOMCOLOUR>CLOTHING_PINK_LIGHT</randomColour>
    	<randomColour>CLOTHING_RED_DARK</randomColour>
    </presetColourGroup1>

    <presetColourGroup2>
    	<randomColour>CLOTHING_BLACK</randomColour>
    	<randomColour>presetColourGroup1</randomColour>
    </presetColourGroup2>

    <presetColourGroup3>
    	<randomColour>CLOTHING_GOLD</randomColour>
    	<randomColour>CLOTHING_SILVER</randomColour>
    </presetColourGroup3>

    <presetColourGroup4>
    	<randomColour>CLOTHING_WHITE</randomColour>
    	<randomColour>CLOTHING_PINK_LIGHT</randomColour>
    </presetColourGroup4>

2.3 mainWeapons and offhandWeapons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Weapons can be added in a similar (although more limited) manner to clothing.
This file doesn’t use any weapons. Look at
``res/outfits/innoxia/genericMugger/dominion_masculine.xml`` for a weapon example.

The content present in ``mainWeapons`` and ``offhandWeapons`` follow the same rules.
The main weapons block defines which item should be inserted into the
character’s main attack slot, where ass the off hand block defines which item to
be inserted into the character’s off hand. Each block receive one or several
``weapon`` sub elements.

The ``weapon`` block require the following elements to be present:

``conditional``
    references to the conditional statement present in the
    document.

``types``
    A list of valid item to be chosen from. It expects `item identifiers <index.rst>`_.

``damageTypes``
    Possible choices available at
    `src/com/lilithsthrone/game/combat/DamageType.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/combat/DamageType.java>`_

``primaryColours``
    contains a list of ``colour`` elements, which makes
    references to the preset groups defined previously.

``secondaryColours``
    contains a list of ``colour`` elements, which makes
    references to the preset groups defined previously.

colours
    element can be used in addition to, or as a replacement of, the
    primary/secondary/tertiary colours elements.

Individual colours or ``presetColourGroups`` can be listed in each sub-element
related to colours.

.. code:: xml

    <mainWeapons>
    	<weapon>
    		<conditional><![CDATA[cond1 && !cond2]]></conditional>
    		<types>
    			<type>innoxia_pipe_pipe</type>
    			<type>innoxia_bat_wooden</type>
    			<type>innoxia_bat_metal</type>
    		</types>
    		<damageTypes>
    			<damage>PHYSICAL</damage>
    		</damageTypes>
    		<primaryColours>
    			<colour>presetColourGroup1</colour>
    		</primaryColours
    		<secondaryColours/>
    		<colours>
    			<colour>presetColourGroup1</colour>
    		</colours>
    	</weapon>
    </mainWeapons>

.. code:: xml

    <offhandWeapons/>

2.4 guaranteedClothingEquips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For all of the “conditional” elements from this point onwards, you can use the
tag “clothing” to access the clothing type being handled.

All of the pre-set clothing that *is guaranteed* to be attempted to be equipped.
The only time these items won’t be equipped is when multiple items of clothing
are assigned to the same inventory slot (such as a pair of panties and a thong),
in which case only the first item is used.

.. code:: xml

    <guaranteedClothingEquips>
    	<uniqueClothing>
    		<clothing colour="CLOTHING_SILVER" colourSecondary="CLOTHING_PURPLE_LIGHT" colourTertiary="CLOTHING_BLACK" enchantmentKnown="true" id="innoxia_buttPlugs_butt_plug_jewel" isDirty="false" name="[npc.NamePos(true)] butt-plug" pattern="none" patternColour="CLOTHING_BLACK" patternColourSecondary="CLOTHING_BLACK" patternColourTertiary="CLOTHING_BLACK">
    			<effects>
    			  <effect itemEffectType="CLOTHING" limit="0" potency="BOOST" primaryModifier="CLOTHING_ATTRIBUTE" secondaryModifier="DAMAGE_POISON" timer="0"/>
    			  <effect itemEffectType="CLOTHING" limit="0" potency="MINOR_BOOST" primaryModifier="CLOTHING_ATTRIBUTE" secondaryModifier="DAMAGE_FIRE" timer="0"/>
    			</effects>
    			<displacedList/>
    		</clothing>
    	</uniqueClothing>

    	<uniqueClothing>
    		<conditional><![CDATA[npc.hasVagina()]]></conditional>
    		<clothing colour="presetColourGroup2" colourSecondary="CLOTHING_BLACK" colourTertiary="CLOTHING_BLACK" enchantmentKnown="true" id="innoxia_vagina_insertable_dildo" isDirty="false" name="[npc.NamePos(true)] insertable dildo"></clothing>
    	</uniqueClothing>
    </guaranteedClothingEquips>

2.4.1 clothing tags
^^^^^^^^^^^^^^^^^^^

Sub elements
    - effects : list of enchantments.

    - displacedList : Unknown purpose.

The clothing element expects the following variables:

2.4.1.1 Colours group
:::::::::::::::::::::

Each of the following variable must contain a valid ``CLOTHING_`` colour (constant).

Variables
    - ``colour``

    - ``colourSecondary``

    - ``colourTertiary``

2.4.1.2 enchantmentKnown
::::::::::::::::::::::::

No idea. Ask the discord.

Boolean.

2.4.1.3 id
::::::::::

The clothing id. Refer to `Item’s identifier <index.rst>`_.

2.4.1.4 isDirty
:::::::::::::::

Whether the clothing item should spawn dirty, and in need of cleaning.

2.4.1.5 name
::::::::::::

How the item should be displayed. The following example will output to
“Character’s butt-plug”: ``name="[npc.NamePos(true)] butt-plug"``.

2.4.1.6 pattern
:::::::::::::::

The pattern to apply to the item.

2.4.1.7 pattern colour
::::::::::::::::::::::

Each variable must contain a valid ``CLOTHING_`` colour.

- patternColour

- patternColourSecondary

- patternColourTertiary

2.5 genericClothingType
~~~~~~~~~~~~~~~~~~~~~~~

Theses elements automatically populate the possible clothing lists with all
clothing in the game that satisfies the conditionals.

.. code:: xml

    <genericClothingType>
    	<itemTags>
    	  <tag>DRESS</tag>
    	</itemTags>
    	<acceptableFemininities>
    		<femininity>FEMININE</femininity>
    	</acceptableFemininities>
    	<slot/>
    	<rarity>COMMON</rarity>
    	<conditional/>
    	<primaryColours>
    		<colour>presetColourGroup1</colour>
    	</primaryColours>
    	<secondaryColours/>
    	<tertiaryColours/>
    </genericClothingType>

    <genericClothingType> <!-- Generic jewellery. This should probably be used in all outfits, unless you want to manually define your own jewellery. -->
    	<itemTags/>
    	<acceptableFemininities>
    		<femininity>FEMININE</femininity>
    		<femininity>ANDROGYNOUS</femininity>
    	</acceptableFemininities>
    	<slot/>
    	<rarity>COMMON</rarity>
    	<conditional><![CDATA[clothing.getSlot().isJewellery() && (RND.nextInt(100)<=25 || clothing.getSlot()==IS_PIERCING_EAR)]]></conditional>
    	<primaryColours>
    		<colour>presetColourGroup2</colour>
    	</primaryColours>
    	<secondaryColours/>
    	<tertiaryColours/>
    </genericClothingType>

2.5.1 itemTag
^^^^^^^^^^^^^

If tags are defined, then only clothing with the provided tags will be included
for random selection. May be left empty.

Accepted values can be found in the following file:
`src/com/lilithsthrone/game/inventory/ItemTag.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/inventory/ItemTag.java>`_

2.5.1.1 tag
:::::::::::

If the tag contains the constant ``DRESS``, then all items in the game marked as a
``DRESS`` will be included for random selection.

2.5.2 acceptableFemininities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If `1.3 femininity`_ are defined, then only clothing suitable for this femininity
will be included for random selection.

2.5.3 slot
^^^^^^^^^^

If a slot (of type InventorySlot) is defined, then only clothing that fits into
this slot will be included for random selection. Use the Enum values as defined
in `src/com/lilithsthrone/game/inventory/InventorySlot.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/inventory/InventorySlot.java>`_

2.5.4 rarity
^^^^^^^^^^^^

If a rarity is defined, then only clothing that has this rarity will be
included for random selection. Accepted values can be found in the following
file: `src/com/lilithsthrone/game/inventory/Rarity.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/inventory/Rarity.java>`_

2.5.5 conditional
^^^^^^^^^^^^^^^^^

If a condition is defined, then only clothing that satisfies this condition will
be included for random selection. Wrap the conditional statement in ``CDATA`` tags
if used.

In the following logic, earrings have 100% chance to be equipped. All other
jewellery have a 25% chance instead. These items are automatically skipped if
the character doesn’t have the relevant slot accessible. In the case of
jewellery, ears that are not pierced cannot received earrings.

.. code:: java

    clothing.getSlot().isJewellery() && (RND.nextInt(100)<=25 || clothing.getSlot()==IS_PIERCING_EAR)

2.5.6 primary, secondary and tertiary colours
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Three sub elements:

- ``primaryColours``

- ``secondaryColours``

- ``tertiaryColours``

Each accepts a preset color defined earlier in the document.

.. code:: xml

    <primaryColours>
    	<colour>presetColourGroup2</colour>
    </primaryColours>

2.5.7 colours
^^^^^^^^^^^^^

``colours`` elements can be used in addition to, or as a replacement of, the
primary/secondary/tertiary colours elements. Individual colours or
presetColourGroups can be used.

It is defined as follows:

.. code:: xml

    <colours>
    	<colour>presetColourGroup1</colour>
    </colours>

2.6 clothingType
~~~~~~~~~~~~~~~~

Presumably this block filters items based on the list of types, then each
character that satisfy the ``conditional`` sub-element is susceptible to be
selected.

The colour references serves as a list of preset colours for this outfit’s
condional.

The constant present in the ``type`` sub-elements are capitalized references to
the item’s path, minus the name of the author. As such, for an item lying in
``res/clothing/innoxia/chest/lacy_plunge_bra.xml``, it’s type constant will be
``CHEST_LACY_PLUNGE_BRA``.

Both ``genericClothingType`` and ``clothingType`` are shuffled together before being
run through and worn. So if two items occupies the same slot, as for example
several bra, then only one of them will be chosen at random.

``primaryColours`` sub-element has an optional attribute ``value``, which can be
used as a pre-set colour list instead of defining individual colours.

`https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/utils/ColourListPresets.java <https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/utils/ColourListPresets.java>`_

.. code:: xml

    <clothingType>
    	<conditional><![CDATA[npc.hasBreasts()]]></conditional>
    	<types>
    		<type>CHEST_PLUNGE_BRA</type>
    		<type>CHEST_LACY_PLUNGE_BRA</type>
    		<type>CHEST_FULLCUP_BRA</type>
    	</types>
    	<primaryColours values="LINGERIE"/>
    	<secondaryColours/>
    	<tertiaryColours/>
    </clothingType>

    <clothingType>
    	<conditional><![CDATA[npc.getFemininityValue()<75]]></conditional>
    	<types>
    		<type>FOOT_HEELS</type>
    	</types>
    	<primaryColours>
    		<colour>presetColourGroup2</colour>
    	</primaryColours>
    	<secondaryColours/>
    	<tertiaryColours/>
    </clothingType>

    <clothingType>
    	<conditional><![CDATA[npc.getFemininityValue()>=75]]></conditional>
    	<types>
    		<type>FOOT_STILETTO_HEELS</type>
    	</types>
    	<primaryColours>
    		<colour>presetColourGroup2</colour>
    	</primaryColours>
    	<secondaryColours/>
    	<tertiaryColours/>
    </clothingType>

    <clothingType>
    	<conditional><![CDATA[cond1]]></conditional>
    	<types>
    		<type>FINGER_RING</type>
    	</types>
    	<primaryColours>
    		<colour>presetColourGroup2</colour>
    	</primaryColours>
    	<secondaryColours/>
    	<tertiaryColours/>
    </clothingType>

    <clothingType>
    	<conditional><![CDATA[!cond1 || cond2]]></conditional>
    	<types>
    		<type>NECK_HEART_NECKLACE</type>
    	</types>
    	<primaryColours>
    		<colour>presetColourGroup2</colour>
    	</primaryColours>
    	<secondaryColours/>
    	<tertiaryColours/>
    </clothingType>
