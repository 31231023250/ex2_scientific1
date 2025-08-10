import numpy as np
import matplotlib.pyplot as plt

def main(N=50, seed=42, outfile="circles.png"):
    rng = np.random.default_rng(seed)
    # Tọa độ tâm trong [0,1]
    x = rng.random(N)
    y = rng.random(N)
    # Màu ngẫu nhiên trong [0,1]
    colors = rng.random(N)
    # Bán kính r ∈ [0,1] → diện tích = π r^2
    r = rng.random(N)
    area = np.pi * (r ** 2)

    # Matplotlib dùng "s" là diện tích tính theo point^2 → scale để nhìn rõ
    scale = 4000.0
    plt.figure()
    plt.scatter(x, y, s=area * scale, c=colors, alpha=0.5)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Random circles (N={N})")
    plt.tight_layout()
    plt.savefig(outfile, dpi=150)
    print(f"Đã lưu hình: {outfile}")

if __name__ == "__main__":
    main()
