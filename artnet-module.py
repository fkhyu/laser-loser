import asyncio
from pyartnet import ArtNetNode

async def main():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)

        # Suppose fixture expects 51 channels starting at slot 1
        # Create a channel block of width 51
        channel = universe.add_channel(start=1, width=51)

        # Build the data array (0–255 values for each channel)
        data = [0] * 51

        # Example mapping – these numbers are hypothetical,
        # you must replace them with those from your 51-channel mode DMX chart.
        PAN_COARSE = 0  # index in data array (0-based)
        PAN_FINE   = 1
        TILT_COARSE= 2
        TILT_FINE  = 3
        MASTER_DIMMER = 4
        PIXEL1_R = 10   # for example
        PIXEL1_G = 11
        PIXEL1_B = 12
        # ... further pixel channels as defined

        # Set pan to 125 → convert to DMX coarse/fine as needed
        data[PAN_COARSE] = 125
        data[PAN_FINE]   = 0  # if you don’t need fine control

        # Set tilt to 20 → map to DMX value
        data[TILT_COARSE] = 20
        data[TILT_FINE]   = 0

        # Master dimmer to full
        data[MASTER_DIMMER] = 255

        # Pixel-wise: only central pixel red
        data[PIXEL1_R] = 255
        data[PIXEL1_G] = 0
        data[PIXEL1_B] = 0

        # All other pixel bytes are already zero (others off)

        # Send immediately (no fade)
        channel.set_values(data)

        # Optionally hold for a while so the light stays that way
        await asyncio.sleep(10)

asyncio.run(main())