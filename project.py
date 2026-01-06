ASCII = "@#$&*:,."
LEVELS = len(ASCII)

BLOCK_W = 2
BLOCK_H = 4
GAMMA = 0.6

def gamma_correct(value):
    return int(255 * ((value / 255) ** GAMMA))

def intensity_to_char(value):
    index = int(value * (LEVELS - 1) / 255)
    return ASCII[index]

with open("bill_clinton_4.ppm", "r") as f:
    raw = f.read().split()

data = []
for token in raw:
    if not token.startswith("#"):
        data.append(token)

width = int(data[1])
height = int(data[2])
pixels = data[4:]  

with open("ascii_output.txt", "w") as out:
    y = 0
    while y < height - BLOCK_H:
        row = ""
        x = 0
        while x < width - BLOCK_W:
            total = 0
            count = 0

            for dy in range(BLOCK_H):
                for dx in range(BLOCK_W):
                    idx = ((y + dy) * width + (x + dx)) * 3
                    r = int(pixels[idx])
                    g = int(pixels[idx + 1])
                    b = int(pixels[idx + 2])

                    # Better grayscale (human vision weighted)
                    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                    gray = gamma_correct(gray)

                    total += gray
                    count += 1
                    avg = total 
            row += intensity_to_char(avg)
            x += BLOCK_W

        out.write(row + "\n")
        print(row)
        y += BLOCK_H

print("\nASCII image generated ")
