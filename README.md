# KiCad-parts
I'll add schematics and footprints I've made for KiCad here as I go.

## USI WM-N-BM-14 (WICED Module)
The parts you need to make your own hardware based on the [Particle.io P1 module](https://docs.particle.io/datasheets/p1-datasheet/). The schematic for the wm-n-bm-14 module is the first schematic I ever made for KiCad, so the pins are in chronological order (rather than functional). I might re-arrange that at a later time as I now realize it's not very convenient. The footprint reflowed perfectly on my first two PCBs using this module, so it's been tested & works as it should. The lib includes footprints for using with both the integrated PCB antenna or with the u.Fl connector (PCB antenna broken off to save space).

The lib also contains a 0605 RGB LED that is useful for providing the visual feedback required for knowing the [Device mode](https://docs.particle.io/guide/getting-started/modes/photon/) on the Particle platform.