from datetime import datetime

def normalize(raw_event: dict) -> dict:
    """Normalize various log formats into canonical schema.
    Schema: {timestamp, host, src_ip, dst_ip, event_type, raw}
    """
    ts = raw_event.get('timestamp') or raw_event.get('time') or raw_event.get('@timestamp')
    if isinstance(ts, (int, float)):
        try:
            ts = datetime.utcfromtimestamp(ts).isoformat() + 'Z'
        except Exception:
            ts = None

    host = raw_event.get('host') or raw_event.get('hostname') or raw_event.get('computer')
    src = raw_event.get('src_ip') or raw_event.get('source_ip') or raw_event.get('client_ip')
    dst = raw_event.get('dst_ip') or raw_event.get('dest_ip') or raw_event.get('server_ip')
    ev_type = raw_event.get('event_type') or raw_event.get('action') or raw_event.get('event')

    return {
        'timestamp': ts,
        'host': host,
        'src_ip': src,
        'dst_ip': dst,
        'event_type': ev_type,
        'raw': raw_event
    }
