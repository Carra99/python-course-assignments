from datetime import datetime
from collections import defaultdict

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def compute_duration(start, end):
    delta = parse_time(end) - parse_time(start)
    return int(delta.total_seconds() // 60)  # convert to minutes

def parse_log_file(filename):
    activity_durations = defaultdict(int)
    total_minutes = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or "-" not in line:
                continue
            time_part, activity = line.split(maxsplit=1)
            start_time, end_time = time_part.split('-')
            duration = compute_duration(start_time, end_time)
            activity_durations[activity] += duration
            total_minutes += duration

    return activity_durations, total_minutes

def generate_report(activity_durations, total_minutes):
    report_lines = []
    for activity, duration in sorted(activity_durations.items()):
        percentage = round(duration / total_minutes * 100)
        report_lines.append(f"{activity:<25} {duration:>3} minutes   {percentage:>2}%")
    return "\n".join(report_lines)

if __name__ == "__main__":
    log_file = "timelog.txt"
    activity_durations, total_minutes = parse_log_file(log_file)
    report = generate_report(activity_durations, total_minutes)
    print(report)
