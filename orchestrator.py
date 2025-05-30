from agents.data_gatherer_agent import gather_data
from agents.fact_checker_agent import verify_facts
from agents.summarizer_agent import summarize_content
from agents.report_maker_agent import generate_report

def main(topic):
    data = gather_data(topic)
    verified_data = verify_facts(data)
    summary = summarize_content(verified_data)
    generate_report(topic, summary)

if __name__ == "__main__":
    topic = input("Enter your research topic: ")
    main(topic)
