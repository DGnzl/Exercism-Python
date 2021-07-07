import twelve_days
import twelve_days2

x = [twelve_days.recite(n, n)[0] for n in range(1, 4)]
y = [twelve_days2.recite(n, n)[0] for n in range(1, 4)]

print(x)
print(y)