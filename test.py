import spidev
spi = spidev.SpiDev()
spi.open(32766, 0)
to_send = []
for a in range(0,63):
	to_send.append(0x05)
spi.writebytes(to_send)
