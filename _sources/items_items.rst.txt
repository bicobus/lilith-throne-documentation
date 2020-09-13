==================
Miscanelaous Items
==================

    :Author: innoxia, bicobus

.. contents::

Please note: Item modding is not fully complete yet, as you cannot define any enchantment effects for items. I will expand this at some point in the future, but for now, this modding framework should be enough for most uses.

.. _boolean-values:

1 Boolean Values
----------------

Boolean values can be used throughought the elements of this document. Those
values are to be understood as:

- true

- false

2 coreAttributes
----------------

2.1 authorTag
~~~~~~~~~~~~~

How attribution to the mod author (you!) should be displayed in the item’s
tooltip. If left blank or not included, a default attribution based on folder
name will be used.

This tag is optionnal.

.. code:: xml

    <authorTag><![CDATA[A small name stamped on one side of the pill reads 'Inno-Industries'.]]></authorTag>

2.2 value
~~~~~~~~~

How much this item is worth.

.. code:: xml

    <value>20</value>

2.3 determiner
~~~~~~~~~~~~~~

What’s appended before the item’s name in an instance of “Innoxia has X Breeder
Pill”, where X is the determiner. This will usually be either “a” or “an”, but
for other items may be different.

An example might be: “Innoxia is holding X scissors”, where X (the determiner)
would now need to be “a pair of”.

.. code:: xml

    <determiner><![CDATA[a]]></determiner>

2.4 name
~~~~~~~~

The singular name of this item.

.. code:: xml

    <name><![CDATA[breeder pill]]></name>

2.5 namePlural
~~~~~~~~~~~~~~

The plural name of this item.

The argument ``pluralByDefault`` defines whether the item will always be refered
by it’s plural name (e.g. “a pair of pants”). The argument accepts `boolean-values`_.

.. code:: xml

    <namePlural pluralByDefault="false"><![CDATA[breeder pills]]></namePlural>

2.6 description
~~~~~~~~~~~~~~~

The description/lore of this item.

.. code:: xml

    <description><![CDATA[A small, light-purple pill, individually packaged in a foil and plastic wrapper. While the text printed on the foil identifies this pill as an 'Orally-Administered Reproduction Enhancer', it's colloquially known as a 'breeder pill', and temporarily boosts both fertility and virility when ingested.]]></description>

2.7 useDescriptor
~~~~~~~~~~~~~~~~~

How the item is used. This should be a single verb, and is used as the title of
the action when using it.

.. code:: xml

    <useDescriptor>swallow</useDescriptor>

2.8 sexUse
~~~~~~~~~~

Define whether the item can be used during sex, like a dildo or a pill.

This element accepts `boolean-values`_.

.. code:: xml

    <sexUse>true</sexUse>

2.9 combatUseAllies
~~~~~~~~~~~~~~~~~~~

Define whether the item can be used, either on yourself or your allies, during
combat.

This element accepts `boolean-values`_.

.. code:: xml

    <combatUseAllies>true</combatUseAllies>

2.10 combatUseEnemies
~~~~~~~~~~~~~~~~~~~~~

Define whether the item can be used on your opponents during combat.

This element accepts `boolean-values`_.

.. code:: xml

    <combatUseEnemies>false</combatUseEnemies>

2.11 consumedOnUse
~~~~~~~~~~~~~~~~~~

Define whether the item should be consumed on use. *(Editor Note: is it a consumable?)*

This element accepts `1 Boolean Values`_.

.. code:: xml

    <consumedOnUse>true</consumedOnUse>

2.12 rarity
~~~~~~~~~~~

The rarity of this item. Values can be found here:
`src/com/lilithsthrone/game/inventory/Rarity.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/inventory/Rarity.java>`_

.. code:: xml

    <rarity>COMMON</rarity>

2.13 imageName
~~~~~~~~~~~~~~

The file name of this item’s image when in the character’s inventory. The only
supported file type is .svg. I use the free program “Inkscape” to make .svg
images for the game.

.. code:: xml

    <imageName>pill.svg</imageName>

2.14 colours
~~~~~~~~~~~~

Your item can be coloured any way you like, but if you’d like the game to
automatically re-colour your item, you can specify available colours here.

- *Red* is used as base colour for the primary colour of the graphic in-game,
  and the game will only recognise and change the following colours:

  - #ff2a2a

  - #ff5555

  - #ff8080

  - #ffaaaa

  - #ffd5d5

- *Orange* is used as base colour for the secondary colour of the graphic
  in-game, and the game will only recognise and change the following colours:

  - #ff7f2a

  - #ff9955

  - #ffb380

  - #ffccaa

  - #ffe6d5

- *Yellow* is used as base colour for the tertiary colour of the graphic
  in-game, and the game will only recognise and change the following colours:

  - #ffd42a

  - #ffdd55

  - #ffe680

  - #ffeeaa

  - #fff6d5

**any gradients that you use should be called:** ``innoGrad1``, ``innoGrad2``, etc.

A visual representation of these colours is available on the `wiki <https://www.lilithsthrone.com/wiki/doku.php?id=modding_wiki:modding:creating_clothes>`_.

Colour lists to be used can be found here: `src/com/lilithsthrone/utils/colours <https://github.com/Innoxia/liliths-throne-public/tree/dev/src/com/lilithsthrone/utils/colours>`_

Each defaults to ``CLOTHING_BLACK``.

.. code:: xml

    <colourPrimary>CLOTHING_PURPLE_LIGHT</colourPrimary>
    <colourSecondary/>
    <colourTertiary/>

2.15 effectTooltipLines
~~~~~~~~~~~~~~~~~~~~~~~

You can use this section to describe any extra features of this item. These
effects are shown in the tooltip when the player hovers over the item icon, so
try and keep them short (as they should fit on one line). It should probably
only be used to describe what happens in the `apply-effects`_ element. No characters
are passed in as parsing arguments, so you should NOT use any character-specific
parsing elements (such as ``[npc.name]``).

.. code:: xml

    <effectTooltipLines>
    	<line><![CDATA[[#ATTRIBUTE_FERTILITY.getFormattedValue(50)] for 24 hours]]></line>
    	<line><![CDATA[[#ATTRIBUTE_VIRILITY.getFormattedValue(50)] for 24 hours]]></line>
    	<line><![CDATA[[style.boldBad(Removes status effect:)]]]></line>
    	<line><![CDATA['<i>[#SE_PROMISCUITY_PILL.getName(null)]</i>']]></line>
    </effectTooltipLines>

.. _apply-effects:

2.16 applyEffects
~~~~~~~~~~~~~~~~~

This is what is called and parsed every time this item is used on someone. The
character being subjected to the effects is given the tag ``npc``, while the
character using the item on the target is ``npc2``. If self-using the item, ``npc``
and ``npc2`` will be the same character. All of the returned text is displayed to
the player.

.. code:: xml

    <applyEffects><![CDATA[
    	[##npc.removeStatusEffect(SE_PROMISCUITY_PILL)]
    	[##npc.addStatusEffect(SE_VIXENS_VIRILITY, 60*24*60)]
    	<p style='margin-bottom:0; padding-bottom:0;'>
    		The small pill easily slides down [npc.her] throat, and within moments [npc.she] [npc.verb(feel)]
    		#IF(npc.hasVagina())
    			 a soothing, warm glow spreading out from [npc.her] ovaries into [npc.her] lower torso. [npc.Her] mind fogs over with an overwhelming desire to feel potent sperm spurting deep into [npc.her]
    			#IF(npc.isVisiblyPregnant())
    				 pussy,
    			#ELSE
    				 womb,
    			#ENDIF
    			 and before [npc.she] can stop it, a horny whimper escapes from between [npc.her] [npc.lips].
    			#IF(npc.hasPenisIgnoreDildo())
    				 At the same time, [npc.her] manhood begins to throb with need, and [npc.she] [npc.verb(feel)]
    			#ENDIF
    		#ENDIF
    		#IF(npc.hasPenisIgnoreDildo())
    			 an overpowering desire to sink deep into a fertile female's cunt and fill her with [npc.cum+].
    		#ENDIF
    		#IF(!npc.hasPenisIgnoreDildo() && !npc.hasVagina())
    			a desperate heat in [npc.her] genderless mound.
    		#ENDIF
    	</p>
    	<p style='text-align:center; margin-top:0; padding-top:0;'>
    		[style.colourPinkLight([npc.Name] [npc.is] now experiencing <i>'[#SE_VIXENS_VIRILITY.getName(npc)]'</i> for the next 24 hours!)]
    	</p>
    ]]></applyEffects>

.. _item-tags:

2.17 itemTags
~~~~~~~~~~~~~

Special item tags that apply to this item. Values can be found here: `src/com/lilithsthrone/game/inventory/ItemTag.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/inventory/ItemTag.java>`_

.. code:: xml

    <itemTags>
    	<tag>DOMINION_ALLEYWAY_SPAWN</tag>
    	<tag>SUBMISSION_TUNNEL_SPAWN</tag>
    	<tag>BAT_CAVERNS_SPAWN</tag>
    	<tag>ATTRIBUTE_TF_ITEM</tag>
    	<tag>SOLD_BY_RALPH</tag>
    </itemTags>

3 useDescription
----------------

Descriptions that are displayed when using this item.

``selfUse``
    is used when a character uses this item on themselves

``otherUse``
    is used when the item is applied on someone else.

You must define at least one of both of these elements, and if more than one of
each is defined, then the use description will be chosen randomly from all those
you’ve defined.

.. code:: xml

    <useDescriptions>
    	<selfUse><![CDATA[
    	[npc.Name] [npc.verb(pop)] a breeder pill out of its little foil wrapper, before quickly placing it in [npc.her] mouth and swallowing it down.
    	]]></selfUse>
    	<otherUse><![CDATA[
    	[npc.Name] [npc.verb(pop)] a breeder pill out of its little foil wrapper, before bringing it up to [npc2.namePos] [npc2.lips], forcing it into [npc2.her] mouth, and making sure that [npc2.she] [npc2.verb(swallow)] it down.
    	]]></otherUse>
    </useDescriptions>
