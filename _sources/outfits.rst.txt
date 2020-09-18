.. highlight:: xml

.. `outfits`_

=======
Outfits
=======

    :Authors: innoxia, bicobus

Outfits are a way to make randomly generated NPCs’ outfit generation less
chaotic.

As a final note, I will add support for allowing the automatic generation of
piercings in the next update.

An annotated example lives at
:ltgithub:`res/mods/innoxia/outfits/casualDates/dress_toys.xml`

coreAttributes
--------------

name
~~~~

Names are only used for debugging purposes. Still, in case the name is used
elsewhere later on, it’s best to give your outfit a suitable (lowercase) name.

.. code:: xml

    <name><![CDATA[casual dress with toys]]></name>

description
~~~~~~~~~~~

Again, descriptions are only used for debugging purposes. Still, in case the
name is used elsewhere later on, it’s best to give your outfit a suitable
description.

.. code:: xml

    <description><![CDATA[A dress hides the fact that the wearer has a toy or two inserted into their orifices...]]></description>

femininity
~~~~~~~~~~

The femininity needed for someone to generate this outfit.

The three acceptables values are respectively:

1. ``MASCULINE``

2. ``ANDROGYNOUS`` (anyone can use this outfit)

3. ``FEMININE``

.. code:: xml

    <femininity>FEMININE</femininity>

worldTypes
~~~~~~~~~~

The worlds in which this outfit may be used for randomly generated characters.
You can leave this empty, or delete the element entirely, if you do not want
this outfit to be restricted based on ``WorldType`` (so it can be used
anywhere).

.. seealso::
   :ltgithub:`src/com/lilithsthrone/world/WorldType.java`.

.. code:: xml

    <worldTypes>
    	<world>DOMINION</world>
    	<world>SUBMISSION</world>
    </worldTypes>

outfitTypes
~~~~~~~~~~~

Outfit types that this outfit can be used in.

.. seealso::
   A list of :ltgithub:`outfitTypes<src/com/lilithsthrone/game/inventory/clothing/OutfitType.java>`.

.. Caution::

   At the time of creation (*v0.3.0.6*), only the ``MUGGER`` outfitType is used
   in the game. All outfit types will be added eventually.

.. code:: xml

    <outfitTypes>
    	<type>CASUAL_DATE</type>
    </outfitTypes>

acceptableLegConfigurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define which leg configurations can equip this outfit.

.. seealso::

   A list of :ltgithub:`legConfiguration<src/com/lilithsthrone/game/character/body/valueEnums/LegConfiguration.java>`.

.. code:: xml

    <acceptableLegConfigurations>
    	<legConfiguration>BIPEDAL</legConfiguration>
    </acceptableLegConfigurations>

conditional
~~~~~~~~~~~

The condition that needs to be satisfied for someone to generate this outfit.
``npc.hasFetish(FETISH_EXHIBITIONIST)`` should probably always be taken into
account. This conditional instance does **not** support the
``clothingConditionalX`` elements.

.. seealso::

   - List of accepted
     :ltgithub:`method calls<src/com/lilithsthrone/game/character/GameCharacter.java>`
     for the “npc” (using the ``npc`` tag).

   - List of accepted :ltgithub:`method calls<src/com/lilithsthrone/game/Game.java>`
     for the main game (using the ``game`` tag).
   - Generic method calls can be found in:
     :ltgithub:`src/com/lilithsthrone/game/dialogue/utils/UtilText.java`

The method ``initScriptEngine()`` in ``UtilText.java`` shows you what you can get a
handle on.

.. code:: xml

    <conditional><![CDATA[!npc.hasFetish(FETISH_EXHIBITIONIST) && npc.hasFetish(FETISH_MASTURBATION) && npc.getFetishDesire(FETISH_SUBMISSIVE).isPositive()]**></conditional>

weight
~~~~~~

How likely this outfit is to be randomly chosen out of all available ones.
Default outfits have a weight of 100. As there could be several outfits added to
the weighting method, the chance of this outfit being selected is not able to be
precisely determined.

A bigger number makes the outfits more common. There is no upper limit.

.. code:: xml

    <weight>100</weight>

generationAttributes
--------------------

Conditional statements
~~~~~~~~~~~~~~~~~~~~~~

**Node Variables:**
    .. nodevar:: constant <Boolean> (True)

        Conditional statements are evaluated only one time, at the start of
        clothing generation, unless this variable is set to ``False``.

You can define any number of conditional statements to use elsewhere in this
file. They must be enclosed in ``CDATA`` tags, and must use a format of
``clothingConditionalX`` or ``condX``, where ``X`` is a unique ``String`` (e.g.
``cond1``, ``condUnderwear``, ``clothingConditionalMeleeWeapons`` are all valid
tags).

Example
    .. code:: xml

        <cond1 constant="true"><![CDATA[RND.nextInt(100)<=50]]></cond1>
        <cond2 constant="true"><![CDATA[RND.nextInt(100)<=75]**></cond2>

presetColourGroups
~~~~~~~~~~~~~~~~~~

**Node Variables:**
    .. nodevar:: [singleColour] <Boolean> (False)

        The optional :nodevar:`singleColour` attribute, when set to ``True``,
        means that this group will always return the same, randomly chosen
        colour from its list.

Preset colour groups have one of their defined ``randomColour`` randomly chosen
for further use in this XML file. You can have up to 20 ``presetColourGroupX``,
however the numbers must be consecutive. (i.e. You can have
``presetColourGroup1``, ``presetColourGroup2``, and ``presetColourGroup3``, but
**not** ``presetColourGroup1``, ``presetColourGroup2``, and
``presetColourGroup4``, as that skips out a “3”.)

Accepted values can be found in the files present in the
:ltgithub:`src/com/lilithsthrone/utils/colours` diretory.

Preceding ``presetColourGroups`` can be used, but not succeeding ones. (i.e.
``presetColourGroup3`` could not be used in ``presetColourGroup2``.)

.. code:: xml

    <presetColourGroup1 singleColour="true">
    	<randomColour>CLOTHING_PINK</randomColour>
    	<randomColour>CLOTHING_PINK_LIGHT</randomColour>
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

mainWeapons and offhandWeapons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Weapons can be added in a similar (although more limited) manner to clothing.
This file doesn’t use any weapons. Look at
:ltgithub:`res/outfits/innoxia/genericMugger/dominion_masculine.xml` for a
weapon example.

The content present in ``mainWeapons`` and ``offhandWeapons`` follow the same
rules. The main weapons block defines which item should be inserted into the
character’s main attack slot, where ass the off hand block defines which item to
be inserted into the character’s off hand. Each block receive one or several
``weapon`` sub elements.

The ``weapon`` block require the following elements to be present:

``conditional``
    references to the conditional statement present in the document.

``types``
    A list of valid item to be chosen from. It expects :ref:`items
    identifiers<items-identifier>`.

``damageTypes``
    Possible choices available at
    :ltgithub:`src/com/lilithsthrone/game/combat/DamageType.java`

``primaryColours``
    contains a list of ``colour`` elements, which makes references to the preset
    groups defined previously.

``secondaryColours``
    contains a list of ``colour`` elements, which makes references to the preset
    groups defined previously.

``colours``
    element can be used in addition to, or as a replacement of, the
    primary/secondary/tertiary colours elements.

Individual colours or ``presetColourGroups`` can be listed in each sub-element
related to colours.

.. code-block:: xml
   
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
            </primaryColours>
            <secondaryColours/>
            <colours>
                <colour>presetColourGroup1</colour>
            </colours>
        </weapon>
    </mainWeapons>

The element ``offhandWeapons`` follow a similar ruleset.

.. code:: xml

    <offhandWeapons/>

guaranteedClothingEquips
~~~~~~~~~~~~~~~~~~~~~~~~

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
    		<clothing colour="presetColourGroup2" colourSecondary="CLOTHING_BLACK" colourTertiary="CLOTHING_BLACK" enchantmentKnown="true" id="innoxia_vagina_insertable_dildo" isDirty="false" name="[npc.NamePos(true)** insertable dildo"></clothing>
    	</uniqueClothing>
    </guaranteedClothingEquips>

clothing
^^^^^^^^

**Node Variables**:
    .. nodevar:: colour <constant> ()

    .. nodevar:: colourSecondary <constant> ()

    .. nodevar:: colourTertiary <constant> ()

    .. nodevar:: patternColour <constant> ()

    .. nodevar:: patternColourSecondary <constant> ()

    .. nodevar:: patternColourTertiary <constant> ()

        All colours variables must contain a valid ``CLOTHING_`` colour.

    .. nodevar:: enchantmentKnown <boolean> ()

        Determine if the effects on the item are known to the
        player, or if the item remains unidentified.

    .. nodevar:: id <string> ()

        The clothing ID

        .. seealso:: :ref:`items-identifier`

    .. nodevar:: isDirty <boolean> ()

        Whether the clothing item should spawn dirty, and in need of cleaning.

    .. nodevar:: [name] <string> ()

        How the item should be displayed. The following example will output to
        “Character’s butt-plug”: ``name="[npc.NamePos(true)] butt-plug"``. If
        not present, the name of the clothing is used instead.

    .. nodevar:: [pattern] <string> ()

        The pattern to apply to the item.

The clothing tags has the following sub elements.

effects
:::::::

List of enchantments.

displacedList
:::::::::::::

Define in which state a piece of clothing is being equipped.

::

   <displacedList>
        <displacementType value="UNBUTTONS"/>
    </displacedList>

**displacementType Variables:**
    .. nodevar:: value <constant> ()

       The list of constants is available at
       :ltgithub:`src/com/lilithsthrone/game/inventory/clothing/DisplacementType.java`

genericClothingType
~~~~~~~~~~~~~~~~~~~

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

itemTag
^^^^^^^

If tags are defined, then only clothing with the provided tags will be included
for random selection. May be left empty.

Accepted values can be found in the following file:
`src/com/lilithsthrone/game/inventory/ItemTag.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/inventory/ItemTag.java>`_

tag
:::

If the tag contains the constant ``DRESS``, then all items in the game marked as
a ``DRESS`` will be included for random selection.

acceptableFemininities
^^^^^^^^^^^^^^^^^^^^^^

If `femininity`_ are defined, then only clothing suitable for this femininity
will be included for random selection.

slot
^^^^

If a slot (of type InventorySlot) is defined, then only clothing that fits into
this slot will be included for random selection. Use the Enum values as defined
in :ltgithub:`src/com/lilithsthrone/game/inventory/InventorySlot.java`.

rarity
^^^^^^

If a rarity is defined, then only clothing that has this rarity will be
included for random selection. Accepted values can be found in the following
file: :ltgithub:`src/com/lilithsthrone/game/inventory/Rarity.java`.

conditional
^^^^^^^^^^^

If a condition is defined, then only clothing that satisfies this condition will
be included for random selection. Wrap the conditional statement in ``CDATA``
tags if used.

In the following logic, earrings have 100% chance to be equipped. All other
jewellery have a 25% chance instead. These items are automatically skipped if
the character doesn’t have the relevant slot accessible. In the case of
jewellery, ears that are not pierced cannot received earrings.

.. code:: java

    clothing.getSlot().isJewellery() && (RND.nextInt(100)<=25 || clothing.getSlot()==IS_PIERCING_EAR)

primary, secondary and tertiary colours
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Three sub elements:

- ``primaryColours``

- ``secondaryColours``

- ``tertiaryColours``

Each accepts a preset color defined earlier in the document.

.. code:: xml

    <primaryColours>
    	<colour>presetColourGroup2</colour>
    </primaryColours>

colours
^^^^^^^

``colours`` elements can be used in addition to, or as a replacement of, the
primary/secondary/tertiary colours elements. Individual colours or
presetColourGroups can be used.

It is defined as follows:

.. code:: xml

    <colours>
    	<colour>presetColourGroup1</colour>
    </colours>

clothingType
~~~~~~~~~~~~

Presumably this block filters items based on the list of types, then each
character that satisfy the ``conditional`` sub-element is susceptible to be
selected.

The colour references serves as a list of preset colours for this outfit’s
condional.

The constants present in the ``type`` sub-elements are either hard coded
constants or :ref:`items-identifier`.

.. caution:: Some piece of clothing haven't been (yet) converted into a XML
             format, those have hard coded types available at
             :ltgithub:`src/com/lilithsthrone/game/inventory/clothing/ClothingType.java`

Both ``genericClothingType`` and ``clothingType`` are shuffled together before
being run through and worn. So if two items occupies the same slot, as for
example several bra, then only one of them will be chosen at random.

``primaryColours`` sub-element has an optional attribute ``value``, which can be
used as a pre-set colour list instead of defining individual colours.

.. seealso::
   :ltgithub:`src/com/lilithsthrone/utils/colours/ColourListPresets.java`


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
