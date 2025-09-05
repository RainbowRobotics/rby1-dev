# Connect to an External Access Point (AP)

Purpose: move from the hotspot to your lab/office Wi‑Fi (or wired).

## Wi‑Fi (example flow)
1. In the Web UI, open Network → Wi‑Fi.
2. Scan, select your AP SSID, enter credentials, save/apply.
3. Reboot or reconnect if prompted.
4. Rejoin your lab Wi‑Fi on the laptop as well.

## Wired (optional)
- Connect Ethernet from controller to a switch or directly to the laptop.
- Assign a static IP or use DHCP (per lab policy).

## Verify connectivity
- From your laptop: `ping <robot-ip>`
- In Web UI: confirm the interface shows connected with an IP.

## TODO
- [ ] Default IPs/subnets (hotspot vs. lab)
- [ ] Exact Wi‑Fi security modes supported
- [ ] Ethernet/static IP examples used in your lab
