"""Correlates simulated logs into one timeline (CSV + PNG). Case Omega - training data."""
import csv, re, glob, datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TS = re.compile(r"^(\d{4}-\d\d-\d\dT[\d:]+\+05:30)\s+(.*)$")
CAT = [("usb", "USB insertion"), ("Launched", "Malware execution"), ("proxy", "Network"),
       ("sshd", "Lateral movement"), ("sudo", "Privilege escalation"), ("crontab", "Persistence"),
       ("RENAME", "Encryption"), ("DELETE vss", "Backup destruction"), ("HOW_TO", "Ransom note")]
def cat(src, msg):
    if "EXFIL" in msg: return "Exfiltration"
    if "omega.key" in msg: return "Key retrieval"
    if "phishing" in msg: return "Phishing"
    for k, c in CAT:
        if k in msg or k in src: return c
    return "Other"

rows = []
for f in sorted(glob.glob("logs/*.log")):
    for line in open(f):
        m = TS.match(line.strip())
        if m: rows.append((m.group(1), f.split("/")[-1], m.group(2)))
for r in csv.DictReader(open("logs/browser_history.csv")):
    rows.append((r["time"], "browser_history.csv", f'{r["host"]} {r["user"]} {r["url"]}'))
rows.sort(key=lambda r: r[0])
with open("timeline.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["timestamp_ist", "source", "category", "event"])
    for t, s, m in rows: w.writerow([t, s, cat(s, m), m])
print(f"{len(rows)} events correlated -> timeline.csv")

colors = {}
fig, ax = plt.subplots(figsize=(11, 6))
cats = []
for t, s, m in rows:
    c = cat(s, m)
    if c not in cats: cats.append(c)
for t, s, m in rows:
    c = cat(s, m)
    ax.scatter(dt.datetime.fromisoformat(t), cats.index(c), s=80, zorder=3)
ax.set_yticks(range(len(cats))); ax.set_yticklabels(cats)
ax.grid(True, alpha=.3); ax.set_title("Case Omega - Attack timeline (IST, 13-14 Sep 2026)")
fig.autofmt_xdate(); fig.tight_layout(); fig.savefig("timeline.png", dpi=150)
