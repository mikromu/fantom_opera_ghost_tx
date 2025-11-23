import requests, time

def ghost_hunter():
    print("Fantom Opera — Ghost Transaction Hunter (zero-fee magic)")
    seen = set()
    while True:
        r = requests.get("https://api.ftmscan.com/api?module=account&action=txlist&address=0x0000000000000000000000000000000000000000&sort=desc")
        for tx in r.json()["result"][:40]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)
            if int(tx["gasPrice"]) == 0 and int(tx["value"]) > 0:
                value = int(tx["value"]) / 1e18
                if value > 10:  # >10 FTM moved with 0 gas
                    print(f"GHOST TX DETECTED 👻\n"
                          f"{value:.2f} FTM teleported for FREE\n"
                          f"From → {tx['from']}\n"
                          f"To → {tx['to']}\n"
                          f"Hash: {h}\n"
                          f"https://ftmscan.com/tx/{h}\n"
                          f"→ SpookySwap internal / pre-approved magic\n"
                          f"{'👻'*30}")
        time.sleep(1.7)

if __name__ == "__main__":
    ghost_hunter()
