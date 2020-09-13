============
statusEffect
============

    :Author: innoxia, bicobus

.. contents::



1 GENERAL INFORMATION
---------------------

Status effects are bits of logic applied to a character. The effect convey
access to a variety of content, like combat moves or spell. They can also change
the attributes of the character.

You can see an annotated example in the file
``res/statusEffects/innoxia/set_kitty.xml``.

2 renderingPriority
-------------------

An integer used for determining the order of rendering status effect icons. A
higher value means that it’s higher up in the rendering priority (and so will be
rendered before others). Typical values go from 0 to 100. A good default value
is to set it as 50. As this status effect is a set bonus, it has a higher
rendering priority than usual (of 70). For some examples of the rendering
priority:

- A character’s racial perk effect has a priority of 1000, as I want it to
  always be rendered first no matter what.

- Weather effects have a priority of 100 (as I want them to always be displayed
  as high as possible).

- Sexual orientation has a priority of 90 (as I want it to be displayed near the
  start).

- Most other standard status effects (such as pregnancy, well-rested, alcohol
  level, etc.) have a priority of 80.

- Set bonuses have a priority of 70.

.. code:: xml

    <renderingPriority>70</renderingPriority>

3 renderInEffectsPanel
----------------------

Set to ``true`` if you want this status effect to be displayed in the affected
character’s status effect panel. This should pretty much always be ’true’.

.. code:: xml

    <renderInEffectsPanel>true</renderInEffectsPanel>

4 beneficial
------------

Populate with one of these tags:

- ``BENEFICIAL`` if this is a good status effect for a character to have.

- ``NEUTRAL`` if it’s neither.

- ``DETRIMENTAL`` if it’s a bad one.

.. code:: xml

    <beneficial>BENEFICIAL</beneficial>

5 combatEffect
--------------

Set to ``true`` if you want this status effect to be rendered during combat, and
if the `15.2 applyEffect`_ element should be applied to the affected character on every
combat round during which it is active. This should only be set to true if this
a status effect which is applied and used **only** in combat. Status effects which
are marked as combat status effects are not ever applied outside of combat.

.. code:: xml

    <combatEffect>false</combatEffect>

6 sexEffect
-----------

Set to ``true`` if you want this status effect to be rendered during sex.

.. code:: xml

    <sexEffect>false</sexEffect>

7 name
------

The name of this set bonus. The character under the effect is passed in as the
``npc`` parsing argument, so if you want to, you can include parsing elements such
as ``[npc.name]``.

.. code:: xml

    <name><![CDATA[Socks of Power]]></name>

8 description
-------------

The description of this status effect. The character under the effect is passed
in as the ``npc`` parsing argument, so if you want to, you can include parsing
elements such as ``[npc.name]``.

.. code:: xml

    <description><![CDATA[
        By wearing the template socks, you become a sock god#IF(npc.isFeminine())dess#ENDIF!
    ]]></description>

9 imageName
-----------

The name of the icon which should be used to represent this status effect. The
icon must be an svg file, and must be placed in the same folder as this XML
file.

.. code:: xml

    <imageName>set_template.svg</imageName>

10 colours
----------

The colour which should be associated with this status effect. Just like with
clothing and weapon recolouring, this is used to recolour the image you used
above. ``PresetColour`` value should be used here, drawn from
`src/com/lilithsthrone/utils/colours/PresetColour.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/utils/colours/PresetColour.java>`_

10.1 colourPrimary
~~~~~~~~~~~~~~~~~~

This has to have a value defined, or else this XML file will fail to load.

.. code:: xml

    <colourPrimary>CLOTHING_WHITE</colourPrimary>

10.2 colourSecondary
~~~~~~~~~~~~~~~~~~~~

This can optionally be left blank, like the ’colourTertiary’ element below.

.. code:: xml

    <colourSecondary/>

10.3 colourTertiary
~~~~~~~~~~~~~~~~~~~

.. code:: xml

    <colourTertiary/>

11 attributeModifiers
---------------------

The attributes which should be affected by having this status effect. The
``value="10"`` part defines how much the attribute should be numerically affected
(and can be negative), while the ``DAMAGE_LUST`` part defines which attribute is
being affected. You can define any number of attribute modifiers, but it’s
usually best to keep it limited to just a few. Values for attributes should be
drawn from here:
`https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/character/attributes/Attribute.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/character/attributes/Attribute.java>`_

.. code:: xml

    <attributeModifiers>
    	<modifier value="100.0">HEALTH_MAXIMUM</modifier>
    </attributeModifiers>

12 combatMoves
--------------

The ``CombatMoves`` which should be unlocked for the character affected by this
status effect. ``CombatMoves`` identifiers are defined in their constructors. When
modding support for combat moves is added, the identifier will be described in
the modding file there. Current ``CombatMoves`` can be found in the files in this
folder: `src/com/lilithsthrone/game/combat/moves <https://github.com/Innoxia/liliths-throne-public/tree/dev/src/com/lilithsthrone/game/combat/moves>`_

Acceptable format:

.. code:: xml

    <combatMoves>
    	<move>cat-scratch</move>
    </combatMoves>

If combat moves are unecessary, insert an empty tag:

.. code:: xml

    <combatMoves/>

13 spells
---------

The Spells which should be unlocked for the character affected by this status
effect. Current Spells can be found in the files in this folder:
`src/com/lilithsthrone/game/combat/spells/Spell.java <https://github.com/Innoxia/liliths-throne-public/blob/dev/src/com/lilithsthrone/game/combat/spells/Spell.java>`_

Acceptable format:

.. code:: xml

    <spells>
    	<spell>ARCANE_AROUSAL</spell>
    </spells>

For an empty spell list:

.. code:: xml

    <spells/>

14 extraEffects
---------------

You can use this section to describe any extra effects that this status effect
might apply. These effects are shown in the tooltip when the player hovers over
the status effect icon. The character under the effect is passed in as the ``npc``
parsing argument, so if you want to, you can include parsing elements such as
``[npc.name]``. For this status effect, no extra effects need to be described, but
if you need to use this section, use the following format:

.. code:: xml

    <extraEffects>
    	<effect><![CDATA[You're a playful kitty!]]></effect>
    </extraEffects>

An empty ``extraEffects`` list:

.. code:: xml

    <extraEffects/>

15 Effect Logic
---------------

The condition for a status effect to be applied is by default ``false``, which
means that it can only be applied by a direct method call elsewhere for
``GameCharacter.addStatusEffect(AbstractStatusEffect statusEffect, int seconds)``.
If you would like your status effect to similarly only be applied when called
upon, then define this element as:

.. code:: xml

    <applicationCondition><![CDATA[false]]></applicationCondition>

If, however, you would like this status effect to be automatically activated
once certain conditions are met, then make sure that this element returns a
conditional that would result in ``true``, as in the example below.

You must use the game’s parsing engine to get what you want. ``npc`` is the parser
target for the character affected by this status effect. To parse something and
return a String, use a ``#`` character at the start of a command, such as:
``[#npc.isFeminine()]``. To parse something without returning a ``String`` (which
would most likely not be used in this element), use two ``#`` characters, such as:
``[##npc.isFeminine()]``. As a final note, all whitespace is stripped from the
returned String before it is parsed into a Boolean.

15.1 applicationCondition
~~~~~~~~~~~~~~~~~~~~~~~~~

This example is meant to show that you can use the parser to create more
*complex* conditionals.

.. code:: xml

    <applicationCondition><![CDATA[
    	#IF(SET_BONUS_innoxia_template.isCharacterWearingCompleteSet(npc))
    		true
    	#ELSE
    		false
    	#ENDIF
    ]]></applicationCondition>

An alternate, simpler example to achieve the same effect would be to just do:

.. code:: xml

    <applicationCondition><![CDATA[
    	SET_BONUS_innoxia_kitty.isCharacterWearingCompleteSet(npc)
    ]]></applicationCondition>

15.2 applyEffect
~~~~~~~~~~~~~~~~

Status effects execute an ``applyEffect(GameCharacter target, int secondsPassed)``
method every time the game ends a turn. The ``target`` argument is the character
who is under the effect of this particular status effect, while the
``secondsPassed`` argument is how much time, in seconds, has passed on this turn.
During combat, the ``secondsPassed`` argument is always 1 (to represent 1 turn
ending). If the method returns a String, then the game’s flow is interrupted to
display the **Important status effects** screen to the player, along with whatever
``String`` was returned by this ``applyEffect()`` method. You can define your own
effects to be parsed here, just like hard-coded status effects. While your
options are a little limited by what the parser can access, you should be able
to apply a good range of effects.

``interval``
    The ``interval`` attribute is an integer representing how often
    this effect should be applied (measured in seconds). For example, an interval
    of 3600 would make this effect be applied only once per hour (60\*60=3600). Use
    an interval of 0 to make this effect be applied on every turn.

``npc``
    is the parser target for the character affected by this status
    effect.

``SECONDS_PASSED``
    is a special tag which is converted into an integer value
    of the time that passed during the last turn’s end (in seconds).

``TOTAL_SECONDS_PASSED``
    is a special tag which is converted into a long
    value of the total time that’s passed while under the effect of this status
    effect (in seconds). This can be used with a ``TOTAL_SECONDS_PASSED==0`` check
    to, for example, only apply an effect when this status effect is initially
    added.

    - ****Important note:**** In combat, “seconds passed” is actually represented by
      the number of combat turns passed. So, for example, ``TOTAL_SECONDS_PASSED``
      would be converted into 2 if the character had been under the status
      effect’s influence for two turns in combat.

About tabs and spaces: all tabs are stripped from the returned ``String`` after
it is parsed, so it’s safe to use tabs and **not spaces** for formatting.

.. code:: xml

    <applyEffect interval="3600"><![CDATA[
    	#IF(SECONDS_PASSED>0)
    		An hour passed!
    		#IF(TOTAL_SECONDS_PASSED>(60*60*24))
    			[##game.getTextEndStringBuilder().append("<p>This effect has been in effect for more than a day!</p>")]
    		#ENDIF
    	#ENDIF
    ]]></applyEffect>

An empty effect list:

.. code:: xml

    <applyEffect/>

15.3 applyRemovalEffect
~~~~~~~~~~~~~~~~~~~~~~~

In a similar manner to the `15.2 applyEffect`_ element above, the game processes logic
when a status effect is removed.

This logic is performed while the character is still under the effects of this
status effect.

.. code:: xml

    <applyRemovalEffect/>

15.4 applyPostRemovalEffect
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a similar manner to the `15.2 applyEffect`_ element above, the game processes logic
after a status effect has been removed.

This logic is performed immediately after the effect is removed, so the
character is no longer under the effects of this status effect.

.. code:: xml

    <applyPostRemovalEffect/>
