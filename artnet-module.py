import asyncio
from pyartnet import ArtNetNode
import time

time.sleep(3)

d = [0] * 51

async def main():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)

        # 51 channels starting at DMX address 1
        channel = universe.add_channel(start=1, width=51)

        # DMX data buffer

        # PAN & TILT
        d[0] = 65          # pan coarse: 127 center, 115 left, 135 right
        d[1] = 0            # pan fine
        d[2] = 20           # tilt coarse: 54 up, 40 center, 15 down
        d[3] = 0            # tilt fine

        # Motion speed (0 = fast, 255 = slow)
        d[4] = 100          # feels smooth but not sluggish

        # Zoom
        d[5] = 255          # full wide

        # Rot
        d[6] = 0            # no rotation

        # Dimmer
        d[7] = 240          # full output

        # Strobe mode (keep constant on)
        d[8] = 255

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
        seg4 = 24 - 1  # python index starting at 0, segment4 starts at DMX channel 36
        d[seg4]     = 255   # R
        d[seg4 + 1] = 0     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W


        # Send instantly
        channel.set_values(d)

        # Hold state
        await asyncio.sleep(5)


#asyncio.run(main())


async def level1():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)

        # 51 channels starting at DMX address 1
        channel = universe.add_channel(start=1, width=51)

        # DMX data buffer

        # PAN & TILT
        d[0] = 140          # pan coarse: 127 center, 115 left, 135 right
        d[1] = 0            # pan fine
        d[2] = 13           # tilt coarse: 54 up, 40 center, 15 down
        d[3] = 0            # tilt fine

        # Motion speed (0 = fast, 255 = slow)
        d[4] = 100          # feels smooth but not sluggish

        # Zoom
        d[5] = 255          # full wide

        # Rot
        d[6] = 0            # no rotation

        # Dimmer
        d[7] = 255          # full output

        # Strobe mode (keep constant on)
        d[8] = 255

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
        seg4 = 24 - 1  # python index starting at 0, segment4 starts at DMX channel 36
        d[seg4]     = 0   # R
        d[seg4 + 1] = 255     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W


        # Send instantly
        channel.set_values(d)

        # Hold state
        await asyncio.sleep(5)

        d[seg4]     = 255   # R
        d[seg4 + 1] = 0     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W
        channel.set_fade(d, 500)

        # PAN & TILT
        d[0] = 110          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 13           # tilt coarse: 54 up, 40 center, 15 down
        
        channel.set_fade(d, 5000)
        await asyncio.sleep(5)

        # PAN & TILT
        d[0] = 150          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 13           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 5000)
        await asyncio.sleep(5)

        # PAN & TILT
        d[0] = 135          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 50           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 1000)
        await asyncio.sleep(1)

        # PAN & TILT
        d[0] = 120          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 50           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 3000)
        await asyncio.sleep(5)
        
        # PAN & TILT
        d[0] = 140          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 10           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 7000)
        await asyncio.sleep(5)



async def level2():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)

        # 51 channels starting at DMX address 1
        channel = universe.add_channel(start=1, width=51)

        # DMX data buffer

        # PAN & TILT
        d[0] = 115          # pan coarse: 127 center, 115 left, 135 right
        d[1] = 0            # pan fine
        d[2] = 50           # tilt coarse: 54 up, 40 center, 15 down
        d[3] = 0            # tilt fine

        # Motion speed (0 = fast, 255 = slow)
        d[4] = 100          # feels smooth but not sluggish

        # Zoom
        d[5] = 255          # full wide

        # Rot
        d[6] = 0            # no rotation

        # Dimmer
        d[7] = 255          # full output

        # Strobe mode (keep constant on)
        d[8] = 255

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
        seg4 = 24 - 1  # python index starting at 0, segment4 starts at DMX channel 36
        d[seg4]     = 0   # R
        d[seg4 + 1] = 255     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W


        # Send instantly
        channel.set_values(d)

        # Hold state
        await asyncio.sleep(5)

        d[seg4]     = 255   # R
        d[seg4 + 1] = 0     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W
        channel.set_fade(d, 500)

        # PAN & TILT
        d[0] = 115          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 13           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 5000)
        await asyncio.sleep(5)

        # PAN & TILT
        d[0] = 127          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 50           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 5000)
        await asyncio.sleep(5)

        # PAN & TILT
        d[0] = 131          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 14           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 3000)
        await asyncio.sleep(1)

        # PAN & TILT
        d[0] = 140          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 52           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 3000)
        await asyncio.sleep(5)
        


async def level3():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)

        # 51 channels starting at DMX address 1
        channel = universe.add_channel(start=1, width=51)

        # DMX data buffer
        # PAN & TILT
        d[0] = 140          # pan coarse: 127 center, 115 left, 135 right
        d[1] = 0            # pan fine
        d[2] = 15           # tilt coarse: 54 up, 40 center, 15 down
        d[3] = 0            # tilt fine

        # Motion speed (0 = fast, 255 = slow)
        d[4] = 100          # feels smooth but not sluggish

        # Zoom
        d[5] = 255          # full wide

        # Rot
        d[6] = 0            # no rotation

        # Dimmer
        d[7] = 255          # full output

        # Strobe mode (keep constant on)
        d[8] = 255

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
        seg4 = 24 - 1  # python index starting at 0, segment4 starts at DMX channel 36
        d[seg4]     = 0   # R
        d[seg4 + 1] = 255     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W


        # Send instantly
        channel.set_values(d)

        # Hold state
        await asyncio.sleep(5)

        d[seg4]     = 255   # R
        d[seg4 + 1] = 0     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W
        channel.set_fade(d, 500)

        # PAN & TILT
        d[0] = 115          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 50           # tilt coarse: 54 up, 40 center, 15 down

        channel.set_fade(d, 5000)
        await asyncio.sleep(5)

        # PAN & TILT
        d[0] = 115          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 15           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 5000)
        await asyncio.sleep(5)

        # PAN & TILT
        d[0] = 140          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 50           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 3000)
        await asyncio.sleep(1)

        # PAN & TILT
        d[0] = 115          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 15           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 3000)
        await asyncio.sleep(5)

        # PAN & TILT
        d[0] = 140          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 50           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 2000)
        await asyncio.sleep(5)

        # PAN & TILT
        d[0] = 115          # pan coarse: 127 center, 115 left, 135 right
        d[2] = 15           # tilt coarse: 54 up, 40 center, 15 down
        channel.set_fade(d, 1000)
        await asyncio.sleep(5)


async def infiniteLevel():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)

        # 51 channels starting at DMX address 1
        channel = universe.add_channel(start=1, width=51)

        # DMX data buffer

        # PAN & TILT
        d[0] = 140          # pan coarse: 127 center, 115 left, 135 right
        d[1] = 0            # pan fine
        d[2] = 15           # tilt coarse: 54 up, 40 center, 15 down
        d[3] = 0            # tilt fine

        # Motion speed (0 = fast, 255 = slow)
        d[4] = 100          # feels smooth but not sluggish

        # Zoom
        d[5] = 255          # full wide

        # Rot
        d[6] = 0            # no rotation

        # Dimmer
        d[7] = 255          # full output

        # Strobe mode (keep constant on)
        d[8] = 255

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
        seg4 = 24 - 1  # python index starting at 0, segment4 starts at DMX channel 36
        d[seg4]     = 0   # R
        d[seg4 + 1] = 255     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W


        # Send instantly
        channel.set_values(d)

        d[seg4]     = 255   # R
        d[seg4 + 1] = 0     # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W

        channel.set_fade(d, 500)

        # for 3 min move beam to random positions within pan 115-140 and tilt 15-50
        import random
        for _ in range(180):
            d[0] = random.randint(115, 140)
            d[2] = random.randint(15, 50)
            channel.set_fade(d, 1000)
            await asyncio.sleep(1)

        d[9]  = 255
        d[6] = 255
        d[0] = 127
        d[2] = 40

        channel.set_fade(d, 5000)
        await asyncio.sleep(5)

        
async def off():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)

        # 51 channels starting at DMX address 1
        channel = universe.add_channel(start=1, width=51)

        # DMX data buffer
        d = [0] * 51
        channel.set_values(d)
        await asyncio.sleep(1)

async def green():
    async with ArtNetNode.create('10.1.1.104', 6454) as node:
        universe = node.add_universe(1)
        channel = universe.add_channel(start=1, width=51)

        d[7] = 255          # full output
        d[8] = 255
        seg4 = 24 - 1
        d[seg4]     = 0     # R 
        d[seg4 + 1] = 255   # G
        d[seg4 + 2] = 0     # B
        d[seg4 + 3] = 0     # W

        channel.set_values(d)
        await asyncio.sleep(3)


asyncio.run(level1())
asyncio.run(green())
asyncio.run(level2())
asyncio.run(green())
asyncio.run(level3())
asyncio.run(green())
asyncio.run(infiniteLevel())
asyncio.run(off())

        
