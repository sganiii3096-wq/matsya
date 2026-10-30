import json, time
from tinyfish import TinyFish

client = TinyFish()
PAGES = [
    ("Karnataka SSP Scholarships", "https://ssp.karnataka.gov.in"),
    ("NSP Central Sector Scheme", "https://scholarships.gov.in"),
    ("AICTE Student Development Schemes", "https://aicte.gov.in/schemes/students-development-schemes"),
]
    # add 2 to 4 more OFFICIAL scheme pages here, same format
GOAL = ("Find the scholarship scheme on this page. Look in notices, "
        "announcements and important dates for the current last date "
        "to apply. Return JSON with: scheme_name, last_date, "
        "eligibility, documents_needed, source_url. "
        "If no date is shown anywhere, set last_date to 'Not published'. "
        "Never guess a date.")


out = []
for name, url in PAGES:
    try:
        r = client.agent.run(url=url, goal=GOAL)
        res = str(getattr(r, "result", r))
    except Exception as e:
        res = "Could not read this page: " + str(e)[:150]
    out.append({"name": name, "url": url,
                "checked_at": time.strftime("%d %b %Y %H:%M"),
                "result": res})
    json.dump(out, open("schemes.json", "w"), indent=2)
    print("done:", name)