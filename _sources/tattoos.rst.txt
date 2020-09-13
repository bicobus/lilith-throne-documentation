.. include:: global.inc.rst

=======
Tattoos
=======

    :Author: innoxia, bicobus

For a version without all of the comments, see
:ltgithub:`res/mods/innoxia/items/tattoos/heartWomb/heart_womb.xml`.

coreAttributes
--------------

value
~~~~~

The base value of this tattoo. All of the standard tattoos are 500 flames. I
roughly base things on 1 flame = 10p, so 10 flames = £1.

.. code:: xml

    <value>2000</value> 

name
~~~~

The name of this tattoo.

.. code:: xml

    <name><![CDATA[heart womb]]></name>

description
~~~~~~~~~~~

The description that’s shown in tooltips and on the item’s inspection page.

.. code:: xml

    <description><![CDATA[A stylised heart tattoo, which roughly resembles the shape of a female's reproductive system.]]></description>

availabilityRequirements
~~~~~~~~~~~~~~~~~~~~~~~~

Availability requirements for this tattoo. Use ’npc’ for the character receiving
the tattoo. Can be left blank.

Example
    tattoo available only to the player or feminine NPCs

    .. code:: xml

        <availabilityRequirements><![CDATA[npc.isPlayer() || npc.isFeminine()]]></availabilityRequirements>

imageName
~~~~~~~~~

.. seealso::

   :ref:`items-image`

The file path for this clothing’s image.

.. code:: xml

    <imageName>heart_womb.svg</imageName>

enchantmentLimit
~~~~~~~~~~~~~~~~

How many enchantments can be fit into this item. I feel like 5 is a good number
for this.

.. code:: xml

    <enchantmentLimit>10</enchantmentLimit>

slotAvailability
~~~~~~~~~~~~~~~~

Inventory slots that this tattoo can be assigned to. Leave blank to allow all
slots to be used.

.. seealso::

   List of :ltgithub:`possible
   slots</src/com/lilithsthrone/game/inventory/InventorySlot.java>`.

.. code:: xml

    <slotAvailability>
    	<slot>GROIN</slot>
    </slotAvailability>

colours
~~~~~~~

Please consult the relevant :ref:`documentation about colours<colours>`.

Use this section to define available colours for your tattoo. The game detects
specific colour values, and recolours them to the value chosen by the player.

.. code:: xml

    <primaryColours values="ALL"/>
    <secondaryColours values="ALL"/>
    <tertiaryColours values="ALL"/>

You can also make your own, custom list of colours to be used. If you want to
include custom colours, do not define a ’values’ attribute, and instead, list
each Colour, like in the example below.

.. code:: xml

    <tertiaryColours>
    	<colour>CLOTHING_PINK</colour>
    	<colour>CLOTHING_PINK_LIGHT</colour>
    </tertiaryColours>
