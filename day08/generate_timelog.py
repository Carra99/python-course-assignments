from datetime import datetime
from collections import defaultdict

def parse_log_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        blocks = f.read().strip().split("\n\n")
    
    all_sessions = []
    for block in blocks:
        lines = block.strip().split("\n")
        session = []
        for line in lines:
            time_str, activity = line.strip().split(" ", 1)
            time_obj = datetime.strptime(time_str, "%H:%M")
            session.append((time_obj, activity))
        all_sessions.append(session)
    return all_sessions

def create_detailed_log(sessions):
    detailed_lines = []
    all_intervals = []

    for session in sessions:
        for i in range(len(session) - 1):
            start_time, activity = session[i]
            end_time, _ = session[i + 1]
            duration = int((end_time - start_time).total_seconds() // 60)
            line = f"{start_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')} {activity}"
            detailed_lines.append(line)
            all_intervals.append((activity, duration))
        detailed_lines.append("")  # blank line between sessions

    return detailed_lines, all_intervals

def summarize_activities(intervals):
    summary = defaultdict(int)
    for activity, duration in intervals:
        summary[activity] += duration

    total_time = sum(summary.values())
    summary_lines = []
    for activity in sorted(summary):
        minutes = summary[activity]
        percentage = round((minutes / total_time) * 100)
        summary_lines.append(f"{activity:<25} {minutes:>3} minutes   {percentage:>2}%")
    return summary_lines

def generate_report(log_file_path, output_file_path):
    sessions = parse_log_file(log_file_path)
    detailed_lines, intervals = create_detailed_log(sessions)
    summary_lines = summarize_activities(intervals)

    full_report = detailed_lines + [""] + summary_lines
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_report))
    print(f"Report generated: {output_file_path}")

# Example usage
if __name__ == "__main__":
    generate_report("timelog.log", "timelog.txt")
