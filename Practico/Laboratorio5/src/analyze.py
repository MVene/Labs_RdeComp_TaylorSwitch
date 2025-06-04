import re
from collections import defaultdict
from typing import Dict, List

# Type aliases for clarity
Timestamp = float
MessageID = str
Protocol = str


def parse_log(filename: str) -> Dict[Protocol, Dict[MessageID, Dict[str, Timestamp]]]:
    """
    Parses the log file and groups sent/received timestamps by message ID and protocol.

    Returns:
        A nested dictionary: protocol -> message ID -> {'sent': ..., 'received': ...}
    """
    # Use defaultdict to avoid key errors when adding nested data
    messages: Dict[Protocol, Dict[MessageID, Dict[str, Timestamp]]] = defaultdict(
        lambda: defaultdict(dict)
    )

    # Regex pattern to match each line
    pattern = re.compile(r"(SENT|RECEIVED) (\S+) at ([\d.]+) - Protocol: (\w+)")

    with open(filename, "r") as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                action, msg_id, timestamp_str, protocol = match.groups()
                timestamp = float(timestamp_str)
                messages[protocol][msg_id][action.lower()] = (
                    timestamp  # lowercase: 'sent' or 'received'
                )

    return messages


def compute_metrics(
    messages: Dict[Protocol, Dict[MessageID, Dict[str, Timestamp]]],
) -> Dict[Protocol, dict]:
    """
    Computes average latency, min/max latency, and jitter for each protocol.

    Returns:
        A dictionary of metrics per protocol.
    """
    results: Dict[Protocol, dict] = {}

    for protocol, exchanges in messages.items():
        latencies: List[float] = []

        # Compute latencies only where both sent and received timestamps exist
        for msg_id, times in exchanges.items():
            if "sent" in times and "received" in times:
                latency = times["received"] - times["sent"]
                latencies.append(latency)

        if not latencies:
            continue  # Skip protocols with no complete messages

        # Sort to make jitter calculation consistent
        latencies.sort()
        avg_latency: float = sum(latencies) / len(latencies)
        min_latency: float = min(latencies)
        max_latency: float = max(latencies)

        # Jitter: average absolute difference between consecutive latencies
        jitter_values: List[float] = [
            abs(latencies[i] - latencies[i - 1]) for i in range(1, len(latencies))
        ]
        avg_jitter: float = (
            sum(jitter_values) / len(jitter_values) if jitter_values else 0.0
        )

        # Save metrics
        results[protocol] = {
            "average_latency": avg_latency,
            "min_latency": min_latency,
            "max_latency": max_latency,
            "jitter": avg_jitter,
            "samples": len(latencies),
        }

    return results


def main() -> None:
    """
    Main function that parses the log and prints computed metrics.
    """
    messages = parse_log("log.txt")
    metrics = compute_metrics(messages)

    for protocol, data in metrics.items():
        print(f"\nProtocol: {protocol.upper()}")
        print(f"  Samples: {data['samples']}")
        print(f"  Average Latency: {data['average_latency'] * 1000:.3f} ms")
        print(f"  Min Latency: {data['min_latency'] * 1000:.3f} ms")
        print(f"  Max Latency: {data['max_latency'] * 1000:.3f} ms")
        print(f"  Jitter: {data['jitter'] * 1000:.3f} ms")


if __name__ == "__main__":
    main()
