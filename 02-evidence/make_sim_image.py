"""Regenerates the 16 MiB SIMULATED disk image used in Case Omega (training data only)."""
import random
random.seed(461)
body = bytearray(b"SIMULATED-DISK-IMAGE|CASE-OMEGA|SRV-EMR-01|training data only\n")
for i in range(1, 41):
    body += f"/emr/patients/record_{i:04d}.db.omega\n".encode()
body += b"/emr/HOW_TO_RECOVER.txt\n/var/spool/cron/crontabs/svc_backup\n"
body += bytes(random.getrandbits(8) for _ in range(16 * 1024 * 1024 - len(body)))
open("srv_emr_01_source.raw", "wb").write(body)
