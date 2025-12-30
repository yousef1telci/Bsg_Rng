from PIL import Image
import math
import os
import random

# --------------------------------------------------
# 1) RNG ضعيف (Linear Congruential Generator)

# مثال على الحساب اليدوي:
#seed = 7
#a = 5
#c = 3
#m = 10
#x1​= (5⋅7+3)mod10=38mod10 = 8
#x2​=(5⋅8+3)mod10=43mod10=3
#x3​=(5⋅3+3)mod10=18mod10=8

#لاحظ

   # بدأ التكرار (8 → 3 → 8)
  #  وهذا هو الضعف!
# --------------------------------------------------
def weak_rng(seed, n):
    a = 5
    c = 1
    m = 64      # نحصر القيم بين 0 و 255 (ألوان)
    x = seed
    numbers = []

    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x*4)

    return numbers


# --------------------------------------------------
# 2) RNG قوي (SystemRandom)
# --------------------------------------------------
def strong_rng(n):
    rng = random.SystemRandom()
    return [rng.randrange(256) for _ in range(n)]


# --------------------------------------------------
# 3) تحويل الأرقام إلى صورة وحفظها كـ JPEG
# --------------------------------------------------
def numbers_to_image(numbers, filename):
    size = int(math.sqrt(len(numbers)))
    img = Image.new("L", (size, size))   # L = Grayscale
    img.putdata(numbers[:size * size])
    img.save(filename, "JPEG", quality=50)


# --------------------------------------------------
# 4) حساب حجم الملف (بالكيلوبايت)
# --------------------------------------------------
def file_size_kb(filename):
    return os.path.getsize(filename) / 1024


# --------------------------------------------------
# 5) التنفيذ الرئيسي
# --------------------------------------------------
N = 65536   # 256 × 256

# RNG ضعيف
weak_numbers = weak_rng(seed=7, n=N)
numbers_to_image(weak_numbers, "weak_rng.jpg")

# RNG قوي
strong_numbers = strong_rng(N)
numbers_to_image(strong_numbers, "strong_rng.jpg")

# طباعة النتائج
print("Weak RNG image size:", file_size_kb("weak_rng.jpg"), "KB")
print("Strong RNG image size:", file_size_kb("strong_rng.jpg"), "KB")
