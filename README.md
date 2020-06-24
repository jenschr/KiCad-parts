# KiCad-parts
I'll add schematics, footprints and scripts that I've made for KiCad here as I go.

## SchematicPositionsToLayout.py
If you are moving from schematic to layout on a large board, it is extremely annying that Kicad imports all parts as a random lump of footprints. [This simple script](plugins/SchematicPositionsToLayout.py) will take two files as parameters: a Kicad 5 schematic (.sch) and a PCB Layout (.kicad_pcb) file. The script lays out all the components in the PCB file on positions that mimic those in the Schematic. This saves a lot of time the first time you lay out a board.

[Ian Ross](https://github.com/ian-ross) converted my quick-n-dirty script to a [full Kicad Plugin and added support for Hierical sheets](https://github.com/ian-ross/kicad-plugins).

## USI WM-N-BM-14 (WICED Module)
The parts you need to make your own hardware based on the [Particle.io P1 module](https://docs.particle.io/datasheets/p1-datasheet/). The schematic for the wm-n-bm-14 module is the first schematic I ever made for KiCad, so the pins are in chronological order (rather than functional). I might re-arrange that at a later time as I now realize it's not very convenient. The footprint reflowed perfectly on my first two PCBs using this module, so it's been tested & works as it should. The lib includes footprints for using with both the integrated PCB antenna or with the u.Fl connector (PCB antenna broken off to save space).

The lib also contains a 0605 RGB LED that is useful for providing the visual feedback required for knowing the [Device mode](https://docs.particle.io/guide/getting-started/modes/photon/) on the Particle platform. Note that there's quite a few of these with different pinout. Mine is Common Anode (common + / current sink).

## L9110 Motor driver
Cheap SO-8 motor driver that can drive up to 0.8A. Based on the part found in John Spencer's [motorised slider](https://github.com/mage0r/RSA0N11M9A0J_motorised_slider). I've fixed the DRC errors on this chip and I'm redistributing it here under its original [OHL license](http://www.tapr.org/OHL).

