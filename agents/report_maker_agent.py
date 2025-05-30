def generate_report(topic, summary):
    with open(f"{topic}_report.md", "w", encoding="utf-8") as file:
        file.write(f"# Research Report: {topic}\n\n")
        file.write(summary)
    print(f"Report saved as {topic}_report.md")
