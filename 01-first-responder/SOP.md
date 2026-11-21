# First Responder SOP - Suspected Ransomware at a Healthcare Facility

**Case:** Omega | **Scope:** Servers, workstations, USB media, network devices, cloud access points

## 1. Arrival and scene safety
1. Confirm patient-safety systems (ICU monitors, ventilators) are on isolated or manual fallback before touching IT.
2. Record arrival time, names of all persons present, and who authorised access.
3. Secure the area; allow only authorised personnel. Log everyone entering or leaving.

## 2. Preserve the scene (do not alter evidence)
1. **Do not** reboot, shut down, log in, or run antivirus clean-up on affected machines.
2. If the machine is on: photograph the screen (ransom note, error messages), then note the time shown.
3. Isolate from the network by **unplugging the network cable / disabling Wi-Fi** (do not power off, to preserve RAM).
4. Capture volatile data first (order of volatility): RAM, running processes, network connections, logged-in users, then disk.
5. Photograph all four sides of each device, cables, ports, and connected USB devices before touching.

## 3. Document the scene
- Photographs: wide, medium, close-up; include a scale/evidence tag.
- Draw a sketch map (see `scene_sketch.png`) with room layout, device positions and labels.
- Tag every item with: Evidence ID, description, make/model/serial, date/time, collector name.

## 4. Identify digital evidence
| Type | Examples in this case |
|---|---|
| Computers | SRV-EMR-01 (EMR server), WS-ADM-07 (billing workstation) |
| Removable media | USB flash disk, serial 0710A4F3 |
| Network | Firewall/proxy logs, switch logs, router config |
| Logs | auth.log, auditd, application logs, VSS/backup logs |
| Cloud | Email tenant, backup cloud console, VPN portal |
| Paper | Ransom note printouts, staff notes |

## 5. Collection and packaging
1. Use write blockers for physical drives; use hashing for every image.
2. Package in anti-static bags, seal with tamper-evident tape, sign across the seal.
3. Start the Chain of Custody form at the scene (see `02-evidence/chain_of_custody.md`).

## 6. Notification
Notify the hospital CISO, legal counsel, and CERT-In (within 6 hours of noticing the incident, per CERT-In Directions, 28 April 2022). Preserve and hand over to the forensic lab.

## 7. Do / Don't
| Do | Don't |
|---|---|
| Photograph before touching | Power off or reboot |
| Record exact times | Pay the ransom or contact the attacker |
| Keep a written log | Plug unknown USBs into any system |
| Hash all images | Work on the original evidence |
