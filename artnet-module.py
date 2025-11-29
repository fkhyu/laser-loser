import asyncio
from pyartnet import ArtNetNode

async def main():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)

        # 51 channels starting at DMX address 1
        channel = universe.add_channel(start=1, width=51)

        # DMX data buffer
        d = [0] * 51

        # PAN & TILT
        d[0] = 125          # pan coarse
        d[1] = 0            # pan fine
        d[2] = 20           # tilt coarse
        d[3] = 0            # tilt fine

        # Motion speed (0 = fast, 255 = slow)
        d[4] = 100          # feels smooth but not sluggish

        # Zoom
        d[5] = 255          # full wide

        # Dimmer
        d[7] = 255          # full output

        # Strobe mode (keep constant on)
        d[8] = 0

        # Base RGB(W) output — keep off
        d[9]  = 0
        d[10] = 0
        d[11] = 0
        d[12] = 0

        # Background RGBW — keep off
        d[18] = 0
        d[19] = 0
        d[20] = 0
        d[21] = 0

        # SEGMENT COLOR CONTROL
        # Segment layout (per manual):
        # 24–27 = seg1, 28–31 = seg2, 32–35 = seg3,
        # 36–39 = seg4, 40–43 = seg5, 44–47 = seg6, 48–51 = seg7

        # Light ONLY segment 4 RED
        seg4 = 36 - 1  # python index starting at 0, segment4 starts at DMX channel 36
        d[seg4]     = 255   # R
        d[seg4 + 1] = 0     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W

        # Send instantly
        channel.set_value(d)

        # Hold state
        await asyncio.sleep(5)


asyncio.run(main())