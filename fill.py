from tinyfish import TinyFish
client = TinyFish()

r = client.agent.run(
    url="https://nationalscholarshipapplication.netlify.app",
    goal=("Fill the form with: Full name Ananya R.; "
          "Email ananya@example.com; Mobile 9876543210; "
          "State Karnataka; Category OBC; Course B.Tech CSE; "
          "Year 2; Marks 82; Annual family income 250000. "
          "Do NOT click Submit. Stop when every field is filled."),
)
print(getattr(r, "result", r))