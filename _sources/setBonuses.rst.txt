.. include:: global.inc.rst
.. former title was setBonuses

=========
Item Sets
=========

    :Author: innoxia, bicobus

GENERAL INFORMATION
-------------------

If you are unsure of anything, please join the `Lilith's Throne Discord`_ and
ask for help! You can see another annotated example in the file
:ltgithub:`res/setBonuses/innoxia/enforcer.xml`.

name
----

The name of this set bonus.

.. code:: xml
    :name: name

    <name><![CDATA[Socks of Power]]></name>

statusEffect
------------

The id of the status effect which should be applied when a character is under
the effect of this set bonus.

.. code:: xml
    :name: statusEffect

    <statusEffect>innoxia_set_template</statusEffect>

numberRequiredForCompleteSet
----------------------------

The number of items of clothing or weapons which a character needs to equip to
gain this set bonus.

.. code:: xml
    :name: numberRequiredForCompleteSet

    <numberRequiredForCompleteSet>1</numberRequiredForCompleteSet>

blockedSlotsCountingTowardsFullSet
----------------------------------

If any of the slots defined in this section are blocked (due to the character’s
body not supporting clothing in these slots), then the slot is counted as being
equipped with an item of clothing from this set. For example, as the leg slot is
defined in this section, a character with a taur’s body (which is therefore
blocked from wearing leg clothing) would have the
``numberRequiredForCompleteSet`` reduced by 1. It’s usually best to fill out
this section with each slot that can be fitted with an item of this set’s
clothing. As this set only has 1 item in it, this section does nothing (as an
item set can only ever be activated with at least 1 item of clothing/weapon
equipped), and is just for demonstrative purposes.

Possible slots are found here:
:ltgithub:`src/com/lilithsthrone/game/inventory/InventorySlot.java`

.. code:: xml
    :name: blockedSlotsCountingTowardsFullSet

    <blockedSlotsCountingTowardsFullSet>
    	<slot>SOCK</slot>
    </blockedSlotsCountingTowardsFullSet>
