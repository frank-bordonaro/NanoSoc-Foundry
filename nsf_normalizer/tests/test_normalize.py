from normalizer.normalizer_core import normalize

def test_normalize_minimal():
    raw = {'@timestamp':'2025-12-01T00:00:00Z','host':'h1','source_ip':'1.2.3.4','dest_ip':'5.6.7.8','event':'auth'}
    c = normalize(raw)
    assert c['host']=='h1'
    assert c['src_ip']=='1.2.3.4'
    assert c['dst_ip']=='5.6.7.8'
    assert 'raw' in c
