"""Recomputes every number and identity the book states. Run by `make verify`."""
import math, random

g, sig, A, k, T = 0.005, 0.676, 1.49, 2.52, 360          # RELIANCE calibration (report/tables/numbers.tex)
r2 = lambda v, w: abs(v - w) < 5e-3 * max(1, abs(w))

# Ch 1: fill rate at 0.5 INR
assert r2(A * math.exp(-k * 0.5), 0.423)

# Ch 4: f'(d) = A e^{-kd}[-k + (k+g) e^{-g(d+c)}], root d* = ln(1+g/k)/g - c is the maximum
c = -0.35
f = lambda d: A * math.exp(-k * d) * (1 - math.exp(-g * (d + c)))
fp = lambda d: A * math.exp(-k * d) * (-k + (k + g) * math.exp(-g * (d + c)))
for d in (0.1, 0.8, 2.0):
    h = 1e-6
    assert abs((f(d + h) - f(d - h)) / (2 * h) - fp(d)) < 1e-7
ds = math.log(1 + g / k) / g - c
assert abs(fp(ds)) < 1e-12 and fp(ds - 0.1) > 0 and fp(ds + 0.1) < 0
assert r2(math.log(1 + g / k) / g, 0.396)

# Ch 5: E[-exp(-g(x + q S_T))] = -exp(-g x) exp(-g(q s - g q^2 sig^2 tau / 2))  (normal MGF, by quadrature)
s, x, q, tau = 100.0, 10.0, 3, 50.0
n, lo, hi = 200000, -12.0, 12.0
dz = (hi - lo) / n
mc = sum(-math.exp(-g * (x + q * (s + sig * math.sqrt(tau) * (lo + (i + .5) * dz))))
         * math.exp(-(lo + (i + .5) * dz) ** 2 / 2) / math.sqrt(2 * math.pi) * dz for i in range(n))
th = -math.exp(-g * x) * math.exp(-g * (q * s - 0.5 * g * q * q * sig ** 2 * tau))
assert abs(mc / th - 1) < 1e-9
G = lambda q, tau=T: -0.5 * g * sig ** 2 * q * q * tau
assert r2(G(10), -41.13)

# Ch 6: differences of g, r, spread, quotes = r +- spread/2, worked numbers
for q in (-4, 0, 3, 10):
    db, da = G(q + 1) - G(q), G(q) - G(q - 1)
    assert abs(db + 0.5 * g * sig ** 2 * T * (2 * q + 1)) < 1e-9
    assert abs(da + 0.5 * g * sig ** 2 * T * (2 * q - 1)) < 1e-9
    r = s - q * g * sig ** 2 * T
    assert abs(s + 0.5 * (da + db) - r) < 1e-9
    e = math.log(1 + g / k) / g
    sp = g * sig ** 2 * T + 2 * e
    assert abs((e + da) + (e - db) - sp) < 1e-9
    assert abs((s - (e - db)) - (r - sp / 2)) < 1e-9 and abs((s + (e + da)) - (r + sp / 2)) < 1e-9
assert r2(g * sig ** 2 * T, 0.823) and r2(2 * math.log(1 + g / k) / g, 0.793)
assert r2(g * sig ** 2 * T + 2 * math.log(1 + g / k) / g, 1.615)
assert r2(10 * g * sig ** 2 * T, 8.23)
assert r2(g * sig ** 2 * 60, 0.137) and r2(g * sig ** 2 * 60 + 2 * math.log(1 + g / k) / g, 0.930)
print("verify: all checks pass")
