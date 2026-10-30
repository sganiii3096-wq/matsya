from tinyfish import TinyFish

client = TinyFish()

response = client.agent.run(
    url="https://scholarships.gov.in",
    goal=("Find the Central Sector Scheme of Scholarships. Look in notices, "
          "announcements and important dates for the current last date "
          "to apply. Return JSON with: scheme_name, last_date, "
          "eligibility, documents_needed, source_url. "
          "If no date is shown anywhere, set last_date to 'Not published'. "
          "Never guess a date."),
)
print(getattr(response, "result", response))