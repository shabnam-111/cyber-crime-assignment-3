# Case Omega - Investigating a Ransomware Attack on a Healthcare Network

Assignment 3, Unit 3 (Investigation of Cyber Crimes). **All data is simulated for training.**

## Repository structure
| Folder | Contents |
|---|---|
| `01-first-responder/` | SOP, scene sketch |
| `02-evidence/` | Imaging log, SHA-256 hashes, chain of custody |
| `03-malware-analysis/` | Behaviour analysis, IOCs (no live malware included) |
| `04-timeline/` | Logs, `build_timeline.py`, `timeline.csv`, `timeline.png` |
| `05-report/` | Final legal-technical report (DOCX) |
| `screenshots/` | Terminal and scene screenshots |
| `docs/` | Tool summary, workflow, authorship declaration |

## Reproduce
```bash
cd 02-evidence && python3 make_sim_image.py
dd if=srv_emr_01_source.raw of=srv_emr_01.dd bs=4M conv=noerror,sync
sha256sum srv_emr_01_source.raw srv_emr_01.dd
cd ../04-timeline && python3 build_timeline.py
```
