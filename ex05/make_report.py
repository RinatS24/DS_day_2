from analytics import Research
from analytics import Analytics
from config import num_of_steps
from config import report_text
import sys


def main(file_path):
    research = Research(file_path)
    data = research.file_reader()

    analytics = Analytics(data)
    tails,heads = analytics.counts()
    tails_percent,heads_percent = analytics.fractions(tails,heads)

    rand = analytics.predict_random(num_of_steps)
    predict_tails,predict_heads = Analytics(rand).counts()

    report = report_text.format(
        total_exp = tails + heads,
        tails = tails,
        heads = heads,
        tails_per = tails_percent,
        heads_per = heads_percent,
        num_of_steps = num_of_steps,
        predict_tails = predict_tails,
        predict_heads = predict_heads 
    )

    analytics.save_file(report,"report","txt")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])