import csv
import math
from statistics import mean

CSV_PATH = 'C:\SchoolWork (SRCC & MAPUA)\MAPUA DIGITAL WORKS (COLLEGE 3RD YEAR) (1st SEMESTER)\Works and Activities\CPE106L-4 - FOPI01\Lab7\breadprice.csv'

def parse_float(s):
    if s is None:
        return None
    s = s.strip()
    if s == '':
        return None
    s = ''.join(ch for ch in s if ch.isdigit() or ch in '.-')
    try:
        return float(s)
    except:
        return None

def read_csv(path):
    rows = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows

def compute_yearly_avg(rows):
    yearly = []
    for r in rows:
        year = r.get('Year') or r.get('year') or r.get('YEAR')
        if year is None:
            continue
        try:
            year = int(year)
        except:
            try:
                year = int(float(year))
            except:
                continue
        vals = []
        for k, v in r.items():
            key = k.strip().lower()
            if key == 'year':
                continue
            fv = parse_float(v)
            if fv is not None:
                vals.append(fv)
        avg = mean(vals) if vals else float('nan')
        yearly.append((year, avg))
    yearly.sort()
    return yearly

def print_table(yearly):
    print(f"{'Year':>6} {'AvgPrice':>10}")
    print("-" * 18)
    for y, a in yearly:
        if math.isnan(a):
            a_str = 'N/A'
        else:
            a_str = f"{a:.4f}"
        print(f"{y:6d} {a_str:>10}")

def ascii_plot(yearly, width=60, height=12):
    ys = [v for (_, v) in yearly if not math.isnan(v)]
    if not ys:
        print("No numeric data to plot.")
        return
    ymin, ymax = min(ys), max(ys)
    if ymin == ymax:
        ymin -= 0.5
        ymax += 0.5
    grid = [[' ']*len(yearly) for _ in range(height)]
    for col, (_, val) in enumerate(yearly):
        if math.isnan(val):
            continue
        frac = (val - ymin) / (ymax - ymin)
        row = height - 1 - int(frac * (height - 1))
        grid[row][col] = '*'
    for r in range(height):
        scale_val = ymin + ( (height-1-r)/(height-1) )*(ymax-ymin)
        print(f"{scale_val:8.2f} | " + ''.join(grid[r]))
    print(' ' * 11 + '-'*len(yearly))
    years_line = ' ' * 11
    for (y, _) in yearly:
        years_line += str(y)[-1]
    print(years_line)
    print("Note: x-axis shows last digit of year for compactness")

def main():
    rows = read_csv(CSV_PATH)
    yearly = compute_yearly_avg(rows)
    print_table(yearly)
    print()
    ascii_plot(yearly)

if __name__ == "__main__":
    main()
