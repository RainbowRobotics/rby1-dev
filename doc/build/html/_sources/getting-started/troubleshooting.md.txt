# Troubleshooting

## Cannot reach Web UI
- Reconnect to hotspot and verify SSID/password.
- Try the default Web UI URL/port again.
- Check DHCP/static settings. Reboot if needed.

## Cannot ping the robot
- Verify you are on the same subnet.
- Prefer wired for first tests; try a different cable/port.
- Temporarily disable local firewall (or add an allow rule).

## SDK cannot connect
- Confirm endpoint IP:PORT and that services are running.
- Test TCP reachability: `nc -vz <ip> <port>`.
- Ensure Python venv is active and rby1‑sdk is installed.

## Time sync (optional)
- If logs show large drift, sync time (NTP/PTP) or record an offset.

## TODO
- [ ] List default ports/services
- [ ] Add common error codes and quick resolutions
- [ ] Where to grab logs and how to share them
