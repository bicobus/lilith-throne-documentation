=============
Items Weapons
=============

    :Author: innoxia, bicobus

coreAttributes
--------------

authorTag
~~~~~~~~~

How attribution to the mod author (*you*) should be displayed in the item’s
tooltip. If left blank or not included, a default attribution based on folder
name will be used.

This tag is optionnal.

.. code:: xml

    <authorTag><![CDATA[A discreet inscription at the base of the dagger's blade informs you that it was made by 'Innoxia'.]]></authorTag>

value
~~~~~

How much this weapon is worth.

.. code:: xml

    <value>3000</value>

melee
~~~~~

Use “true” if this is a melee weapon, and “false” if it’s ranged. (Without
quotation marks.)

.. code:: xml

    <melee>true</melee>

twoHanded
~~~~~~~~~

Use “true” if this weapon is two-handed, and thus cannot be simultaneously
wielded with an offhand weapon, and “false” if it’s one-handed. (Without
quotation marks.)

.. code:: xml

    <twoHanded>false</twoHanded>

determiner
~~~~~~~~~~

What’s appended before the weapon’s name in an instance of “Innoxia was holding
X Demon’s Dagger”, where X is the determiner. This will usually be either “a” or
“an”, but for other weapons may be different.

An example might be: “Innoxia was holding X scissors”, where X (the determiner)
would now need to be “a pair of”.

.. code:: xml

    <determiner><![CDATA[a]]></determiner>

name
~~~~

The name of this weapon.

``appendDamageName``
    defaults to true and can be left out. If you ever want this weapon to not be
    described by its damage type, then set it as false. That is this dagger
    would always be called “Demon’s Dagger” instead of, for example, “Forceful
    Demon’s Dagger”.

.. code:: xml

    <name appendDamageName="true"><![CDATA[Demon's Dagger]]></name>

namePlural
~~~~~~~~~~

The plural name of this weapon.

``pluralByDefault``
    If set to ``true``, then the game will always use the plural name when
    referring to this weapon.

.. code:: xml

    <namePlural pluralByDefault="false"><![CDATA[Demon's Daggers]]></namePlural>

description
~~~~~~~~~~~

The description/lore of this weapon.

.. code:: xml

    <description><![CDATA[A demon's dagger, with a blade made out of enchanted ethereal energy. Daggers such as this one are carried by the elite demon Enforcers, and, while intended primarily to be a symbol of power and status, they are nonetheless completely functional.]]></description>

attackDescriptor
~~~~~~~~~~~~~~~~

How the weapon is used. This should be a single verb, and is used as the title
of attacking actions in combat.

.. code:: xml

    <attackDescriptor>stab</attackDescriptor>

attackTooltipDescription
~~~~~~~~~~~~~~~~~~~~~~~~

The description that’s displayed when hovering over the attack action in combat.
Follow the same guidelines as equipText (a couple of entries further down this
page).

As this tooltip is only ever seen from the player’s perspective, you can always
write in the first-person narrative. (Still use npc2 for the target, though.)

.. code:: xml

    <attackTooltipDescription><![CDATA[Strike out with your Demon's Dagger at [npc2.name].]]></attackTooltipDescription>

rarity
~~~~~~

The rarity of this weapon.

Values can be found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/Rarity.java`

.. code:: xml

    <rarity>EPIC</rarity>

weaponSet
~~~~~~~~~

Which set this weapon is a part of.

Values can be found here: :ltgithub:`/res/setBonuses/`

.. seealso::

   :doc:`/setBonuses`

.. code:: xml

    <weaponSet/>

1.13 equipText
~~~~~~~~~~~~~~

The description that’s used when equipping this weapon. The description should
be generic, able to be used by both the player and NPCs. Just make sure to use
the tag ``[npc.verb()]`` whenever using a verb, which will then, for example,
parse like this:

- ``[npc.verb(run)]`` if npc is player = “run”

- ``[npc.verb(run)]`` if npc is not the player = “runs”

Always use the first-person singular verb.

The target ``npc`` OR ``npc1`` should be used for the character using the weapon.
e.g. If the player is the one attacking (and is called Innoxia), then
``[npc.Name]`` will return “Innoxia”.

The target ``npc2`` should be used for the character being attacked. e.g. If Brax
is the one being attacked, then ``[npc2.Name]`` will return “Brax”.

.. code:: xml

    <equipText><![CDATA[[npc.Name] [npc.verb(unsheathe)] the dagger, readying it for use in combat.]]></equipText>

1.14 unequipText
~~~~~~~~~~~~~~~~

The description that’s used when equipping this weapon. Follow the same
guidelines as equipText.

.. code:: xml

    <unequipText><![CDATA[[npc.Name] [npc.verb(sheathe)] the dagger, before putting it away.]]></unequipText>

1.15 imageName
~~~~~~~~~~~~~~

The file name of this weapon’s image when in the character’s inventory. The only
supported file type is .svg. I use the free program “Inkscape” to make .svg
images for the game.

.. code:: xml

    <imageName>dagger_sheathed.svg</imageName>

1.16 imageEquippedname
~~~~~~~~~~~~~~~~~~~~~~

The file name of this weapon’s image when equipped. Can be (and usually is) the
same as the imageName (which in this example would be ``dagger_sheathed.svg``).

.. code:: xml

    <imageEquippedName>dagger.svg</imageEquippedName>

1.17 physicalResistance
~~~~~~~~~~~~~~~~~~~~~~~

How much natural physical resistance this weapon provides when equipped. Should
only really be above 0 for shields or other such protective weapons.

.. code:: xml

    <physicalResistance>0</physicalResistance>

1.18 damage
~~~~~~~~~~~

The base damage that this weapon deals.

.. code:: xml

    <damage>20</damage>

If you want to define additional AoE damages, add ``aoe`` elements.

A working example of AoE damages can be found in
``res/weapons/innoxia/lightningGlobe/lightning_globe.xml``.

.. code:: xml

    <aoe chance="50">10</aoe> 50% chance of hitting an additional enemy (who has not been hit yet) for 10 damage
    <aoe chance="25">5</aoe> 25% chance of hitting an additional enemy (who has not been hit yet) for 5 damage

1.19 arcaneCost
~~~~~~~~~~~~~~~

How many arcane essences are required, and drained, by firing this weapon.
Ranged weapons should usually use the value 1, while melee weapons should
usually be 0.

.. code:: xml

    <arcaneCost>0</arcaneCost>

1.20 damageVariance
~~~~~~~~~~~~~~~~~~~

The variance in base damage when this weapon is actually used to attack.

Values can be found here:
`https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/game/combat/DamageVariance.java <https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/game/combat/DamageVariance.java>`_

.. code:: xml

    <damageVariance>MEDIUM</damageVariance>

1.21 availableDamageTypes
~~~~~~~~~~~~~~~~~~~~~~~~~

The available damage types that this weapon can spawn in with.

Values can be found here (MISC should not be used):
`src/com/lilithsthrone/game/combat/DamageType.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/combat/DamageType.java>`_

.. code:: xml

    <availableDamageTypes>
    	<damageType>PHYSICAL</damageType>
    	<damageType>ICE</damageType>
    	<damageType>FIRE</damageType>
    	<damageType>POISON</damageType>
    </availableDamageTypes>

.. _spells:

1.22 spells
~~~~~~~~~~~

The spells that are unlocked when equipping this weapon. IF you want to add any,
use the format:

.. code:: xml

    <spells changeOnReforge="true"> <!-- ref:cor -->
    	<spell damageType="FIRE">FIREBALL</spell> <!-- ref:dmt -->
    	<spell damageType="ICE">ICE_SHARD</spell>
    	<spell damageType="LUST">ARCANE_AROUSAL</spell>
    	<spell damageType="PHYSICAL">SLAM</spell>
    	<spell damageType="POISON">POISON_VAPOURS</spell>
    </spells>

The changeOnReforge variable determines whether this weapon should regenerate
spells whenever the player changes the damage type. (i.e. If they reforge a
``FIRE`` dagger to an ``ICE`` dagger, if changeOnReforge is true, then the granted
spell ``FIREBALL`` will automatically switch to ``ICE_SHARD``).

The damageType variable corresponds to the damageType which causes the spell to
be unlocked when this weapon is spawned in. You can have multiple entries of the
same damageType, like so:

.. code:: xml

    <spell damageType="FIRE">FIREBALL</spell>
    <spell damageType="FIRE">FLASH</spell>
    <spell damageType="FIRE">ICE_SHARD</spell>
    <spell damageType="FIRE">STEAL</spell>

Note that the ``damageType`` does not have to correspond to the spell’s school (so
``FIRE`` can unlock ``ICE_SHARD``, etc.).

Values for spells can be found here: `https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/game/combat/Spell.java <https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/game/combat/Spell.java>`_

For an empty spell list, use an empty element:

.. code:: xml

    <spells/>

.. _combat-moves:

1.23 combatMoves
~~~~~~~~~~~~~~~~

The combat moves that are unlocked when equipping this weapon. The ``combatMoves``
element is similar to the `spells`_ element.

.. code:: xml

    <combatMoves changeOnReforge="true">
    	<move damageType="PHYSICAL">ASSAULT_RIFLE_MAG_DUMP</move>
    </combatMoves>

The changeOnReforge variable determines whether this weapon should regenerate
combat moves whenever the player changes the damage type. Using the example
above, if they reforge a ``PHYSICAL`` dagger to an ``ICE`` dagger and
changeOnReforge is true, then the granted combat move ``ASSAULT_RIFLE_MAG_DUMP``
will be lost.

The damageType variable corresponds to the damageType which causes the move to
be unlocked when this weapon is spawned in. You can have multiple entries of the
same damageType, like so:

.. code:: xml

    <move damageType="FIRE">EXAMPLE_MOVE_1</move>
    <move damageType="FIRE">EXAMPLE_MOVE_2</move>
    <move damageType="FIRE">EXAMPLE_MOVE_3</move>
    <move damageType="FIRE">EXAMPLE_MOVE_4</move>

Values for combat moves can be found here: `https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/game/combat/CMWeaponSpecials.java <https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/game/combat/CMWeaponSpecials.java>`_

**Note:** combat moves are not yet moddable. There will be a way to add modded
combat moves soon!

For an item with no combat move, simply write an empty element:

.. code:: xml

    <combatMoves/>

1.24 enchantmentLimit
~~~~~~~~~~~~~~~~~~~~~

How many effects this weapon can be enchanted with. Weapons standard is 5, for
balance purpose.

.. code:: xml

    <enchantmentLimit>5</enchantmentLimit>

1.25 effects
~~~~~~~~~~~~

The effects that this weapon spawns in with. Remember that the player can
remove, change or add effects. To know what to put in here, it would probably be
easiest to enchant clothing in your game, save the game, then copy over that
clothing’s ’effects’ in your save file.

There are two special values for secondaryModifier, which are:

``RESISTANCE_WEAPON``
    applies the related resistance of this weapon’s damage
    type.

``DAMAGE_WEAPON``
    applies the related damage type.

For example, if this dagger spawned in as type ``POISON``, and I’d replaced both
instances of ``CRITICAL_CHANCE`` with ``DAMAGE_WEAPON``, then this dagger would
spawn with two +5 Poison Damage effects.

.. code:: xml

    <effects> 
        <effect itemEffectType="CLOTHING" limit="0" potency="MAJOR_BOOST" primaryModifier="CLOTHING_ATTRIBUTE" secondaryModifier="CRITICAL_CHANCE" timer="0"/>
        <effect itemEffectType="CLOTHING" limit="0" potency="MAJOR_BOOST" primaryModifier="CLOTHING_ATTRIBUTE" secondaryModifier="CRITICAL_CHANCE" timer="0"/>
    </effects>

1.26 extraEffects
~~~~~~~~~~~~~~~~~

You can use this section to describe any extra features of this weapon. These
effects are shown in the tooltip when the player hovers over the weapon icon, so
try and keep them short (as they should fit on one line). It should probably
only be used to describe what happens in the `1.27 onHitEffect`_ element. No characters
are passed in as parsing arguments, so you should **not** use any
character-specific parsing elements (such as ``[npc.name]``). For this weapon, no
extra effects need to be described, but if you need to use this section, use the
following format:

.. code:: xml

    <extraEffects>
    	<effect><![CDATA[Stab time!]]></effect>
    </extraEffects>

Empty extra effect:

.. code:: xml

    <extraEffects/>

.. _on-hit-effect:

1.27 onHitEffect
~~~~~~~~~~~~~~~~

This is applied every time this weapon hits a target. It does **not** apply when
the weapon critically hits. The returned text is appended to the hit
description. ``npc`` corresponds to the attacker, and ``npc2`` to the target, for
use in effects/parsing. For this weapon, no hit effects need to be added, but if
you need to use this section, use the following format:

.. code:: xml

    <onHitEffect><![CDATA[
    [##npc2.setHealth(0)]
    [npc2.Name] is instantly defeated!
    ]]></onHitEffect>

An empty effect

.. code:: xml

    <onHitEffect/>

1.28 onCriticalHitEffect
~~~~~~~~~~~~~~~~~~~~~~~~

This is applied every time this weapon critically hits a target. It does **not**
apply when the weapon does a non-critical hit.

The returned text is appended to the hit description. ``npc`` corresponds to the
attacker, and ``npc2`` to the target, for use in effects/parsing. Use the same
format as `on-hit-effect`_.

.. code:: xml

    <onCriticalHitEffect/>

1.29 colours
~~~~~~~~~~~~

Please consult the relevant `documentation <index.rst>`_ about colours.

Your clothing can be coloured any way you like, but if you’d like the player to
be able to dye your clothing, you can specify available colours here.
``primaryColours`` and ``secondaryColours`` all spawn in as a default colour, while
their ``Dye`` counterparts are only available if the player chooses to dye the
clothing in that colour. The game detects specific colour values, and recolours
them to the value chosen by the player. These values are as follows:

- Red is used as base colour for changing the ``DAMAGE TYPE``’s colour of the
  graphic in-game, and the game will only recognise and change the following
  colours:

  - #ff2a2a

  - #ff5555

  - #ff8080

  - #ffaaaa

  - #ffd5d5

- Orange is used as base colour for changing the ``PRIMARY`` colour of the graphic
  in-game, and the game will only recognise and change the following colours:

  - #ff7f2a

  - #ff9955

  - #ffb380

  - #ffccaa

  - #ffe6d5

- Yellow is used as base colour for changing the ``SECONDARY`` colour of the graphic
  in-game, and the game will only recognise and change the following colours:

  - #ffd42a

  - #ffdd55

  - #ffe680

  - #ffeeaa

  - #fff6d5

- Green is used as base colour for changing the ``TERTIARY`` colour of the graphic
  in-game, and the game will only recognise and change the following colours:

  - #abc837

  - #bcd35f

  - #cdde87

  - #dde9af

  - #eef4d7

As you can see above, weapons differ from clothing in that their ``Red`` colour is
recoloured based on the weapon’s damage type! The ``primaryColours``,
``secondaryColours``, and ``tertiaryColours`` defined below are for recolouring the
``Orange``, ``Yellow``, and ``Green`` values, respectively.

**Any gradients that you use should be called:** ``innoGrad1``, ``innoGrad2``, etc.

You can see a visual representation of these colours (as used in clothing) here:
`https://www.lilithsthrone.com/wiki/doku.php?id=modding_wiki:modding:creating_clothes <https://www.lilithsthrone.com/wiki/doku.php?id=modding_wiki:modding:creating_clothes>`_

Colour lists to be used can be found here:
`https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/utils/ColourListPresets.java <https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/utils/ColourListPresets.java>`_

.. code:: xml

    <primaryColours recolouringAllowed="true" values="JUST_STEEL"/> <!-- You can leave the attribute 'recolouringAllowed' out of colour definitions. If you want the player to be unable to change this colour, then set it as false. This is only used in very niche situations (such as for the filly choker).-->

    <primaryColoursDye values="ALL_METAL"/>
    <secondaryColours values="JUST_BLACK"/>
    <secondaryColoursDye values="ALL"/>

1.30 customColours
~~~~~~~~~~~~~~~~~~

You can define any number of custom colours to replace the shades you’ve
coloured your svg with. If you have used the primary/secondary/tertiary elements
up above, then do not use their associated colour hexes. (i.e. If you’ve defined
a primaryColours element, do not use #ff7f2a, #ff9955, #ffb380, #ffccaa, or
#ffe6d5 in the customColour attributes.)

You should NEVER use the primary recolouring shades, as they are always reserved
for the damage type’s colour: #ff2a2a, #ff5555, #ff8080, #ffaaaa, or #ffd5d5

.. code:: xml

    <customColours>
    	<!-- The 'copyColourIndex' attribute defines which colour index should be copied into this colour slot on weapon generation. This particular colour, having an index of 0, will always be coloured the same as the primary colour when generated. Indexes go from 0->X, where X is the number of defined colours. i.e. If you only define primary and secondary, the first custom colour (i.e. this one) will have an index of 2. -->
    	<customColour copyColourIndex="0" c0="#6C5D53" c1="#917C6F" c2="#AC9D93" c3="#C8BEB7" c4="#E3DEDB">
    		<defaultColours>
    			<colour>CLOTHING_STEEL</colour>
    		</defaultColours>
    		<extraColours values="ALL_METAL"/>
    	</customColour>
    	 <!-- This particular copyColourIndex, having an index of 1, will always be coloured the same as the secondary colour when generated -->
    	<customColour copyColourIndex="1" recolouringAllowed="true" c0="#6C5353" c1="#916F6F" c2="#AC9393" c3="#C8B7B7" c4="#E3DBDB"> <!-- These are the colours which you've used in your svg and would like replaced with the colours you define below. c0 is the darkest shade. Shades can go up to any number, but setting just 5 shades should work best. -->
    		<defaultColours>
    			<colour>CLOTHING_BLACK</colour> <!-- The colours which this clothing should spawn in with. -->
    		</defaultColours>
    		<extraColours values="ALL"/> <!-- The colours which this weapon can be dyed to. -->
    	</customColour>
    </customColours>

1.31 itemTags
~~~~~~~~~~~~~

Special item tags that apply to this weapon. Values can be found here: `https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/game/inventory/ItemTag.java <https://github.com/Innoxia/liliths-throne-public/blob/master/src/com/lilithsthrone/game/inventory/ItemTag.java>`_

.. code:: xml

    <itemTags>
    	<tag>SOLD_BY_VICKY</tag>
    	<tag>WEAPON_BLADE</tag>
    </itemTags>

2 hitDescription
----------------

Descriptions that are used when hitting an enemy. One of the ``hitText`` values
will be randomly selected each time the attacker hits their target. Follow the
same guidelines as ``equipText``.

You can add hit descriptions which will only be shown on a critical hit by using
the ``criticalHitText`` element. This is optional, and you don’t need to define
any critical hit descriptions. If none are define and a critical hit occurs, a
regular ``hitText`` will be used instead.


.. code:: xml

    <hitDescriptions>
    	<hitText><![CDATA[
    	Thrusting out with [npc.her] Demon's Dagger, [npc.name] [npc.verb(manage)] to stab [npc2.name] in the chest; the ethereal arcane blade passing through [npc2.her] torso to drain [npc2.her] energy!
    	]]></hitText>
    	<hitText><![CDATA[
    	Striking out at [npc2.name] with [npc.her] Demon's Dagger, [npc.name] [npc.verb(manage)] to slash through [npc2.her] [npc2.arm] with the ethereal blade and drain [npc2.her] energy!
    	]]></hitText>
    	<hitText><![CDATA[
    	With a quick step forwards, [npc.name] [npc.verb(lunge)] out at [npc2.name] with [npc.her] Demon's Dagger, sinking the ethereal blade into [npc2.her] shoulder and causing [npc2.herHim] to lose some energy!
    	]]></hitText>
    	<criticalHitText><![CDATA[
    	Expertly sidestepping around [npc2.namePos] attempt to block [npc.her] attack, [npc.name] [npc.verb(deal)] a devastating strike with [npc.her] Demon's Dagger!
    	]]></criticalHitText>
    </hitDescriptions>

3 missDescription
-----------------

Descriptions that are used when missing an enemy. One of the missText values will be randomly selected each time the attacker misses their target. Follow the same guidelines as equipText.

.. code:: xml

    <missDescriptions>
    	<missText><![CDATA[
    	Thrusting out with [npc.her] Demon's Dagger, [npc.name] [npc.verb(attempt)] to stab [npc2.name] in the chest, but [npc.verb(end)] up missing [npc2.herHim]!
    	]]></missText>
    	<missText><![CDATA[
    	Striking out at [npc2.name] with [npc.her] Demon's Dagger, [npc.name] [npc.verb(let)] out a frustrated cry as [npc.she] [npc.verb(miss)] [npc.her] target!
    	]]></missText>
    	<missText><![CDATA[
    	With a quick step forwards, [npc.name] [npc.verb(lunge)] out at [npc2.name] with [npc.her] Demon's Dagger, but [npc.she] [npc.verb(miss)] [npc.her] target!
    	]]></missText>
    </missDescriptions>
